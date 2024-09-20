from enum import Enum
import config


if config.ARROWS:
    class Key(Enum):
        W = 'up'
        S = 'down'
        A = 'left'
        D = 'right'
else:
    class Key(Enum):
        W = 'w'
        S = 's'
        A = 'a'
        D = 'd'


STRATAGEMS: dict[str, list[Key]] = {
    # General
    "reinforce": [Key.W, Key.S, Key.D, Key.A, Key.W],
    "resupply": [Key.S, Key.S, Key.W, Key.D],
    "sos": [Key.W, Key.S, Key.D, Key.W],
    "hellbomb": [Key.S, Key.W, Key.A, Key.S, Key.W, Key.D, Key.S, Key.W],
    "flare": [Key.D, Key.D, Key.A, Key.A],
    "flag": [Key.S, Key.W, Key.S, Key.W],
    "seaf": [Key.D, Key.W, Key.W, Key.S],
    # Patriotic Administration Center
    "machine": [Key.S, Key.A, Key.S, Key.W, Key.D],
    "antimaterial": [Key.S, Key.A, Key.D, Key.W, Key.S],
    "stalwart": [Key.S, Key.A, Key.S, Key.W, Key.W, Key.A],
    "expendable": [Key.S, Key.S, Key.A, Key.W, Key.D],
    "recoilless": [Key.S, Key.A, Key.D, Key.D, Key.A],
    "flamethrower": [Key.S, Key.A, Key.W, Key.S, Key.W],
    "autocannon": [Key.S, Key.A, Key.S, Key.W, Key.W, Key.D],
    "railgun": [Key.S, Key.D, Key.S, Key.W, Key.A, Key.D],
    "spear": [Key.S, Key.S, Key.W, Key.S, Key.S],
    # Orbital Cannons
    "orbital_gatling": [Key.D, Key.S, Key.A, Key.W, Key.W],
    "orbital_airburst": [Key.D, Key.D, Key.D],
    "orbital_120mm": [Key.D, Key.D, Key.S, Key.A, Key.D, Key.S],
    "orbital_380mm": [Key.D, Key.S, Key.W, Key.W, Key.A,Key.S, Key.S],
    "orbital_walking": [Key.D, Key.D, Key.S, Key.A, Key.D, Key.S],
    "orbital_laser": [Key.D, Key.S, Key.W, Key.D, Key.S],
    "orbital_railcannon": [Key.D, Key.W, Key.S, Key.S, Key.D],
    # Hangar
    "eagle_rearm": [Key.W, Key.W, Key.A, Key.W, Key.D],
    "eagle_strafing": [Key.W, Key.D, Key.D],
    "eagle_airstrike": [Key.W, Key.D, Key.S, Key.D],
    "eagle_cluster": [Key.W, Key.D, Key.S, Key.S, Key.D],
    "eagle_napalm": [Key.W, Key.D, Key.S, Key.W],
    "jump_pack": [Key.S, Key.W, Key.W, Key.S, Key.W],
    "eagle_smoke": [Key.W, Key.D, Key.W, Key.S],
    "eagle_110mm": [Key.W, Key.D, Key.W, Key.A],
    "eagle_500kg": [Key.W, Key.D, Key.S, Key.S, Key.S],
    # Bridge
    "orbital_precision": [Key.D, Key.D, Key.W],
    "orbital_gas": [Key.D, Key.D, Key.S, Key.D],
    "orbital_ems": [Key.D, Key.D, Key.A, Key.S],
    "orbital_smoke": [Key.D, Key.D, Key.S, Key.W],
    "hmg_replacement": [Key.W, Key.S, Key.A, Key.D, Key.D, Key.A],
    "shield_relay": [Key.S, Key.W, Key.A, Key.D, Key.A, Key.S],
    "tesla_tower": [Key.S, Key.W, Key.D, Key.W, Key.A, Key.D],
    # Engineering Bay
    "minefield": [Key.S, Key.A, Key.W, Key.D],
    "supply_pack": [Key.S, Key.A, Key.S, Key.W, Key.W, Key.S],
    "grenade_launcher": [Key.S, Key.A, Key.W, Key.A, Key.S],
    "laser_cannon": [Key.S, Key.A, Key.W, Key.A, Key.S],
    "incendiary_mines": [Key.S, Key.A, Key.A, Key.S],
    "guard_dog_rover": [Key.S, Key.A, Key.S, Key.W, Key.A, Key.S, Key.S],
    "ballistic_shield": [Key.S, Key.A, Key.W, Key.W, Key.D],
    "arc_thrower": [Key.S, Key.D, Key.W, Key.A, Key.S],
    "shield_generator": [Key.S, Key.W, Key.A, Key.D, Key.A, Key.D],
    # Robotics Workshop
    "machine_sentry": [Key.S,Key.W, Key.D, Key.S, Key.D, Key.S, Key.W],
    "gatling_sentry": [Key.S, Key.W, Key.D, Key.A],
    "mortar_sentry": [Key.S, Key.W, Key.D, Key.D, Key.S],
    "guard_dog": [Key.S, Key.W, Key.A, Key.W, Key.D, Key.S],
    "autocannon_sentry": [Key.S, Key.W, Key.D, Key.W, Key.A, Key.W],
    "rocket_sentry": [Key.S, Key.W, Key.D, Key.D, Key.A],
    "ems_sentry": [Key.S, Key.S, Key.W, Key.W, Key.A],
}
