import os

from dynaconf import Dynaconf, Validator

config_dirname = 'hd2_stratagem_asr'
config_filename = f'{config_dirname}.yaml'
default_config_dir = f"{os.getenv('USERPROFILE', '~')}/{config_dirname}"
default_config_filepath = f"{default_config_dir}/{config_filename}"

validators = [
    Validator('arrows', cast=bool, default=False, apply_default_on_none=True),
    Validator('stratagem_menu_button', default='ctrl', apply_default_on_none=True),
    Validator('stratagem_menu_button_hold', cast=bool, default=True, apply_default_on_none=True),
    Validator('trigger_words', default=None, apply_default_on_none=True),
    Validator('language', cast=str, default='en', apply_default_on_none=True),
    Validator('whisper_api_url', cast=str, default=None, apply_default_on_none=True),
    Validator('stratagem_aliases', default={}, apply_default_on_none=True),
    Validator('debug_keypresses', cast=bool, default=False, apply_default_on_none=True),
    Validator('microphone_device_id', default=None, apply_default_on_none=True),
    Validator('closest_match_cutoff', cast=float, default=0.6, apply_default_on_none=True),
    Validator('phrase_length_limit_seconds', cast=float, default=1.5, apply_default_on_none=True),
    Validator('phrase_energy_threshold', cast=int, default=1200, apply_default_on_none=True),
    Validator('phrase_threshold', cast=float, default=0.3, apply_default_on_none=True),
    Validator('phrase_non_speaking_duration', cast=float, default=0.3, apply_default_on_none=True),
]
defaults = dict(
    arrows=False,
    stratagem_menu_button='ctrl',
    stratagem_menu_button_hold=True,
    trigger_words=None,
    language='en',
    whisper_api_url=None,
    stratagem_aliases={},
    debug_keypresses=False,
    microphone_device_id=None,
    closest_match_cutoff=0.6,
    phrase_length_limit_seconds=1.5,
    phrase_energy_threshold=1200,
    phrase_threshold=0.3,
    phrase_non_speaking_duration=0.3,
)
config = Dynaconf(
    environments=False,
    load_dotenv=False,
    apply_default_on_none=True,
    auto_cast=True,
    lowercase_read=True,
    root_path=default_config_dir,
    yaml_loader='safe_load',
    core_loaders=['YAML'],
    validators=validators,
    defaults=defaults,
    fresh_vars=[
        'trigger_words',
        'stratagem_aliases',
        'debug_keypresses',
    ],
    settings_files=[
        default_config_filepath,
        f"./{config_filename}",
    ]
)
pass
