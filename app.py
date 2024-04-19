from flask import Flask, request
import Graph,os
app = Flask(__name__)
@app.route('/')
def index():
    os.system('wget https://gitlab.com/graphviz/graphviz/-/package_files/6163716/download')
    os.system('tar -xf download')
    os.system('rm download')
    os.system('mv graphviz-2.46.0 graphviz')
    os.system('cd graphviz && ./configure && make && CPATH=[your_env]/include/python3.8 make install')
@app.route('/getWays')
def getWays():
    return Graph.getJSONShortestWays(request.args.get('parent'), request.args.get('child'),int(request.args.get('number')))
