#!/usr/bin/env python

import easysnmp
import socket
import time
import getenv
import os

graphite_server = '192.168.1.100'
port = 2003

# Get hpcc component name
roxie_name = os.popen("service hpcc-init -c roxie status|awk '{print $1}'").readline().replace('\n', '')

sender = socket.socket()
sender.connect((graphite_server, port))

server_list = getenv.XMLParser()

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

# Disk IO /media/disk1
bytes_read_since_boot_disk1 = '1.3.6.1.4.1.2021.13.15.1.1.3.28'
bytes_written_since_boot_disk1 = '1.3.6.1.4.1.2021.13.15.1.1.4.28'
bytes_read_accesses_since_boot_disk1 = '1.3.6.1.4.1.2021.13.15.1.1.5.28'
bytes_write_accesses_since_boot_disk1 = '1.3.6.1.4.1.2021.13.15.1.1.6.28'

# Disk IO /media/disk2
bytes_read_since_boot_disk2 = '1.3.6.1.4.1.2021.13.15.1.1.3.30'
bytes_written_since_boot_disk2 = '1.3.6.1.4.1.2021.13.15.1.1.4.30'
bytes_read_accesses_since_boot_disk2 = '1.3.6.1.4.1.2021.13.15.1.1.5.30'
bytes_write_accesses_since_boot_disk2 = '1.3.6.1.4.1.2021.13.15.1.1.6.30'



while True:
    for server in server_list.IPs():
        get_load_1 = easysnmp.snmp_get(load_1, hostname=server, community='public', version=2)
        result = '%s.%s.load1.%s %s %d\n' % (roxie_name, server.replace('.', '_').replace('\n', ''),
                                             'count', get_load_1.value, time.time())
        sender.sendall(result)

        get_load_5 = easysnmp.snmp_get(load_5, hostname=server, community='public', version=2)
        result = '%s.%s.load5.%s %s %d\n' % (roxie_name, server.replace('.', '_').replace('\n', ''),
                                             'count', get_load_5.value, time.time())
        sender.sendall(result)

        get_load_15 = easysnmp.snmp_get(load_15, hostname=server, community='public', version=2)
        result = '%s.load15.%s %s %d\n' % (server.replace('.', '_').replace('\n', ''), 'count', get_load_15.value,
                                           time.time())
        sender.sendall(result)

        get_user_cpu_time = easysnmp.snmp_get(user_cpu_time, hostname=server, community='public', version=2)
        result = '%s.%s.user_cpu_time.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', get_user_cpu_time.value, time.time())
        sender.sendall(result)

        get_raw_user_cpu_time = easysnmp.snmp_get(raw_user_cpu_time, hostname=server, community='public', version=2)
        result = '%s.%s.raw_user_cpu_time.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', get_raw_user_cpu_time.value, time.time
        ())
        sender.sendall(result)

        get_percentage_cpu_time = easysnmp.snmp_get(percentage_cpu_time, hostname=server, community='public', version=2)
        result = '%s.%s.percentage_cpu_time.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', get_percentage_cpu_time.value, time.
        time())
        sender.sendall(result)

        get_raw_system_cpu_time = easysnmp.snmp_get(raw_system_cpu_time, hostname=server, community='public', version=2)
        result = '%s.%s.raw_system_cpu_time.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', get_raw_system_cpu_time.value, time.time())
        sender.sendall(result)

        get_percentage_idle_cpu_time = easysnmp.snmp_get(percentage_idle_cpu_time, hostname=server, community='public',
                                                         version=2)
        result = '%s.%s.percentage_idle_cpu_time.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', get_percentage_idle_cpu_time.value, time.time())
        sender.sendall(result)

        get_raw_idle_cpu_time = easysnmp.snmp_get(raw_idle_cpu_time, hostname=server, community='public', version=2)
        result = '%s.%s.raw_system_cpu_time.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', get_raw_idle_cpu_time.value, time.time())

        get_raw_nice_cpu_time = easysnmp.snmp_get(raw_nice_cpu_time, hostname=server, community='public', version=2)
        result = '%s.%s.raw_nice_cpu_time.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', get_raw_nice_cpu_time.value, time.time
        ())
        sender.sendall(result)

        get_total_cpu_count = easysnmp.snmp_walk(total_cpu_count, hostname=server, community='public', version=2)
        result = '%s.%s.total_cpu_count.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', len(get_total_cpu_count), time.time())
        sender.sendall(result)

        get_total_swap_size = easysnmp.snmp_get(total_swap_size, hostname=server, community='public', version=2)
        result = '%s.%s.total_swap_size.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', get_total_swap_size.value, time.time())
        sender.sendall(result)

        get_available_swap_space = easysnmp.snmp_get(available_swap_space, hostname=server, community='public',
                                                     version=2)
        result = '%s.%s.available_swap_space.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', get_available_swap_space.value, time.time())
        sender.sendall(result)

        get_total_ram_in_machine = easysnmp.snmp_get(total_ram_in_machine, hostname=server, community='public',
                                                     version=2)
        result = '%s.%s.total_ram_in_machine.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', get_total_ram_in_machine.value, time.time())
        sender.sendall(result)

        get_total_ram_used = easysnmp.snmp_get(total_ram_used, hostname=server, community='public', version=2)
        result = '%s.%s.total_ram_used.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', get_total_ram_used.value, time.time())
        sender.sendall(result)

        get_total_ram_free = easysnmp.snmp_get(total_ram_free, hostname=server, community='public', version=2)
        result = '%s.%s.total_ram_free.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', get_total_ram_free.value, time.time())
        sender.sendall(result)

        get_total_ram_shared = easysnmp.snmp_get(total_ram_shared, hostname=server, community='public', version=2)
        result = '%s.%s.total_ram_shared.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', get_total_ram_shared.value, time.time()
        )
        sender.sendall(result)

        get_total_ram_buffered = easysnmp.snmp_get(total_ram_buffered, hostname=server, community='public', version=2)
        result = '%s.%s.total_ram_buffered.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', get_total_ram_buffered.value, time.time())
        sender.sendall(result)

        get_total_cached_memory = easysnmp.snmp_get(total_cached_memory, hostname=server, community='public', version=2)
        result = '%s.%s.total_cached_memory.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', get_total_cached_memory.value, time.time())
        sender.sendall(result)

        get_total_disk_space_disk1 = easysnmp.snmp_get(total_disk_space_disk1, hostname=server, community='public',
                                                       version=2)
        result = '%s.%s.total_disk_space_disk1.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', get_total_disk_space_disk1.value,
        time.time())
        sender.sendall(result)

        get_available_disk_space_disk1 = easysnmp.snmp_get(available_disk_space_disk1, hostname=server,
                                                           community='public', version=2)
        result = '%s.%s.available_disk_space_disk1.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', get_available_disk_space_disk1.value,
        time.time())
        sender.sendall(result)

        get_used_disk_space_disk1 = easysnmp.snmp_get(used_disk_space_disk1, hostname=server, community='public',
                                                      version=2)
        result = '%s.%s.used_disk_space_disk1.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', get_used_disk_space_disk1.value, time.time())
        sender.sendall(result)

        get_total_disk_space_disk2 = easysnmp.snmp_get(total_disk_space_disk2, hostname=server, community='public',
                                                       version=2)
        result = '%s.%s.total_disk_space_disk2.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', get_total_disk_space_disk2.value,
        time.time())
        sender.sendall(result)

        get_available_disk_space_disk2 = easysnmp.snmp_get(available_disk_space_disk2, hostname=server,
                                                           community='public', version=2)
        result = '%s.%s.available_disk_space_disk2.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', get_available_disk_space_disk2.value,
        time.time())
        sender.sendall(result)

        get_used_disk_space_disk2 = easysnmp.snmp_get(used_disk_space_disk2, hostname=server, community='public',
                                                      version=2)
        result = '%s.%s.used_disk_space_disk2.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', get_used_disk_space_disk2.value, time.time())
        sender.sendall(result)

        get_bytes_read_since_boot_disk1 = easysnmp.snmp_get(bytes_read_since_boot_disk1, hostname=server,
                                                            community='public', version=2)
        result = '%s.%s.bytes_read_since_boot_disk1.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', get_bytes_read_since_boot_disk1.value,
        time.time())
        sender.sendall(result)

        get_bytes_written_since_boot_disk1 = easysnmp.snmp_get(bytes_written_since_boot_disk1, hostname=server,
                                                               community='public', version=2)
        result = '%s.%s.bytes_written_since_boot_disk1.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', get_bytes_written_since_boot_disk1.value,
        time.time())
        sender.sendall(result)

        get_bytes_read_accesses_since_boot_disk1 = easysnmp.snmp_get(bytes_read_accesses_since_boot_disk1,
                                                                     hostname=server, community='public', version=2)
        result = '%s.%s.bytes_read_accesses_since_boot_disk1.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', get_bytes_read_accesses_since_boot_disk1.value,
        time.time())
        sender.sendall(result)

        get_bytes_write_accesses_since_boot_disk1 = easysnmp.snmp_get(bytes_write_accesses_since_boot_disk1,
                                                                      hostname=server, community='public', version=2)
        result = '%s.%s.bytes_write_accesses_since_boot_disk1.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count',
        get_bytes_write_accesses_since_boot_disk1.value, time.time())
        sender.sendall(result)

        get_bytes_read_since_boot_disk2 = easysnmp.snmp_get(bytes_read_since_boot_disk2, hostname=server,
                                                            community='public', version=2)
        result = '%s.%s.bytes_read_since_boot_disk2.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count',
        get_bytes_read_since_boot_disk2.value, time.time())
        sender.sendall(result)

        get_bytes_written_since_boot_disk2 = easysnmp.snmp_get(bytes_written_since_boot_disk2, hostname=server,
                                                               community='public', version=2)
        result = '%s.%s.bytes_written_since_boot_disk2.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count', get_bytes_written_since_boot_disk2.value,
        time.time())
        sender.sendall(result)

        get_bytes_read_accesses_since_boot_disk2 = easysnmp.snmp_get(bytes_read_accesses_since_boot_disk2,
                                                                     hostname=server, community='public', version=2)
        result = '%s.%s.bytes_read_accesses_since_boot_disk2.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count',
        get_bytes_read_accesses_since_boot_disk2.value, time.time())
        sender.sendall(result)

        get_bytes_write_accesses_since_boot_disk2 = easysnmp.snmp_get(bytes_write_accesses_since_boot_disk2,
                                                                      hostname=server, community='public', version=2)
        result = '%s.%s.bytes_write_accesses_since_boot_disk2.%s %s %d\n' % (
        roxie_name, server.replace('.', '_').replace('\n', ''), 'count',
        get_bytes_write_accesses_since_boot_disk2.value, time.time())

        time.sleep(1)
