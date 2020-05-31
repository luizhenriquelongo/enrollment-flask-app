from flask import (
    json,
    Response,
)


# @app.route('/api/')
# @app.route('/api/<idx>')
# def api(idx=None):
#     if not idx:
#         jdata = courses_data
#     else:
#         jdata = courses_data[int(idx)]

#     return Response(json.dumps(jdata), mimetype="application/json")
