#!/usr/bin/python

import easysnmp
import socket
import time

graphite_server = '192.168.1.121'
port = 2003

sender = socket.socket()
sender.connect((graphite_server, port))

cpu_load_15 = easysnmp.snmp_get('1.3.6.1.4.1.2021.10.1.3.3', hostname='192.168.1.100', community='public', version=2)
result = '%s.%s %s %s' % ('Polaris', 'count', cpu_load_15.value.replace('.','_'), time.time())
sender.sendall(result)