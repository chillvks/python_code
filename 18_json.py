#!/usr/local/bin/python3

import urllib.parse
import requests

main_api = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
	address = input("ADDRESS: ")
	if address == 'quit' or address == 'q':
		break
		
	url = main_api + urllib.parse.urlencode({'address':address})
	json_data = requests.get(url).json()
	json_status = json_data["status"]
	print("URL: ",url)
	print("STATUS: ", json_status)
	
	if json_status == 'OK':
		for each in json_data["results"][0]["address_components"]:
			print(each["long_name"])
		print('Formatted Address: ', json_data["results"][0]["formatted_address"])
		print('Latitude: ',json_data["results"][0]["geometry"]["location"]["lat"])
		print('Longiude: ',json_data["results"][0]["geometry"]["location"]["lng"])
	else:
		print("Json is not correct")
