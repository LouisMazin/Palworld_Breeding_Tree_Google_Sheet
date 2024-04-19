from flask import Flask
import Graph
app = Flask(__name__)

@app.route('/')
def start():
    return Graph.getJSONShortestWays("Frostallion","Frostallion")

Graph.getJSONShortestWays("Frostallion","Lamball")