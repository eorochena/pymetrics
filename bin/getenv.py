#!/usr/bin/env python

import xml.etree.ElementTree as ET

xml_local = '/tmp/environment.xml'


class XMLParser:
    def __init__(self):
        self.parsing = self

    def IPs(self):
        parsexml = ET.parse(xml_local)
        doc_root = parsexml.getroot()
        ip_addresses = []
        for i in doc_root.findall('.//DafilesrvProcess/Instance'):
            ip = i.attrib['netAddress']
            ip_addresses.append(ip)
        return ip_addresses
