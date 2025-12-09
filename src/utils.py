# src/utils.py

import requests                 # For making HTTP request to API
import json                     # For converting response to JSON format

def get_location():

    response = requests.get('http://ip-api.com/json')   # Call IP-based location API

    data = json.loads(response.text)                    # Convert API response to JSON

    return data['lat'], data['lon']                     # Return latitude and longitude
