from flask import Flask, request
import Graph,os
app = Flask(__name__)
@app.route('/')
def index():
    os.system("sudo apt install graphviz")
@app.route('/getWays')
def getWays():
    return Graph.getJSONShortestWays(request.args.get('parent'), request.args.get('child'),int(request.args.get('number')))
