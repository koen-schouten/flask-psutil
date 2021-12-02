from utils.json_builder import recursively_build_json
from flask import jsonify
import psutil

def api_boot_time():
    return jsonify(psutil.boot_time())


def api_users():
    return jsonify(recursively_build_json(psutil.users()))
