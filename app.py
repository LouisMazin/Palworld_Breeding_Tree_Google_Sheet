from flask import Flask
import Graph
app = Flask(__name__)

@app.route('/<string:source>/<string:destination>')
def start(*args):
    return Graph.getJSONShortestWays(args[0], args[1])