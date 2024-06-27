print(0)
from flask import Flask, request
print(1)
import Graph,os
print(2)
app = Flask(__name__)
print(3)
@app.route('/getWays')
def getWays():
    return Graph.getJSONShortestWays(request.args.get('parent'), request.args.get('child'),int(request.args.get('number')))
print(4)