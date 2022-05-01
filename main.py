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

api_key = ""
my_region = 'na1'
summoner_name = 'FlSHBONES'

print("API-key\t\t: " + api_key + "\nRegion\t\t: " + my_region + "\nSummoner\t: " + summoner_name)

try:

    # SET UP WATCHER
    #GET https://127.0.0.1:2999/liveclientdata/allgamedata
    request = 
    api_link = "https://" + my_region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name + "?api_key=" + api_key
    watcher = LolWatcher(api_key)

    # GET SUMMONER INFO
    me = watcher.summoner.by_name(my_region, summoner_name)

    print("\nSUMMONER INFO: ")
    pprint.pprint(me)

    # GET RANK

    my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])

    print("\nRANK:")
    pprint.pprint(my_ranked_stats)

except ApiError as err:
    if err.response.status_code == 429:
        print('We should retry in {} seconds.'.format(err.headers['Retry-After']))
        print('this retry-after is handled by default by the RiotWatcher library')
        print('future requests wait until the retry-after time passes')
    elif err.response.status_code == 404:
        print('Summoner with that ridiculous name not found.')
    else:
        raise
