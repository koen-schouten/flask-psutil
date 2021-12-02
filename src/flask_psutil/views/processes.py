from views.utils.string_validation import is_valid_attrs
from views.utils.json_builder import recursively_build_json
from flask import jsonify, request, abort
import psutil

def api_pids():
    return jsonify(psutil.pids())


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


def api_pid_exists():
    pid_get_var = request.args.get('pid', '')

    if pid_get_var.isdigit():
        pid = int(pid_get_var)
        return jsonify(psutil.pid_exists(pid))
    else:
        abort(405)

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