from flask import Flask
import Graph
app = Flask(__name__)

@app.route('/')
def start(*args):
    if(len(args) != 2):
        return "Invalid number of arguments"
    else:
        return args
    return Graph.getJSONShortestWays(args[0], args[1])