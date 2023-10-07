#Author         : Zane Chiang
#Summoner Name  : FlSHBONES
# Date          : April 30th, 2022

# IMPORTS

import requests
import json
import time
import subprocess
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))

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
    return None

# JINX AUDIO FILES
audio_file1 = os.path.join(script_dir, "./riot/champ-theme/Jinx/get-jinxed-1.mp3")
audio_file2 = os.path.join(script_dir, "./riot/champ-theme/Jinx/get-jinxed-2.mp3")
audio_file3 = os.path.join(script_dir, "./riot/champ-theme/Jinx/get-jinxed-3.mp3")
audio_file4 = os.path.join(script_dir, "./riot/champ-theme/Jinx/get-jinxed-4.mp3")
audio_file5 = os.path.join(script_dir, "./riot/champ-theme/Jinx/get-jinxed-5.mp3")

query = 'eventdata'
if getattr(sys, 'frozen', False):
    bundle_dir = sys._MEIPASS
else:
    bundle_dir = os.path.dirname(os.path.abspath(__file__))
cert_path = os.path.join(bundle_dir, 'riotgames.pem')
# PARAMETERS
IGN = 'FlSHBONES'       # Summoner Name
REFRESH_RATE = 0.2      # In Game Refresh Rate
HP_REFRESH_RATE = 60    # Holding Pattern Refresh Rate
SINGLE_KILL = False     # Play Audio On Single Kill

# LAUNCH LEAGUE OF LEGENDS
print("Launching League of Legends")
os.system("open /Applications/'League of Legends.app'")

while(True):
    stored_events = {}
    
    try:
        while(True):

            # GET DATA
            response = requests.get(('https://127.0.0.1:2999/liveclientdata/' + query), verify=cert_path)
            events = json.loads(response.text)['Events']

            # IF THERE ARE NEW EVENTS

            if(len(stored_events) != len(events)):

                num_new_events = len(events) - len(stored_events) # Number of new events

                # ITERATES THROUGH NEW EVENTS

                for eventID in range(len(events) - num_new_events, len(events)):

                    event = find_event(events, eventID) # Get Event
                    print(event['EventName'])
                    
                    # IF EVENT IS 'ChampionKill'

                    if(event['EventName'] == 'ChampionKill' and event['KillerName'] == IGN):

                        next_event = find_event(events, eventID + 1) # Search for a next event

                        # IF SINGLE_KILL IS TURNED ON
                        # IF SUBSEQUENT EVENT IS A MULTI-KILL, DON'T PLAY 1ST KILL AUDIO

                        if(SINGLE_KILL and (next_event == None or next_event['EventName'] != 'Multikill')):
                            return_code = subprocess.call(["afplay", audio_file1])
                    
                    # IF EVENT IS 'Multikill'

                    elif(event['EventName'] == 'Multikill' and event['KillerName'] == IGN):

                        # PLAY DOUBLE KILL AUDIO
                        if(event['KillStreak'] == 2):
                            return_code = subprocess.call(["afplay", audio_file2])

                        # PLAY TRIPLE KILL AUDIO
                        elif(event['KillStreak'] == 3):
                            return_code = subprocess.call(["afplay", audio_file3])

                        # PLAY QUADRA KILL AUDIO
                        elif(event['KillStreak'] == 4):
                            return_code = subprocess.call(["afplay", audio_file4])
                        else:
                            return_code = subprocess.call(["afplay", audio_file5])

                    # IF EVENT IS 'EpicMonsterKill'
                    # AND IS STEAL

                    elif(event['EventName'] == 'BaronKill' or event['EventName'] == 'DragonKill' or event['EventName'] == 'HeraldKill'):
                        if(event['Stolen'] == "True" and event['KillerName'] == IGN):
                            return_code = subprocess.call(["afplay", audio_file1])

                return_code = subprocess.call(["afplay", audio_file1])
                # UPDATE STORED EVENTS
                stored_events = events.copy()

            time.sleep(REFRESH_RATE)
    except Exception as e:
        print("No Game In Progress...")
    except KeyboardInterrupt as e:
        print("Program Terminated")
    

    
    time.sleep(HP_REFRESH_RATE)


