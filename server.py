import os
import datetime
import requests
from flask import Flask, request, send_file, jsonify

app = Flask(__name__)

@app.route('/logo.png')
def tracker():
    response_data = {
        "status": "success",
        "message": "This is a JSON response from /logo.png",
        "timestamp": datetime.datetime.now().isoformat(),
        "client_ip": request.remote_addr
    }
    return jsonify(response_data), 200 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)