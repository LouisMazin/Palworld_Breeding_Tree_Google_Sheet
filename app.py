from flask import Flask, request
import Graph
app = Flask(__name__)
app.logger.disabled = True
@app.route('/getWays', methods=['GET'])
def getWays():
    return Graph.getJSONShortestWays(request.args.get('parent'), request.args.get('child'),int(request.args.get('number')))

app.run(host='0.0.0.0', port=1029)