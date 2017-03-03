from flask import Flask
from flask import Response, send_from_directory, render_template, request
from ivandb import DB
import json as JS

app = Flask(__name__)
"""
Ver tema del login

"""

@app.route("/")
def hola():
    ret =  JS.dumps({"hola": "ivan"})
    resp = Response(ret, status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route("/sendmsg", methods=['POST'])
def sendmsg():

    json = request.get_json(force=True)
    db = DB()
    ret = db.nuevoMensaje(json)

    resp = Response(ret, status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route("/getmsg", methods=['POST'])
def getmsg():
    json = request.get_json(force=True)
    db = DB()
    ret = db.getMsgs(json)

    resp = Response(ret, status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)