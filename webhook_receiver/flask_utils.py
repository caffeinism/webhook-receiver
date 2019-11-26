from flask import request, abort

def get(dic, key):
    try:
        return dic[key]
    except KeyError:
        abort(400, f'Missing key: {key}')

def get_header(key):
    return get(request.headers, key)

def get_json():
    return request.json

def get_data():
    return request.data