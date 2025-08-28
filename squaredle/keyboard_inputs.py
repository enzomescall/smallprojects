import time
from datetime import datetime
import pyautogui as py
from typing import List, Dict, Set

def type_words(words: Set[str], interval: float = 0):
    for word in words:
        print(f"{datetime.now().strftime('%H:%M:%S')} - Inputting {word}")
        py.typewrite(word, interval=interval)
        py.press("enter")

"""
Depracated helper functions since we can literally just type out the words and the game will understand
"""

def _board_to_dict(board: List[str]) -> List[List[Dict[str,int]]]:
    board_dict = [[{}]]

    return board_dict

def _keyboard_instruction(key: str, repetitions: int):
    """
    Presses a key and then space certain amount of times
    """
    # press key down
    py.press(key)
    for i in range(repetitions):
        # get pyautogui to press space a certain amount of times 
        py.press(" ")

if __name__ == "__main__":
    print("Get your keyboard in position")
    time.sleep(2)
    type_words(set(["hello", "my", "name","is"]))