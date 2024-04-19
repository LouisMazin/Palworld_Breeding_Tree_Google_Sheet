from flask import Flask, request
import Graph
from os import environ,path
app = Flask(__name__)
environ["PATH"] += path.abspath(".\\Graphviz\\bin")+";"
@app.route('/getWays')
def getWays():
    return Graph.getJSONShortestWays(request.args.get('parent'), request.args.get('child'),int(request.args.get('number')))
