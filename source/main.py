import difflib
import time
import requests
from global_logger import Log
import io
import speech_recognition as sr
import tools
import config
from source.key_press import press_stratagem
from source.stratagems import STRATAGEMS

LOG = Log.get_logger(level=Log.Levels.DEBUG)

mics = sr.Microphone.list_working_microphones()
mic = sr.Microphone(config.MICROPHONE_DEVIDE_ID)
recognizer = sr.Recognizer()
_LOOP = None


def command_to_stratagem(command):
    if not command:
        return

    for stratagem in STRATAGEMS.keys():
        stratagem_words = [stratagem, stratagem.replace('_', ' ')]
        if any([_ for _ in stratagem_words if _.lower() in command.lower()]):
            LOG.info(f"Found direct stratagem {stratagem}")
            return stratagem

    for stratagem, alias_list in config.STRATAGEM_ALIASES.items():
        if any([_ for _ in alias_list if _.lower() in command.lower()]):
            LOG.info(f"Found alias for stratagem {stratagem}")
            return stratagem

    matches = difflib.get_close_matches(command, STRATAGEMS.keys(), 1, config.CLOSEST_MATCH_CUTOFF)
    if matches:
        match = matches[0]
        LOG.info(f"Found closest match for {command}: {match}")
        return match


def audio_to_command(audio):
    LOG.info(f"Transcribing")
    command = None
    if whisper_url := config.WHISPER:
        LOG.info(f"Sending audio to Whisper API @ {whisper_url}")
        audio_bytes = io.BytesIO(audio.get_wav_data())
        url = whisper_url
        audio_file = {'audio_file': ('recorded_audio.wav', audio_bytes, 'audio/wav')}
        params = {
            "task": "transcribe",
            "language": "en",
        }
        response = requests.post(url, files=audio_file, params=params)
        # LOG.info(f"response code: {response.status_code}")
        if response.status_code == 200:
            command = response.text.replace('.', '')
            LOG.info(f"Whisper API responded with: {command}")
        else:
            LOG.warning(f"Whisper API returned wrong response: {response.status_code} {response.reason}")

    if command is None:
        LOG.info(f"Sending audio to Google Translate")
        # noinspection PyUnresolvedReferences
        command = recognizer.recognize_google(audio, show_all=False)
        LOG.info(f"Google Translate responded with: {command}")
    return command


def cb(recognizer_: sr.Recognizer, audiodata: sr.AudioData):
    if not audiodata:
        return

    LOG.info('Processing...')
    command = audio_to_command(audiodata)
    if not command:
        return

    LOG.info(f"Got command: {command}")
    command = command.lower()
    if config.TRIGGER_WORDS:
        if any([_ for _ in config.TRIGGER_WORDS if command.startswith(_)]):
            command = " ".join(command.split(' ')[1:])

    command = command.replace('.', '').strip()
    if command == 'exit':
        LOG.info(f"Exiting")
        exit(0)
    elif 'google' in command:
        return

    command = command_to_stratagem(command)
    if not command:
        return

    LOG.info(f"listen_loop got command: {command}")
    press_stratagem(command)
    tools.tts(f"Launching {command}")


if __name__ == '__main__':
    LOG.info(f"Listen Loop Starts")
    recognizer.energy_threshold = config.PHRASE_ENERGY_THRESHOLD
    recognizer.phrase_threshold = config.PHRASE_THRESHOLD
    recognizer.non_speaking_duration = config.PHRASE_NON_SPEAKING_DURATION
    recognizer.listen_in_background(mic, cb, phrase_time_limit=config.PHRASE_LENGTH_LIMIT_SECONDS)
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        exit(0)
