from flask import Flask, request
import Graph
app = Flask(__name__)
@app.route('/getWays')
def getWays():
    return Graph.getJSONShortestWays(request.args.get('parent'), request.args.get('child'),int(request.args.get('number')))

if __name__ == '__main__': 
    app.run(host='192.168.0.105') 