from flask import Flask, render_template, request
import sys
import os
from text2speech import fetchVoiceName, generate_audio
import asyncio
import json

def get_audio_files():
    audio_files = os.listdir("./static")
    return audio_files


app = Flask(__name__)

@app.route('/')
def entry_point():
    # return 'Hello World!'
    voices = asyncio.run(fetchVoiceName())
    voice_names = []
    for voice in voices:
        voice_names.append(voice["Name"])
   
    return render_template("index.html", voice_names=voice_names,text="",audios=get_audio_files())

#this is for handling the post request 
@app.route("/submit", methods=["POST"])
def form_submit():
    if request.method == "POST":
        print(request.form)
        text = request.form["text"]
        voice = request.form["voice"]
        rate = request.form["rate"]
        pitch = request.form["pitch"]
        audio = asyncio.run(generate_audio(text,voice,rate,pitch))
        
        voices = asyncio.run(fetchVoiceName())
        voice_names = []
        for voice in voices:
            voice_names.append(voice["Name"])
        return render_template("index.html",voice_names=voice_names,text=text,audios=get_audio_files())
    
#this is for deleting the audio file
@app.route("/delete-audio", methods=["POST"])
def audio_delete():
    if request.method == "POST":
        print(request.form)
        audio = request.form["audio"]
        text = request.form["text"]
        
        try:
            os.remove(audio)
            print("File deleted successfully.")
        except FileNotFoundError:
            print(f"File '{audio}' not found.")
        except Exception as e:
            print(f"An error occurred while deleting the file: {e}")
       
        
        voices = asyncio.run(fetchVoiceName())
        voice_names = []
        for voice in voices:
            voice_names.append(voice["Name"])
        return render_template("index.html", voice_names=voice_names,text=text,audios=get_audio_files())


#make sure to comment the below code during  production release
# if __name__ == '__main__':
#     app.run(debug=True, port=8000)

# get_audio_files()