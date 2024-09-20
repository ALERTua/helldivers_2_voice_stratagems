# arrows or WASD
ARROWS = True

STRATAGEM_MENU_BUTTON = 'shift'
STRATAGEM_MENU_BUTTON_HOLD = False

# TRIGGER_WORDS = ['launch', 'change', 'lunch']
TRIGGER_WORDS = ['go']

# WHISPER = None
WHISPER = 'http://192.168.1.3:8131/asr'

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
    'supply_pack': ['so, play back', ],
}

# do not press, only print
DEBUG_KEYPRESSES = True

# MICROPHONE_DEVIDE_ID = None
MICROPHONE_DEVIDE_ID = 31

CLOSEST_MATCH_CUTOFF = 0.6

PHRASE_LENGTH_LIMIT_SECONDS = 1.5
PHRASE_ENERGY_THRESHOLD = 1200
PHRASE_THRESHOLD = 0.3
PHRASE_NON_SPEAKING_DURATION = 0.3
