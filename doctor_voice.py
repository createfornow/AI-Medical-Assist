import os 
from gtts import gTTS
import elevenlabs
from elevenlabs.client import ElevenLabs
import os
from dotenv import load_dotenv
import platform
import subprocess
from playsound import playsound

load_dotenv()

#Step 1: Setup Text to Speech–TTS–model with Google TTS---------- with autoplay 

def tts_with_gtts(input_text, output_filepath):

    language="en"
    audioObj=gTTS(
        text=input_text,
        lang=language,
        slow=False

    )
    audioObj.save(output_filepath)
    print(f"Audio saved to: {output_filepath}")

    os_name=platform.system()
    try:
        if os_name=="Darvin": #macOS
            subprocess.run(['afplay',output_filepath])
        elif os_name=="Windows": # for playing .wav file
            # subprocess.run(['powershell',"-c",f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])    
            playsound(output_filepath)  # for playing .mp3 file
        elif os_name=="Linux":
             # Ensure 'aplay' or 'mpg123' (for MP3) is installed.
             # 'aplay' is for WAV. For MP3 on Linux, 'mpg123' or 'ffplay' is better.
            subprocess.run(['aplay',output_filepath])
        else:
            raise OSError("Unsupported Operating System")
    except Exception as e:
        print(f"An Error Occured while trying to play the audio: {e}")


# input_text="Hi, what's up this side ravi. This is autoplay testing."
# tts_with_gtts(input_text=input_text, output_filepath="gtts_autoplay_testing.mp3")


#Step2 : Setup Text to Speech–TTS–model with ElevenLabs ------------ with autoplay

ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")
def tts_with_elevenlabs(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.text_to_speech.stream(
        text=input_text,
        voice_id="iLzHtPh0bW6RGWRG0Xo5",
        output_format="mp3_22050_32" ,
        model_id="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    print(f"Audio saved to: {output_filepath}")

    os_name=platform.system()
    try:
        if os_name=="Darvin": #macOS
            subprocess.run(['afplay',output_filepath])
        elif os_name=="Windows": # for playing .wav file
            # subprocess.run(['powershell',"-c",f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])    
            playsound(output_filepath)  # for playing .mp3 file
        elif os_name=="Linux":
             # Ensure 'aplay' or 'mpg123' (for MP3) is installed.
             # 'aplay' is for WAV. For MP3 on Linux, 'mpg123' or 'ffplay' is better.
            subprocess.run(['aplay',output_filepath])
        else:
            raise OSError("Unsupported Operating System")
    except Exception as e:
        print(f"An Error Occured while trying to play the audio: {e}")



# tts_with_elevenlabs(input_text, output_filepath="elevenlabs_autoplay_testing.mp3")
