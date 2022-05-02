#Author         : Zane Chiang
#Summoner Name  : FlSHBONES
# Date          : April 30th, 2022

# IMPORTS

import requests
import json
import time
import subprocess

# METHOD TO PRINT ALL EVENT NAMES OF GIVEN DICT
# @PARAM dict: DICTIONARY TO PRINT
def print_events(dict):

    for event in dict:
        print(event['EventName'])

# METHOD TO FIND AN EVENT WITHIN A DICTIONARY
# @PARAM events : DICTIONARY TO SEARCH
# @PARAM eventID: EVENTID TO MATCH
# @RETURN EVENT IF FOUND, ELSE RETURN FALSE
def find_event(events, eventID):
    for event in events:
        if(event['EventID'] == eventID):
            return event
    return False

# JINX AUDIO FILES

audio_file1 = "./riot/champ-theme/Jinx/get-jinxed_1.mp3" # Single Kill
audio_file2 = "./riot/champ-theme/Jinx/get-jinxed_2.mp3" # Double Kill
audio_file3 = "./riot/champ-theme/Jinx/get-jinxed_3.mp3" # Triple Kill
audio_file4 = "./riot/champ-theme/Jinx/get-jinxed_4.mp3" # Quadra Kill

query = 'eventdata'

# PARAMETERS
IGN = 'FlSHBONES'
REFRESH_RATE = 0.2

stored_events = {}

while(True):

    # GET DATA
    response = requests.get(('https://127.0.0.1:2999/liveclientdata/' + query), verify=cert_path)
    events = json.loads(response.text)['Events']

    # IF THERE ARE NEW EVENTS

    if(len(stored_events) != len(events)):

        num_new_events = len(events) - len(stored_events) # Number of new events

        # PRINT NEW EVENTS

        for eventID in range(len(events) - num_new_events, len(events)):

            event = find_event(events, eventID) # Get Event
            print(event['EventName'])
            
            # IF SUMMONER KILLS CHAMPION

            if(event['EventName'] == 'ChampionKill' and event['KillerName'] == IGN):

                next_event = find_event(events, eventID) # Search for a next event

                # IF SUBSEQUENT EVENT IS A MULTI-KILL, DON'T PLAY 1ST KILL AUDIO

                if(next_event != False and next_event['EventName'] == 'Multikill'):
                    pass
                else:
                    return_code = subprocess.call(["afplay", audio_file1])
            
            # IF EVENT IS MULTI-KILL
            elif(event['EventName'] == 'Multikill' and event['KillerName'] == IGN):

                # PLAY DOUBLE KILL AUDIO
                if(event['KillStreak'] == 2):
                    return_code = subprocess.call(["afplay", audio_file2])

                # PLAY TRIPLE KILL AUDIO
                elif(event['KillStreak'] == 3):
                    return_code = subprocess.call(["afplay", audio_file3])

                # PLAY QUADRA KILL AUDIO
                else:
                    return_code = subprocess.call(["afplay", audio_file4])
            

        # UPDATE STORED EVENTS
        stored_events = events.copy()

    time.sleep(REFRESH_RATE)


