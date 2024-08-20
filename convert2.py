import json
import requests
import os
#from pydub import AudioSegment
import sys


URL = ""
data = ""


#Converts json to python dictionary
request = requests.get('https://infinite-walker-app.onrender.com/getDay/')
data = request.json()
# with open('/Users/oriramon/Documents/Unreal Projects/FirstProject/Content/Python/example2.json') as json_file:
#     data = json.load(json_file)

# Make Directory for current Day
os.mkdir(f"C:/Users/amir_desktop/Documents/Unreal Projects/BM1/Content/Endpoint/Days/{sys.argv[1]}")
os.mkdir(f"C:/Users/amir_desktop/Documents/Unreal Projects/BM1/Content/Endpoint/Days/{sys.argv[1]}/time")
os.mkdir(f"C:/Users/amir_desktop/Documents/Unreal Projects/BM1/Content/Endpoint/Days/{sys.argv[1]}/sentiment")
os.mkdir(f"C:/Users/amir_desktop/Documents/Unreal Projects/BM1/Content/Endpoint/Days/{sys.argv[1]}/inscription")
os.mkdir(f"C:/Users/amir_desktop/Documents/Unreal Projects/BM1/Content/Endpoint/Days/{sys.argv[1]}/speech_parts0")
os.mkdir(f"C:/Users/amir_desktop/Documents/Unreal Projects/BM1/Content/Endpoint/Days/{sys.argv[1]}/speech_parts0/audio")
os.mkdir(f"C:/Users/amir_desktop/Documents/Unreal Projects/BM1/Content/Endpoint/Days/{sys.argv[1]}/speech_parts0/text")
os.mkdir(f"C:/Users/amir_desktop/Documents/Unreal Projects/BM1/Content/Endpoint/Days/{sys.argv[1]}/speech_parts1")
os.mkdir(f"C:/Users/amir_desktop/Documents/Unreal Projects/BM1/Content/Endpoint/Days/{sys.argv[1]}/speech_parts1/audio")
os.mkdir(f"C:/Users/amir_desktop/Documents/Unreal Projects/BM1/Content/Endpoint/Days/{sys.argv[1]}/speech_parts1/text")
os.mkdir(f"C:/Users/amir_desktop/Documents/Unreal Projects/BM1/Content/Endpoint/Days/{sys.argv[1]}/speech_parts2")
os.mkdir(f"C:/Users/amir_desktop/Documents/Unreal Projects/BM1/Content/Endpoint/Days/{sys.argv[1]}/speech_parts2/audio")
os.mkdir(f"C:/Users/amir_desktop/Documents/Unreal Projects/BM1/Content/Endpoint/Days/{sys.argv[1]}/speech_parts2/text")
os.mkdir(f"C:/Users/amir_desktop/Documents/Unreal Projects/BM1/Content/Endpoint/Days/{sys.argv[1]}/location")

# Get Location.txt
Location = data["location"].split(", ")
f = open(f"C:/Users/amir_desktop/Documents/Unreal Projects/BM1/Content/Endpoint/Days/{sys.argv[1]}/location/city.txt", "w")
f.write(Location[0])
f = open(f"C:/Users/amir_desktop/Documents/Unreal Projects/BM1/Content/Endpoint/Days/{sys.argv[1]}/location/country.txt", "w")
f.write(Location[1])
f.close()

# Get Time Stamp .txt
Time = data["created_at"]
f = open(f"C:/Users/amir_desktop/Documents/Unreal Projects/BM1/Content/Endpoint/Days/{sys.argv[1]}/time/time.txt", "w")
f.write(Time)
f.close()

# Get Time Audio .mp3
time_audio = data["date_shout"]
response = requests.get(time_audio)
open(f"C:/Users/amir_desktop/Documents/Unreal Projects/BM1/Content/Endpoint/Days/{sys.argv[1]}/time/time.mp3", "wb").write(response.content)

# Get Inscription .txt
Time = data["inscription"]
f = open(f"C:/Users/amir_desktop/Documents/Unreal Projects/BM1/Content/Endpoint/Days/{sys.argv[1]}/inscription/inscription.txt", "w")
f.write(Time)
f.close()

# # Get Time Stamp Audio
# URL= data["date_speech_file"]
# response = requests.get(URL)
# open(f"/Users/oriramon/Documents/Unreal Projects/FirstProject/Content/Audio/WavFiles/{sys.argv[1]}/time/audio/time.mp3", "wb").write(response.content)

# Get Speech files
for i in range(3):
    j=1
    
    # Txt
    for sentence in data["speech_parts"][i]["text"]:
        f = open(f"C:/Users/amir_desktop/Documents/Unreal Projects/BM1/Content/Endpoint/Days/{sys.argv[1]}/speech_parts{i}/text/text{j}.txt", "w")
        f.write(sentence)
        f.close()
        j += 1
    
    j=1

    # Audio
    for audio in data["speech_parts"][i]["audio"]:
        response = requests.get(audio)
        open(f"C:/Users/amir_desktop/Documents/Unreal Projects/BM1/Content/Endpoint/Days/{sys.argv[1]}/speech_parts{i}/audio/speech{j}.mp3", "wb").write(response.content)
        # f.write(response.content)
        # f.close()
        j += 1

# Get Sentiment
sentiment = data["sentiment"]
f = open(f"C:/Users/amir_desktop/Documents/Unreal Projects/BM1/Content/Endpoint/Days/{sys.argv[1]}/sentiment/sentiment.txt", "w")
f.write(sentiment)
f.close()
