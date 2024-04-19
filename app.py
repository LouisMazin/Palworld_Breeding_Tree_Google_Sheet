from flask import Flask
import Graph
app = Flask(__name__)

@app.route('/<string:source>/<string:destination>')
def start(*args):
    if(len(args) != 2):
        return "Invalid number of arguments"
    return Graph.getJSONShortestWays(args[0], args[1])