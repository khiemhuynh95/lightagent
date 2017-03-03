import json
import os
import sys

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/', methods=['GET'])
def verify():
	

	return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    log(req)
    print("Request:")
    print(json.dumps(req, indent=4))

    return "ok", 200



if __name__ == '__main__':
    app.run(debug=True)