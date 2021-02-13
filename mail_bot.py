import flask
from flask import jsonify
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "ok"})


@app.route('/cputemp', methods=['GET'])
def home():
    temp = os.popen("vcgencmd measure_temp").readline()
    return jsonify({"cpu": (temp.replace("temp=", "")})



app.run()
