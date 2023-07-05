from flask import Flask, render_template, request
import sys
import os
from text2speech import fetchVoiceName, generate_audio
import asyncio
import json




app = Flask(__name__)

@app.route('/')
def entry_point():
    # return 'Hello World!'
    voices = asyncio.run(fetchVoiceName())
    voice_names = []
    for voice in voices:
        voice_names.append(voice["Name"])
   
    return render_template("index.html", voice_names=voice_names)

#this is for handling the post request 
@app.route("/submit", methods=["POST"])
def form_submit():
    if request.method == "POST":
        print(request.form)
        text = request.form["text"]
        voice = request.form["voice"]
        audio = asyncio.run(generate_audio(text,voice))
        return render_template("index.html", audio=audio)


# if __name__ == '__main__':
#     app.run(debug=True, port=8000)