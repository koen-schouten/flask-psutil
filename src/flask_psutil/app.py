from flask import Flask, url_for, jsonify

from views.cpu import *
from views.disk import *
from views.memory import *
from views.misc import *
from views.network import *
from views.processes import *
from views.sensors import *

app = Flask(__name__)

#cpu
app.add_url_rule("/api/cpu_times", view_func=api_cpu_times, methods=['GET'])
app.add_url_rule("/api/cpu_percent", view_func=api_cpu_percent, methods=['GET'])
app.add_url_rule("/api/cpu_count", view_func=api_cpu_count, methods=['GET'])
app.add_url_rule("/api/cpu_stats", view_func=api_cpu_stats, methods=['GET'])
app.add_url_rule("/api/cpu_freq", view_func=api_cpu_freq, methods=['GET'])
app.add_url_rule("/api/getloadavg", view_func=api_getloadavg, methods=['GET'])

#disk
app.add_url_rule("/api/disk_partitions", view_func=api_disk_partitions, methods=['GET'])
app.add_url_rule("/api/disk_usage", view_func=api_disk_usage, methods=['GET'])
app.add_url_rule("/api/disk_io_counters", view_func=api_disk_io_counters, methods=['GET'])

#memory
app.add_url_rule("/api/virtual_memory", view_func=api_virtual_memory, methods=['GET'])
app.add_url_rule("/api/swap_memory", view_func=api_swap_memory, methods=['GET'])

#misc
app.add_url_rule("/api/boot_time", view_func=api_boot_time, methods=['GET'])
app.add_url_rule("/api/users", view_func=api_users, methods=['GET'])

#network
app.add_url_rule("/api/net_io_counters", view_func=api_net_io_counters, methods=['GET'])
app.add_url_rule("/api/net_connections", view_func=api_net_connections, methods=['GET'])
app.add_url_rule("/api/net_if_addrs", view_func=api_net_if_addrs, methods=['GET'])
app.add_url_rule("/api/net_if_stats", view_func=api_net_if_stats, methods=['GET'])

#processes
app.add_url_rule("/api/pids", view_func=api_pids, methods=['GET'])
app.add_url_rule("/api/process_list", view_func=api_process_iter, methods=['GET'])
app.add_url_rule("/api/process_iter", view_func=api_process_iter, methods=['GET'])
app.add_url_rule("/api/pid_exists", view_func=api_pid_exists, methods=['GET'])
app.add_url_rule("/api/process/as_dict", view_func=api_process, methods=['GET'])

#sensors
app.add_url_rule("/api/sensors_temperatures", view_func=api_sensors_temperatures, methods=['GET'])
app.add_url_rule("/api/sensors_fans", view_func=api_sensors_fans, methods=['GET'])
app.add_url_rule("/api/sensors_battery", view_func=api_sensors_battery, methods=['GET'])

#site-map
def rule_has_no_empty_params(rule):
    defaults = ()
    arguments = ()
    if rule.defaults is not None:
        defaults = rule.defaults
    if rule.arguments is not None:
        arguments = rule.arguments 
    return len(defaults) >= len(arguments)

@app.route("/api")
def site_map():
    url_list = []
    for rule in app.url_map.iter_rules():
        if(rule_has_no_empty_params(rule)):
            options = {}
            for arg in rule.arguments:
                options[arg] = "[{0}]".format(arg)

            methods = ','.join(rule.methods)
            url = url_for(rule.endpoint, **options)
            url = {
                "url" : url,
                "methods" : methods
            }
            url_list.append(url)

    return jsonify(url_list)