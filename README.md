# Xolaani
## Description:
Xolaani is a unique program leveraging the powerful Riot APIs to enhance your League of Legends gaming experience. With real-time in-game event tracking, Xolaani plays corresponding segments of your champion's theme song when multi-kills are achieved!

Demo Link: https://youtu.be/L067Ug5cvcA
## Dependancies:
```
<pip install requests>
```
```
<pip install numpy>
```
```
<pip install opencv-python>
```
```
<pip install pyautogui>
```

## Set-Up

go into the main.py file and set the following values:
```
IGN = '[your summoner name here]'
REFRESH_RATE = '[recommended 0.2]'
PLAY_SINGLE = [True/False]
```

## Run
1. Run Program
```
python3 Xolaani.py
```
2. Start League Game

## Update dist
```
pyinstaller --onefile \
--add-data 'riotgames.pem:.' \
--add-data './riot/champ-theme/Jinx/Jinx-1.mp3:./riot/champ-theme/Jinx' \
--add-data './riot/champ-theme/Jinx/Jinx-2.mp3:./riot/champ-theme/Jinx' \
--add-data './riot/champ-theme/Jinx/Jinx-3.mp3:./riot/champ-theme/Jinx' \
--add-data './riot/champ-theme/Jinx/Jinx-4.mp3:./riot/champ-theme/Jinx' \
--add-data './riot/champ-theme/Jinx/Jinx-5.mp3:./riot/champ-theme/Jinx' \
--add-data './riot/champ-theme/KaiSa/KaiSa-2.mp3:./riot/champ-theme/KaiSa' \
--add-data './riot/champ-theme/KaiSa/KaiSa-3.mp3:./riot/champ-theme/KaiSa' \
--add-data './riot/champ-theme/KaiSa/KaiSa-4.mp3:./riot/champ-theme/KaiSa' \
--add-data './riot/champ-theme/KaiSa/KaiSa-5.mp3:./riot/champ-theme/KaiSa' \
--add-data './riot/champ-theme/Star-Guardian.mp3:./riot/champ-theme' \
Xolaani.py
```
