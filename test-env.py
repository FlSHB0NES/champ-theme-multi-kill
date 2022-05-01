#Author         : Zane Chiang
#Summoner Name  : FlSHBONES
# Date          : April 30th, 2022

# IMPORTS

import requests
import json
from riotwatcher import LolWatcher, ApiError
import pandas as pd
import pprint
import time

def print_events(dict):

    for event in dict:
        print(event['EventName'])
        
# USER INFORMATION

api_key = "RGAPI-e8615c8d-9508-4e7c-b63e-74dd8f7e3974"
my_region = 'na1'
summoner_name = 'FlSHBONES'
query = 'eventdata'
cert_path = './riot/riotgames.pem'

stored_events = {}

while(True):

    # GET DATA
    response = requests.get(('https://127.0.0.1:2999/liveclientdata/' + query), verify=cert_path)
    events = json.loads(response.text)['Events']

    print_events(events)
    
    time.sleep(1)

