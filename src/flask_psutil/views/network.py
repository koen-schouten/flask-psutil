from views.utils.string_validation import string_is_true, string_is_false, is_valid_connection_kind, is_valid_attrs
from views.utils.json_builder import recursively_build_json
from flask import jsonify, request, abort
import psutil

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


def api_net_if_addrs():
    return jsonify(recursively_build_json(psutil.net_if_addrs()))


def api_net_if_stats():
    return jsonify(recursively_build_json(psutil.net_if_stats()))