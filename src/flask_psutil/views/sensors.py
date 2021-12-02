from views.utils.string_validation import string_is_true
from views.utils.json_builder import recursively_build_json
from flask import jsonify, request, abort
import psutil


def api_sensors_temperatures():
    if hasattr(psutil, 'sensors_temperatures'):
        fahrenheit = False
        fahrenheit_get_arg = request.args.get('fahrenheit', '')
        if string_is_true(fahrenheit_get_arg):
            fahrenheit = True
        return jsonify(recursively_build_json(psutil.sensors_temperatures(fahrenheit=fahrenheit)))
    else:
        abort(405)


def api_sensors_fans():
    if hasattr(psutil, 'sensors_fans'):
        return jsonify(recursively_build_json(psutil.sensors_fans().items()))
    else:
        abort(405)


def api_sensors_battery():
    if hasattr(psutil, 'sensors_battery'):
        return jsonify(psutil.sensors_battery())
    else:
        abort(405)