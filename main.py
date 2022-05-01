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

print("API-key\t\t: " + api_key + "\nRegion\t\t: " + my_region + "\nSummoner\t: " + summoner_name + "\n")

# MAKE JSON REQUEST

api_link = "https://" + my_region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name + "?api_key=" + api_key
watcher = LolWatcher(api_key)
me = watcher.summoner.by_name(my_region, summoner_name)

print("SUMMONER INFO: ")
pprint.pprint(me)
