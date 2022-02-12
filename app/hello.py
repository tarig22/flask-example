# -*- coding:utf-8 -*-

from flask import Flask, render_template
from flask_cors import CORS,cross_origin
import requests

def getData():
    url = requests.get("https://www.as-goal.com/m/").text
    x = url.find("<div id=\"Today\"")
    y = url.find("<div id=\"Tomorrow\"")
    return  "url[x:y]"


app = Flask(__name__)
CORS(app)

@app.route("/" , methods=['POST', 'GET','OPTIONS'])
@cross_origin()
def index():
    return getData() , 200, {'Content-Type': 'text/html; charset=UTF-8'}
#     return render_template("index.html", data=getData())


if __name__ == "__main__":
    app.debug = True
    app.run()

