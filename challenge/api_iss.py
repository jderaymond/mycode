#!/usr/bin/env python3

import requests
import time

API = 'http://api.open-notify.org/iss-now.json'

def main():
    resp = requests.get(API).json()
    lon = resp['iss_position']['longitude']
    lat = resp['iss_position']['latitude']
    timestamp= resp['timestamp']
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timestamp))
    print(f"CURRENT LOCATION OF THE ISS: \nTimestamp: {timestamp}\nLon: {lon}\nLat: {lat}")
main()
