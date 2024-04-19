from flask import Flask, request
import Graph
app = Flask(__name__)

@app.route('/getWays')
def getWays():
    if not request.args.get('number') == None:
        return Graph.getJSONShortestWays(request.args.get('parent'), request.args.get('child'),int(request.args.get('number')))