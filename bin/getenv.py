#!/usr/bin/env python

import xml.etree.ElementTree as ET
import paramiko
import getpass

xml_local = '/tmp/environment.xml'


class XMLParser:
    def __init__(self):
        self.parsing = self

    def IPs(self):
        ParseXML = ET.parse(xml_local)
        doc_root = ParseXML.getroot()
        ip_addresses = []
        for i in doc_root.findall('.//DafilesrvProcess/Instance'):
            ip = i.attrib['netAddress']
            ip_addresses.append(ip)
        return ip_addresses
