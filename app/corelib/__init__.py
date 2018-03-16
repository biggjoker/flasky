import requests
import json
from app import config


def auth_requests(method, *args, **kwargs):

    headers = {
        "Apitoken": json.dumps({"name": config['default'].NAME, "sig": config['default'].SIG})
    }

    if "name" in kwargs:
        headers["Apitoken"] = json.dumps({"name": kwargs["name"], "sig": config['default'].SIG})
        del kwargs["name"]

    if not kwargs:
        kwargs = {}

    if "headers" in kwargs:
        headers.update(kwargs["headers"])
        del kwargs["headers"]

    if method == "POST":
        return requests.post(*args, headers=headers, timeout=config['default'].REQUEST_TIMEOUT, **kwargs)
    elif method == "GET":
        return requests.get(*args, headers=headers, timeout=config['default'].REQUEST_TIMEOUT, **kwargs)
    elif method == "PUT":
        return requests.put(*args, headers=headers, timeout=config['default'].REQUEST_TIMEOUT, **kwargs)
    elif method == "DELETE":
        return requests.delete(*args, headers=headers, timeout=config['default'].REQUEST_TIMEOUT, **kwargs)
    else:
        raise Exception("invalid http method")
