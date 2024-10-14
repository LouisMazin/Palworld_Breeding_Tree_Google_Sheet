from flask import Flask, request
import Graph
app = Flask(__name__)
@app.route('/getWays')
def getWays():
    return Graph.getJSONShortestWays(request.args.get('parent'), request.args.get('child'),int(request.args.get('number')))
app.run(host='77.207.48.109',port=1029)