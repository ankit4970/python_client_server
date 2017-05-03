#Python serial program sends data to server(using post request)
#sudo apt-get install python-serial on board

import datetime
import serial
import requests
import json

'''
port = serial.Serial("/dev/ttyTHS1", baudrate=115200, timeout=3.0)

def readSensorRaw():
    lines = port.read(18)
    return lines
	
def readSensorData():
	lines = readSensorRaw()
	print(lines)

def updateJsonFile():
    jsonFile = open("replayScript.json", "r") # Open the JSON file for reading
    data = json.load(jsonFile) # Read the JSON into the buffer
    jsonFile.close() # Close the JSON file

	# Working with buffered content
	tmp = data["location"] 
	data["location"] = path
	data["mode"] = "replay"

	#Save our changes to JSON file
	jsonFile = open("replayScript.json", "w+")
	jsonFile.write(json.dumps(data))
	jsonFile.close()
'''	
def post():
    #threading.Timer(1800.0, post).start()
    #temperature = read_temp()
    #data = temperature
    #data['room'] = 'Server Room'
    #print(data)

    #data=urllib.urlencode(data)
    #path='http://sample-env-3.rqytrpkkpi.us-west-2.elasticbeanstalk.com'    	#the url you want to POST to
    #req=urllib2.Request(path, data)
    #req.add_header("Content-type", "application/x-www-form-urlencoded")
    #page=urllib2.urlopen(req).read()
	
	#Only use this
	url = 'http://ec2-34-209-58-240.us-west-2.compute.amazonaws.com:3000/storeAlert'
	#url = "http://10.0.0.178:5000"
	#query = {'field': value}
	headers = {'Content-Type': 'application/json'}

	query = {	
				"sourceID" 		: "ankit1",
				"request_type" 	: "alert",
				"sourceType" 	: "device",
				"dataType" 		: "float",
				"deviceID" 		: "001",
				"location" 		: "xyz",
				"alertType" 	: "trash",
				"data" 			: "25.3", 
				"date" 			: "04272017",
				"time"			: "11:35",
				"checksum" 		: "10"
			};
		
	query['deviceID'] = 002		
	res = requests.post(url, data=json.dumps(query),headers=headers)
	print(res.text)
	
def main():
	post()
	#while true:
	#readSensorData()
		
main()
