import asyncio
from msspeech import MSSpeech
import uuid
from datetime import datetime




async def fetchVoiceName():
     mss = MSSpeech()
     voices = await mss.get_voices_list()
     return voices
     


    
async def generate_audio(txt,voice,rate,pitch):
   
     content = txt
     mss = MSSpeech()
     
     await mss.set_voice(voice)
     
     print(rate)
           
     await mss.set_rate(rate)
     await mss.set_pitch(pitch)
     await mss.set_volume(1)
     
     now = datetime.now()
     fileName = str(now).replace(" ","-")
     fileName = str(uuid.uuid1())

     await mss.synthesize(content.strip(), f"./static/{fileName}.mp3")
     
     return f"./static/{fileName}.mp3"
        
# # generate_audio()

# asyncio.run(generate_audio())