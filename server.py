from flask import Flask,make_response
from datetime import datetime
from flask import jsonify, request, Response
import flask
import json

app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def getid():
	if request.method == "GET":
		r={'id' : '1'
    	}
		return json.dumps(r)
	else:
		data = json.loads(request.data)
		print(data)
		return json.dumps(data),201
    	

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
'''
@app.route('/device/', methods = ["POST"])
def device():
	data = json.loads(request.data)
	print(data)
	return json.dumps(data),201
'''


