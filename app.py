from flask import Flask, request
import Graph
app = Flask(__name__)

@app.route('/getWays', methods=['GET'])
def getWays():
    print("getWays : ", request.args.to_dict())
    return Graph.getJSONShortestWays(request.args.get('parent'), request.args.get('child'),int(request.args.get('number')))