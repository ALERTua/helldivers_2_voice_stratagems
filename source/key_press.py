import random
import time
import pyautogui
from global_logger import Log
from stratagems import STRATAGEMS
import config

LOG = Log.get_logger()

_gaussian_args = (36, 112, 28, 81)

DEBUG = config.DEBUG_KEYPRESSES


# Gaussian function to generate a random time delay
def gaussian(min_val: int, max_val: int, sig: int, mu: int) -> float:
    while True:
        value: float = random.gauss(mu, sig)
        if min_val <= value <= max_val:
            return value


def key_press(key: str) -> None:
    random_key_press_sleep: float = gaussian(*_gaussian_args)
    if DEBUG:
        LOG.info(f"Would have pressed {key} once with sleep {random_key_press_sleep}")
        return

    pyautogui.keyDown(key)
    time.sleep(random_key_press_sleep / 1000)
    pyautogui.keyUp(key)


def key_hold(key: str):
    random_key_press_sleep: float = gaussian(*_gaussian_args)
    if DEBUG:
        LOG.info(f"Would have held {key} with sleep {random_key_press_sleep}")
        return

    pyautogui.keyDown(key)
    time.sleep(random_key_press_sleep / 1000)


def key_release(key: str) -> None:
    random_key_press_sleep: float = gaussian(*_gaussian_args)
    if DEBUG:
        LOG.info(f"Would have released {key} with sleep {random_key_press_sleep}")
        return
    pyautogui.keyUp(key)
    time.sleep(random_key_press_sleep / 1000)


def press_stratagem(stratagem: str):
    stratagem_sequence = STRATAGEMS.get(stratagem, [])
    if not stratagem_sequence:
        LOG.error(f"No stratagem sequence for {stratagem}")
        return

    LOG.info(f"Pressing {stratagem} sequence {stratagem_sequence}")
    stratagem_menu_button = config.STRATAGEM_MENU_BUTTON
    stratagem_menu_button_hold = config.STRATAGEM_MENU_BUTTON_HOLD
    if stratagem_menu_button:
        if stratagem_menu_button_hold:
            key_hold(stratagem_menu_button)
        else:
            key_press(stratagem_menu_button)

        for stratagem_key in stratagem_sequence:
            # noinspection PyTypeChecker
            key_press(stratagem_key.value)

        if stratagem_menu_button_hold:
            key_release(stratagem_menu_button)
