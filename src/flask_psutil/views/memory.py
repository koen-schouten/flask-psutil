from views.utils.json_builder import recursively_build_json
from flask import jsonify
import psutil

def api_virtual_memory():
    return jsonify(recursively_build_json(psutil.virtual_memory()))


def api_swap_memory():
    return jsonify(recursively_build_json(psutil.swap_memory()._asdict()))