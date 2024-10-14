from flask import Flask, request
import Graph

import os
import subprocess

def obtain_ssl_certificate(domain):
    # Command to run Certbot
    command = [
        'certbot', 'certonly', '--standalone',
        '--non-interactive', '--agree-tos',
        '-m mazinlouis79@gmail.com',  # Replace with your email
        '-d', domain
    ]
    
    try:
        # Run the command to obtain the SSL certificate
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("SSL certificate obtained successfully!")
    except subprocess.CalledProcessError as e:
        print("Error obtaining SSL certificate:")
        print(e.stderr.decode())

# Call the function with your domain name
obtain_ssl_certificate('panel.louismazin.com')

app = Flask(__name__)
@app.route('/getWays')
def getWays():
    return Graph.getJSONShortestWays(request.args.get('parent'), request.args.get('child'),int(request.args.get('number')))