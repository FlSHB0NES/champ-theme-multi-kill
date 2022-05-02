import subprocess
audio_file = "./riot/get-jinxed.mp3"

return_code = subprocess.call(["afplay", audio_file])