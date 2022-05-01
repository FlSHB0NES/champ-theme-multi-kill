#Author         : Zane Chiang
#Summoner Name  : FlSHBONES
# Date          : April 30th, 2022

# IMPORTS

import requests
import json
from riotwatcher import LolWatcher, ApiError
import pandas as pd
import pprint

# USER INFORMATION

api_key = "RGAPI-e8615c8d-9508-4e7c-b63e-74dd8f7e3974"
my_region = 'na1'
summoner_name = 'FlSHBONES'
query = 'allgamedata'
cert_path = './riot/riotgames.pem'

# print("API-key\t\t: " + api_key + "\nRegion\t\t: " + my_region + "\nSummoner\t: " + summoner_name)

# SET UP WATCHER
#GET https://127.0.0.1:2999/liveclientdata/allgamedata
request = requests.get(('https://127.0.0.1:2999/liveclientdata/' + query), verify=cert_path)
print(request)
