from flask import Flask
import Graph
app = Flask(__name__)

@app.route('/')
def start(*args):
    return Graph.getJSONShortestWays(args[0], args[1])