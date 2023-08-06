"""
NOTE: this file is DEPRECATED and will be removed soon

NB: adapted to work as a library for PDF extraction. Will probably be
re-written eventually to be correct, complete, and robust; this is just a
first iteration.

This script tries to extract everything from a GROBID TEI XML fulltext dump:

- header metadata
- affiliations
- references (with context)
- abstract
- fulltext
- tables, figures, equations

A flag can be specified to disable copyright encumbered bits (--no-emcumbered):

- abstract
- fulltext
- tables, figures, equations

Prints JSON to stdout, errors to stderr

This file copied from the sandcrawler repository.
"""

import io
import json
import xml.etree.ElementTree as ET
from typing import Any, AnyStr, Dict, List, Optional

from .types import *

xml_ns = "http://www.w3.org/XML/1998/namespace"
ns = "http://www.tei-c.org/ns/1.0"


def all_authors(elem: Optional[ET.Element],
                ns: str = ns) -> List[Dict[str, Any]]:
    if not elem:
        return []
    names = []
    for author in elem.findall(".//{%s}author" % ns):
        pn = author.find("./{%s}persName" % ns)
        if not pn:
            continue
        given_name = pn.findtext("./{%s}forename" % ns) or None
        surname = pn.findtext("./{%s}surname" % ns) or None
        full_name = " ".join([t.strip() for t in pn.itertext()
                              if t.strip()]).strip()
        obj: Dict[str, Any] = dict(name=full_name)
        if given_name:
            obj["given_name"] = given_name
        if surname:
            obj["surname"] = surname
        ae = author.find("./{%s}affiliation" % ns)
        if ae:
            affiliation: Dict[str, Any] = dict()
            for on in ae.findall("./{%s}orgName" % ns):
                on_type = on.get("type")
                if on_type:
                    affiliation[on_type] = on.text
            addr_e = ae.find("./{%s}address" % ns)
            if addr_e:
                address = dict()
                for t in addr_e.getchildren():
                    address[t.tag.split("}")[-1]] = t.text
                if address:
                    affiliation["address"] = address
                # affiliation['address'] = {
                #    'post_code': addr.findtext('./{%s}postCode' % ns) or None,
                #    'settlement': addr.findtext('./{%s}settlement' % ns) or None,
                #    'country': addr.findtext('./{%s}country' % ns) or None,
                # }
            obj["affiliation"] = affiliation
        names.append(obj)
    return names


def journal_info(elem: ET.Element) -> Dict[str, Any]:
    journal = dict()
    journal["name"] = elem.findtext(f".//{{{ns}}}monogr/{{{ns}}}title")
    journal["publisher"] = elem.findtext(
        f".//{{{ns}}}publicationStmt/{{{ns}}}publisher")
    if journal["publisher"] == "":
        journal["publisher"] = None
    journal["issn"] = elem.findtext('.//{%s}idno[@type="ISSN"]' % ns)
    journal["eissn"] = elem.findtext('.//{%s}idno[@type="eISSN"]' % ns)
    journal["volume"] = elem.findtext('.//{%s}biblScope[@unit="volume"]' % ns)
    journal["issue"] = elem.findtext('.//{%s}biblScope[@unit="issue"]' % ns)
    keys = list(journal.keys())

    # remove empty/null keys
    for k in keys:
        if not journal[k]:
            journal.pop(k)
    return journal


def biblio_info(elem: ET.Element, ns: str = ns) -> Dict[str, Any]:
    ref: Dict[str, Any] = dict()
    ref["id"] = elem.attrib.get("{http://www.w3.org/XML/1998/namespace}id")
    ref["unstructured"] = elem.findtext('.//{%s}note[@type="raw_reference"]' %
                                        ns)
    # Title stuff is messy in references...
    ref["title"] = elem.findtext(f".//{{{ns}}}analytic/{{{ns}}}title")
    other_title = elem.findtext(f".//{{{ns}}}monogr/{{{ns}}}title")
    if other_title:
        if ref["title"]:
            ref["journal"] = other_title
        else:
            ref["journal"] = None
            ref["title"] = other_title
    ref["authors"] = all_authors(elem, ns=ns)
    ref["publisher"] = elem.findtext(
        f".//{{{ns}}}publicationStmt/{{{ns}}}publisher")
    if not ref["publisher"]:
        ref["publisher"] = elem.findtext(
            f".//{{{ns}}}imprint/{{{ns}}}publisher")
    if ref["publisher"] == "":
        ref["publisher"] = None
    date = elem.find('.//{%s}date[@type="published"]' % ns)
    ref["date"] = (date is not None) and date.attrib.get("when")
    ref["volume"] = elem.findtext('.//{%s}biblScope[@unit="volume"]' % ns)
    ref["issue"] = elem.findtext('.//{%s}biblScope[@unit="issue"]' % ns)
    ref["doi"] = elem.findtext('.//{%s}idno[@type="DOI"]' % ns)
    ref["arxiv_id"] = elem.findtext('.//{%s}idno[@type="arXiv"]' % ns)
    if ref["arxiv_id"] and ref["arxiv_id"].startswith("arXiv:"):
        ref["arxiv_id"] = ref["arxiv_id"][6:]
    ref["pmcid"] = elem.findtext('.//{%s}idno[@type="PMCID"]' % ns)
    ref["pmid"] = elem.findtext('.//{%s}idno[@type="PMID"]' % ns)
    el = elem.find('.//{%s}biblScope[@unit="page"]' % ns)
    if el is not None:
        if el.attrib.get("from") and el.attrib.get("to"):
            ref["pages"] = "{}-{}".format(el.attrib["from"], el.attrib["to"])
        else:
            ref["pages"] = el.text
    el = elem.find(".//{%s}ptr[@target]" % ns)
    if el is not None:
        ref["url"] = el.attrib["target"]
        # Hand correction
        # TODO: move this elsewhere
        if ref["url"].endswith(".Lastaccessed"):
            ref["url"] = ref["url"].replace(".Lastaccessed", "")
        if ref["url"].startswith("<"):
            ref["url"] = ref["url"][1:]
        if ">" in ref["url"]:
            ref["url"] = ref["url"].split(">")[0]
    else:
        ref["url"] = None
    return ref


def teixml2json(content: AnyStr, encumbered: bool = True) -> Dict[str, Any]:

    if isinstance(content, str):
        tree = ET.parse(io.StringIO(content))
    elif isinstance(content, bytes):
        tree = ET.parse(io.BytesIO(content))

    info: Dict[str, Any] = dict()

    # print(content)
    # print(content.getvalue())
    tei = tree.getroot()

    header = tei.find(".//{%s}teiHeader" % ns)
    if header is None:
        raise ValueError("XML does not look like TEI format")
    application_tag = header.findall(
        f".//{{{ns}}}appInfo/{{{ns}}}application")[0]
    info["grobid_version"] = application_tag.attrib["version"].strip()
    info["grobid_timestamp"] = application_tag.attrib["when"].strip()
    info["title"] = header.findtext(f".//{{{ns}}}analytic/{{{ns}}}title")
    info["authors"] = all_authors(
        header.find(f".//{{{ns}}}sourceDesc/{{{ns}}}biblStruct"))
    info["journal"] = journal_info(header)
    date = header.find('.//{%s}date[@type="published"]' % ns)
    info["date"] = (date is not None) and date.attrib.get("when")
    info["fatcat_release"] = header.findtext('.//{%s}idno[@type="fatcat"]' %
                                             ns)
    info["doi"] = header.findtext('.//{%s}idno[@type="DOI"]' % ns)
    if info["doi"]:
        info["doi"] = info["doi"].lower()

    refs = []
    for (i, bs) in enumerate(
            tei.findall(f".//{{{ns}}}listBibl/{{{ns}}}biblStruct")):
        ref = biblio_info(bs)
        ref["index"] = i
        refs.append(ref)
    info["citations"] = refs

    text = tei.find(".//{%s}text" % (ns))
    # print(text.attrib)
    if text and text.attrib.get("{%s}lang" % xml_ns):
        info["language_code"] = text.attrib["{%s}lang" % xml_ns]  # xml:lang

    if encumbered:
        el = tei.find(f".//{{{ns}}}profileDesc/{{{ns}}}abstract")
        info["abstract"] = (el or None) and " ".join(el.itertext()).strip()
        el = tei.find(f".//{{{ns}}}text/{{{ns}}}body")
        info["body"] = (el or None) and " ".join(el.itertext()).strip()
        el = tei.find(f'.//{{{ns}}}back/{{{ns}}}div[@type="acknowledgement"]')
        info["acknowledgement"] = (el or None) and " ".join(
            el.itertext()).strip()
        el = tei.find(f'.//{{{ns}}}back/{{{ns}}}div[@type="annex"]')
        info["annex"] = (el or None) and " ".join(el.itertext()).strip()

    # remove empty/null keys
    keys = list(info.keys())
    for k in keys:
        if not info[k]:
            info.pop(k)
    return info


def transform_grobid_ref_xml(raw_xml: str) -> Optional[dict]:
    """
    Parses GROBID XML for the case of a single reference/citation string (eg,
    not a full/propper TEI-XML fulltext document), and returns a dict.
    """
    # first, remove any xmlns stuff, for consistent parsing
    raw_xml = raw_xml.replace('xmlns="http://www.tei-c.org/ns/1.0"', "")
    tree = ET.parse(io.StringIO(raw_xml))
    root = tree.getroot()
    ref = biblio_info(root, ns="")
    if not any(ref.values()):
        return None
    return ref
