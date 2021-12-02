from utils.string_validation import string_is_true, string_is_false, is_valid_connection_kind, is_valid_attrs
from utils.json_builder import recursively_build_json
from flask import jsonify, request
import psutil

def api_cpu_times():
    if string_is_true(request.args.get('percpu', '')):
        return jsonify(recursively_build_json(psutil.cpu_times(percpu=True)))
    else:
        return jsonify(recursively_build_json(psutil.cpu_times(percpu=False)))


def api_cpu_percent():
    interval_get_var = request.args.get('interval', '')
    interval = int(interval_get_var) if interval_get_var.isdigit() else 0
    if string_is_true(request.args.get('percpu', '')):
        return jsonify(recursively_build_json(psutil.cpu_percent(interval=interval, percpu=True)))
    else:
        return jsonify([recursively_build_json(psutil.cpu_percent(interval=interval, percpu=False))])


def api_cpu_count():
    logical = True
    if string_is_false(request.args.get('logical', '')):
        logical = False
    return jsonify(recursively_build_json(psutil.cpu_count(logical=logical)))


def api_cpu_stats():
    return jsonify(recursively_build_json(psutil.cpu_stats()))


def api_cpu_freq():
    if string_is_true(request.args.get('percpu', '')):
        return jsonify(recursively_build_json(psutil.cpu_freq(percpu=True)))
    else:
        return jsonify([recursively_build_json(psutil.cpu_freq(percpu=False))])


def api_getloadavg():
    return jsonify(psutil.getloadavg())


