from flask import Response
import json


def make_respose(data: dict, status_code: int = 200, mimetype='application/json') -> Response:
    return Response(
        json.dumps(data),
        status=status_code,
        mimetype='application/json'
    )