# src/utils.py
import requests
import json

def get_location():
    response = requests.get('http://ip-api.com/json')
    data = json.loads(response.text)
    return data['lat'], data['lon']