#!/usr/bin/env python

import easysnmp
import socket
import time
import getenv

graphite_server = '192.168.1.100'
port = 2003

sender = socket.socket()
sender.connect((graphite_server, port))

server_list = getenv.XMLParser()
print(server_list.IPs())

# Load
load_1 = '1.3.6.1.4.1.2021.10.1.3.1'
load_5 = '1.3.6.1.4.1.2021.10.1.3.2'
load_15 = '1.3.6.1.4.1.2021.10.1.3.3'

# CPU
user_cpu_time = '1.3.6.1.4.1.2021.11.9.0'
raw_user_cpu_time = '1.3.6.1.4.1.2021.11.50.0'
percentage_cpu_time = '1.3.6.1.4.1.2021.11.10.0'
raw_system_cpu_time = '1.3.6.1.4.1.2021.11.52.0'
percentage_idle_cpu_time = '1.3.6.1.4.1.2021.11.11.0'
raw_idle_cpu_time = '1.3.6.1.4.1.2021.11.53.0'
raw_nice_cpu_time = '1.3.6.1.4.1.2021.11.51.0'
total_cpu_count = '1.3.6.1.2.1.25.3.3.1.2'

# Memory Statistics
total_swap_size = '1.3.6.1.4.1.2021.4.3.0'
available_swap_space = '1.3.6.1.4.1.2021.4.4.0'
total_ram_in_machine = '1.3.6.1.4.1.2021.4.5.0'
total_ram_used = '1.3.6.1.4.1.2021.4.6.0'
total_ram_free = '1.3.6.1.4.1.2021.4.11.0'
total_ram_shared = '1.3.6.1.4.1.2021.4.13.0'
total_ram_buffered = '1.3.6.1.4.1.2021.4.14.0'
total_cached_memory = '1.3.6.1.4.1.2021.4.15.0'

# Storage /
total_disk_space = '1.3.6.1.4.1.2021.9.1.6.1'
available_disk_space = '1.3.6.1.4.1.2021.9.1.7.1'
used_disk_space = '1.3.6.1.4.1.2021.9.1.8.1'

# Storage /media/disk1
total_disk_space_disk1 = '1.3.6.1.4.1.2021.9.1.6.7'
available_disk_space_disk1 = '1.3.6.1.4.1.2021.9.1.7.7'
used_disk_space_disk1 = '1.3.6.1.4.1.2021.9.1.8.7'

# Storage /media/disk2
total_disk_space_disk2 = '1.3.6.1.4.1.2021.9.1.6.8'
available_disk_space_disk2 = '1.3.6.1.4.1.2021.9.1.7.8'
used_disk_space_disk2 = '1.3.6.1.4.1.2021.9.1.8.8'

while True:
    for server in server_list.IPs():
        get_load_1 = easysnmp.snmp_get(load_1, hostname=server, community='public', version=2)
        result = '%s.load1.%s %s %d\n' % (server.replace('.', '_').replace('\n', ''), 'count', get_load_1.value, time.time())
        sender.sendall(result)

        get_load_5 = easysnmp.snmp_get(load_5, hostname=server, community='public', version=2)
        result = '%s.load5.%s %s %d\n' % (server.replace('.', '_').replace('\n', ''), 'count', get_load_5.value, time.time())
        sender.sendall(result)

        get_load_15 = easysnmp.snmp_get(load_15, hostname=server, community='public', version=2)
        result = '%s.load15.%s %s %d\n' % (server.replace('.', '_').replace('\n', ''), 'count', get_load_15.value, time.time())
        sender.sendall(result)
