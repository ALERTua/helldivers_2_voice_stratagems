import os
import threading

from global_logger import Log

LOG = Log.get_logger()


def tts_ps(text, volume=50):
    cmd = (f'powershell.exe -Command "'
           f' Add-Type -AssemblyName System.speech;'
           f' $tts = New-Object System.Speech.Synthesis.SpeechSynthesizer;'
           f' $tts.Volume = {volume};'
           f' $tts.Speak(\'{text}\');'
           f'"')
    return os.system(cmd)


def tts_ps_background(text, volume=50):
    # Run the tts_ps function in a separate thread
    thread = threading.Thread(target=tts_ps, args=(text, volume))
    thread.start()


# def tts_pytts(text, volume=0.7, rate=150):
#     import pyttsx3
#     # convert volume percents to 0.0-1.0
#     if volume > 100:
#         volume = volume / 100
#
#     engine = pyttsx3.init()
#     engine.setProperty('rate', rate)
#     engine.setProperty('volume', volume)  # setting up volume level  between 0 and 1
#
#     voices = engine.getProperty('voices')  # getting details of current voice
#     # noinspection PyUnresolvedReferences
#     engine.setProperty('voice', voices[0].id)  # changing index, changes voices. 1 for female
#
#     engine.say(text)
#     engine.runAndWait()


def tts(text, volume=50):
    LOG.info(f"TTS: {text}")
    text = text.replace('_', ' ')
    return tts_ps_background(text=text, volume=volume)


if __name__ == '__main__':
    print(1)
    tts_ps_background('text')
    print(2)
