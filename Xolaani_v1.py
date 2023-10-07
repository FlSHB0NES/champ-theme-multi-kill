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
import threading
from tkinter import Tk, Label, Button, Entry, Text, Scrollbar, END
from functools import partial

script_dir = os.path.dirname(os.path.abspath(__file__))


def print_to_console(self, msg):
    self.console.config(state='normal')
    self.console.insert(END, str(msg) + '\n')
    self.console.config(state='disabled')
    # Automatically scroll to the bottom
    self.console.yview(END)


# METHOD TO PRINT ALL EVENT NAMES OF GIVEN DICT
# @PARAM dict: DICTIONARY TO PRINT
def print_events(dict, safe_print):

    for event in dict:
        safe_print(event['EventName'])

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
HP_REFRESH_RATE = 10    # Holding Pattern Refresh Rate
SINGLE_KILL = False     # Play Audio On Single Kill

# LAUNCH LEAGUE OF LEGENDS
def launch_game():
    print("Launching League of Legends")
    os.system("open /Applications/'League of Legends.app'")

def script_loop(self, stop_event):


    while not stop_event.is_set():
        stored_events = {}
        
        try:
            while not stop_event.is_set():

                # GET DATA
                response = requests.get(('https://127.0.0.1:2999/liveclientdata/' + "playerlist"), verify=cert_path)
                self.safe_print(response)
                response = requests.get(('https://127.0.0.1:2999/liveclientdata/' + query), verify=cert_path)
                events = json.loads(response.text)['Events']

                # IF THERE ARE NEW EVENTS

                if(len(stored_events) != len(events)):

                    num_new_events = len(events) - len(stored_events) # Number of new events

                    # ITERATES THROUGH NEW EVENTS

                    for eventID in range(len(events) - num_new_events, len(events)):

                        event = find_event(events, eventID) # Get Event
                        self.safe_print(event['EventName'])
                        
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

                    # UPDATE STORED EVENTS
                    stored_events = events.copy()

                time.sleep(REFRESH_RATE)
        except Exception as e:
            self.safe_print("No Game In Progress...")
        except KeyboardInterrupt as e:
            self.safe_print("Program Terminated")
        

        
        time.sleep(HP_REFRESH_RATE)


class App:
    def __init__(self, root):
        self.root = root
        self.stop_script_event = threading.Event()
        self.script_thread = None

        self.ign_lbl = Label(root, text="Summoner Name")
        self.ign_entry = Entry(root)
        self.ign_entry.insert(0, IGN)
        self.start_button = Button(root, text="Start", command=self.start_script)
        self.stop_button = Button(root, text="Stop", state="disabled", command=self.stop_script)

        self.ign_lbl.pack()
        self.ign_entry.pack()
        self.start_button.pack()
        self.stop_button.pack()

        self.console = Text(root, wrap='word', height=10, state='disabled')
        self.console_scrollbar = Scrollbar(root, command=self.console.yview)
        self.console['yscrollcommand'] = self.console_scrollbar.set

        self.console.pack(fill='both', expand=True)
        self.console_scrollbar.pack(side='right', fill='y')

        self.safe_print = partial(print_to_console, self)

        

    def start_script(self):
        self.safe_print("Start Script Initiated")
        global IGN
        IGN = self.ign_entry.get()
        launch_game()

        if not self.script_thread or not self.script_thread.is_alive():
            self.stop_script_event.clear()
            self.script_thread = threading.Thread(target=script_loop, args=(self, self.stop_script_event,))
            self.script_thread.start()

            self.start_button.config(state="disabled")
            self.stop_button.config(state="normal")

    def stop_script(self):
        self.safe_print("Stop Script Initiated")
        if self.script_thread and self.script_thread.is_alive():
            self.stop_script_event.set()
            self.script_thread.join()

            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")

if __name__ == "__main__":
    root = Tk()
    root.title("LoL Event Tracker")
    app = App(root)
    root.mainloop()
