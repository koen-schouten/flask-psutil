from views.utils.string_validation import string_is_true, string_is_false
from views.utils.json_builder import recursively_build_json
from flask import jsonify, request, abort
import psutil

def api_disk_partitions():
    all = False
    if string_is_true(request.args.get('all', '')):
        all = True
    return jsonify(recursively_build_json(psutil.disk_partitions(all=all)))


def api_disk_usage():
    path_get_arg = request.args.get('path', '')
    path = path_get_arg if path_get_arg else "/"
    try:
        return jsonify(recursively_build_json(psutil.disk_usage(path)))
    except:
        abort(400)


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