from flask import Flask, jsonify, request, abort
import psutil
from utils.string_validation import string_is_true, string_is_false, is_valid_connection_kind, is_valid_attrs
from utils.json_builder import recursively_build_json


app = Flask(__name__)


@app.route("/psutil/api/cpu_times", methods=['GET'])
def api_cpu_times():
    if string_is_true(request.args.get('percpu', '')):
        return jsonify(recursively_build_json(psutil.cpu_times(percpu=True)))
    else:
        return jsonify(recursively_build_json(psutil.cpu_times(percpu=False)))


@app.route("/psutil/api/cpu_percent", methods=['GET'])
def api_cpu_percent():
    interval_get_var = request.args.get('interval', '')
    interval = int(interval_get_var) if interval_get_var.isdigit() else 0
    if string_is_true(request.args.get('percpu', '')):
        return jsonify(recursively_build_json(psutil.cpu_percent(interval=interval, percpu=True)))
    else:
        return jsonify([recursively_build_json(psutil.cpu_percent(interval=interval, percpu=False))])


@app.route("/psutil/api/cpu_count", methods=['GET'])
def api_cpu_count():
    logical = True
    if string_is_false(request.args.get('logical', '')):
        logical = False
    return jsonify(recursively_build_json(psutil.cpu_count(logical=logical)))


@app.route("/psutil/api/cpu_stats", methods=['GET'])
def api_cpu_stats():
    return jsonify(recursively_build_json(psutil.cpu_stats()))


@app.route("/psutil/api/cpu_freq", methods=['GET'])
def api_cpu_freq():
    if string_is_true(request.args.get('percpu', '')):
        return jsonify(recursively_build_json(psutil.cpu_freq(percpu=True)))
    else:
        return jsonify([recursively_build_json(psutil.cpu_freq(percpu=False))])


@app.route("/psutil/api/getloadavg", methods=['GET'])
def api_getloadavg():
    return jsonify(psutil.getloadavg())


@app.route("/psutil/api/virtual_memory", methods=['GET'])
def api_virtual_memory():
    return jsonify(recursively_build_json(psutil.virtual_memory()))


@app.route("/psutil/api/swap_memory", methods=['GET'])
def api_swap_memory():
    return jsonify(recursively_build_json(psutil.swap_memory()._asdict()))


@app.route("/psutil/api/disk_partitions", methods=['GET'])
def api_disk_partitions():
    all = False
    if string_is_true(request.args.get('all', '')):
        all = True
    return jsonify(recursively_build_json(psutil.disk_partitions(all=all)))


@app.route("/psutil/api/disk_usage", methods=['GET'])
def api_disk_usage():
    path_get_arg = request.args.get('path', '')
    path = path_get_arg if path_get_arg else "/"
    try:
        return jsonify(recursively_build_json(psutil.disk_usage(path)))
    except:
        abort(400)


@app.route("/psutil/api/disk_io_counters", methods=['GET'])
def api_disk_io_counters():
    perdisk = False
    nowrap = True

    perdisk_get_arg = request.args.get('perdisk', '')
    nowrap_get_arg = request.args.get('nowrap', '')

    if string_is_true(perdisk_get_arg):
        perdisk = True
    if string_is_false(nowrap_get_arg):
        nowrap = False

    if perdisk:
        return jsonify(recursively_build_json(psutil.disk_io_counters(perdisk=perdisk, nowrap=nowrap)))
    else:
        return jsonify(recursively_build_json(psutil.disk_io_counters(perdisk=perdisk, nowrap=nowrap)))


@app.route("/psutil/api/net_io_counters", methods=['GET'])
def api_net_io_counters():
    pernic = False
    nowrap = True

    pernic_get_arg = request.args.get('pernic', '')
    nowrap_get_arg = request.args.get('nowrap', '')

    if string_is_true(pernic_get_arg):
        pernic = True

    if string_is_false(nowrap_get_arg):
        nowrap = False

    if pernic:
        return jsonify(recursively_build_json(pernic=pernic, nowrap=nowrap))
    else:
        return jsonify(recursively_build_json(psutil.net_io_counters(pernic=pernic, nowrap=nowrap)))


@app.route("/psutil/api/net_connections", methods=['GET'])
def api_net_connections():
    kind = ""
    kind_get_arg = request.args.get('kind', '')

    if is_valid_connection_kind(kind_get_arg):
        kind = kind_get_arg

    if kind:
        try:
            return jsonify(recursively_build_json(psutil.net_connections(kind=kind)))
        except:
            abort(400)
    else:
        try:
            return jsonify(recursively_build_json(psutil.net_connections()))
        except:
            abort(400)


@app.route("/psutil/api/net_if_addrs", methods=['GET'])
def api_net_if_addrs():
    return jsonify(recursively_build_json(psutil.net_if_addrs()))


@app.route("/psutil/api/net_if_stats", methods=['GET'])
def api_net_if_stats():
    return jsonify(recursively_build_json(psutil.net_if_stats()))


@app.route("/psutil/api/sensors_temperatures", methods=['GET'])
def api_sensors_temperatures():
    if hasattr(psutil, 'sensors_temperatures'):
        fahrenheit = False
        fahrenheit_get_arg = request.args.get('fahrenheit', '')
        if string_is_true(fahrenheit_get_arg):
            fahrenheit = True
        return jsonify(recursively_build_json(psutil.sensors_temperatures(fahrenheit=fahrenheit)))
    else:
        abort(405)


@app.route("/psutil/api/sensors_fans", methods=['GET'])
def api_sensors_fans():
    if hasattr(psutil, 'sensors_fans'):
        return jsonify(recursively_build_json(psutil.sensors_fans().items()))
    else:
        abort(405)


@app.route("/psutil/api/sensors_battery", methods=['GET'])
def api_sensors_battery():
    if hasattr(psutil, 'sensors_battery'):
        return jsonify(psutil.sensors_battery())
    else:
        abort(405)


@app.route("/psutil/api/boot_time", methods=['GET'])
def api_boot_time():
    return jsonify(psutil.boot_time())


@app.route("/psutil/api/users", methods=['GET'])
def api_users():
    return jsonify(recursively_build_json(psutil.users()))


@app.route("/psutil/api/pids", methods=['GET'])
def api_pids():
    return jsonify(psutil.pids())


@app.route("/psutil/api/process_list", methods=['GET'])
@app.route("/psutil/api/process_iter", methods=['GET'])
def api_process_iter():
    attrs = None
    ad_value = None

    attrs_get_vars = request.args.get('attrs', '')
    ad_value_get_var = request.args.get('ad_value', '')

    attrs_get_vars = attrs_get_vars.split(',')

    if len(attrs_get_vars) > 0:
        attrs = []
        for attr in attrs_get_vars:
            if is_valid_attrs(attr):
                attrs.append(attr)
    if ad_value_get_var:
        ad_value = ad_value_get_var
    
    return jsonify([recursively_build_json(p.as_dict()) for 
                    p in psutil.process_iter(attrs=attrs, ad_value=ad_value) if 
                    psutil.pid_exists(p.pid)])


@app.route("/psutil/api/pid_exists", methods=['GET'])
def api_pid_exists():
    pid_get_var = request.args.get('pid', '')

    if pid_get_var.isdigit():
        pid = int(pid_get_var)
        return jsonify(psutil.pid_exists(pid))
    else:
        abort(405)

@app.route("/psutil/api/process/as_dict", methods=['GET'])
def api_process():
    attrs = None

    pid_get_var = request.args.get('pid', '')
    attrs_get_vars = request.args.get('attrs', '')

    attrs_get_vars = attrs_get_vars.split(',')
    if len(attrs_get_vars) > 0:
        attrs = []
        for attr in attrs_get_vars:
            if is_valid_attrs(attr):
                attrs.append(attr)


    if pid_get_var.isdigit():
        pid = int(pid_get_var)
        if psutil.pid_exists(pid):
            return jsonify(recursively_build_json(psutil.Process(pid).as_dict(attrs=attrs)))
        else:
           abort(405) 
    else:
        return jsonify(recursively_build_json(psutil.Process().as_dict(attrs=attrs)))