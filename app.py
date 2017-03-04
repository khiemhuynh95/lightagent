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
    #print("Request:")
    #print(json.dumps(req, indent=4))
    result = req.get("result")
    parameters = result.get("parameters")

    action = parameters.get("action-type")
    print(action)
    color = parameters.get("color")
    print(color)

    process(action,color)

    return "ok", 200

def process(action,color):

	if action == "change":
		if color == "":
			pass
		elif color == "red":
			print("red") #replace for light action here
		elif color == "blue":
			print("blue")
		elif color == "green":
			print("green")
		elif color == "yellow":
			print("yellow")
		else:
			print("purple")
	elif action == "turn on":
		print("turn on")
	else:
		print("turn off")

if __name__ == '__main__':
    app.run(debug=True)