# Arrows or WASD
ARROWS = True

# the name of the button that opens stratagems menu
STRATAGEM_MENU_BUTTON = 'shift'

# whether this button needs to be held while the stratagem menu is open
STRATAGEM_MENU_BUTTON_HOLD = False

# if filled, triggers only on phrases that start with these trigger words
TRIGGER_WORDS = None
# TRIGGER_WORDS = ['launch', 'change', 'lunch']
# TRIGGER_WORDS = ['go']

# Speech Recognition language
LANGUAGE = 'en'

# https://github.com/ahmetoner/whisper-asr-webservice
# WHISPER = None
WHISPER_API_URL = 'http://192.168.1.3:8131/asr'

# list of aliases for each stratagem name. the names are available at source/stratagems.py
STRATAGEM_ALIASES = {
    'resupply': ['the play', 'supply'],
    'jump_pack': ['jump', 'jump back'],
    'reinforce': ['force', 'rain', 'respawn'],
    'railgun': ['royal', ],
    'machine': ['machine gun', 'machinegun'],
    'hellbomb': ['hell bomb', 'hellbump'],
    'grenade_launcher': ['grenade launcher', 'grenade'],
    'orbital_airburst': ['burst', 'air burst', 'albert', 'birr', 'burr'],
    'orbital_precision': ['precision', 'orbital precision', 'prix', 'decision'],
    'seaf': ['cif', 'thief', 'safe'],
    'orbital_laser': ['laser', ],
    'orbital_railcannon': ['real cannon', 'real canon', 'real calm'],
    'eagle_rearm': ['igil rihar', 'ryarm', 'rear', ],
    'orbital_walking': ['walking', ],
    'orbital_120mm': ['120', ],
    'orbital_380mm': ['380', ],
    'eagle_110mm': ['110', ],
    'eagle_500kg': ['500', ],
    'eagle_smoke': ['smoke', ],
    'orbital_gas': ['god', ],
    'orbital_ems': ['ems', ],
    'hmg_replacement': ['hmg', ],
    'shield_relay': ['show the relay', ],
    'tesla_tower': ['tesla', ],
    'supply_pack': ['so, play back', 'playback', ],
}

# do not send the keypresses, only print
DEBUG_KEYPRESSES = False

# MICROPHONE_DEVICE_ID = None
MICROPHONE_DEVICE_ID = 1

# difflib.get_close_matches cutoff to match for closest stratagem names
CLOSEST_MATCH_CUTOFF = 0.6

PHRASE_LENGTH_LIMIT_SECONDS = 1.5
PHRASE_ENERGY_THRESHOLD = 1200
PHRASE_THRESHOLD = 0.3
PHRASE_NON_SPEAKING_DURATION = 0.3
