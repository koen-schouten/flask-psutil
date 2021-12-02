from flask import Flask
from views.cpu import *
from views.disk import *
from views.memory import *
from views.misc import *
from views.network import *
from views.processes import *
from views.sensors import *

app = Flask(__name__)

#cpu
app.add_url_rule("/api/cpu_times",api_cpu_times, methods=['GET'])
app.add_url_rule("/api/cpu_percent",api_cpu_percent, methods=['GET'])
app.add_url_rule("/api/cpu_count",api_cpu_count, methods=['GET'])
app.add_url_rule("/api/cpu_stats",api_cpu_stats, methods=['GET'])
app.add_url_rule("/api/cpu_freq",api_cpu_freq, methods=['GET'])
app.add_url_rule("/api/getloadavg",api_getloadavg, methods=['GET'])

#disk
app.add_url_rule("/api/disk_partitions",api_disk_partitions, methods=['GET'])
app.add_url_rule("/api/disk_usage",api_disk_usage, methods=['GET'])
app.add_url_rule("/api/disk_io_counters",api_disk_io_counters, methods=['GET'])

#memory
app.add_url_rule("/api/virtual_memory",api_virtual_memory, methods=['GET'])
app.add_url_rule("/api/swap_memory",api_swap_memory, methods=['GET'])

#misc
app.add_url_rule("/api/boot_time",api_boot_time, methods=['GET'])
app.add_url_rule("/api/users",api_users, methods=['GET'])

#network
app.add_url_rule("/api/net_io_counters",api_net_io_counters, methods=['GET'])
app.add_url_rule("/api/net_connections",api_net_connections, methods=['GET'])
app.add_url_rule("/api/net_if_addrs",api_net_if_addrs, methods=['GET'])
app.add_url_rule("/api/net_if_stats",api_net_if_stats, methods=['GET'])

#processes
app.add_url_rule("/api/pids",api_pids, methods=['GET'])
app.add_url_rule("/api/process_list",api_process_iter, methods=['GET'])
app.add_url_rule("/api/process_iter",api_process_iter, methods=['GET'])
app.add_url_rule("/api/pid_exists",api_pid_exists, methods=['GET'])
app.add_url_rule("/api/process/as_dict",api_process, methods=['GET'])

#sensors
app.add_url_rule("/api/sensors_temperatures",api_sensors_temperatures, methods=['GET'])
app.add_url_rule("/api/sensors_fans",api_sensors_fans, methods=['GET'])
app.add_url_rule("/api/sensors_battery",api_sensors_battery, methods=['GET'])