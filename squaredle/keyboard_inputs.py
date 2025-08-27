import pyautogui as py
from typing import List, Dict, Tuple

# given grid and path, type it out

# given coords, find input sequence
# -> turn the board into List[List[Dict[char, int]]]
# -> Array of dicts, storing the character and which iteration it is

def _board_to_dict(board: List[str]) -> List[List[Dict[str,int]]]:
    board_dict = [[{}]]

    return board_dict

def _keyboard_instruction(instruction: Dict[str, int]):
    key = next(iter(instruction)) # gets the first key
    presses = instruction[key] + 1 # key ocorrunces are indexed at 0
    for i in range(presses):
        # get pyautogui to press the keyboard this many times


def type_words(board: List[str], paths: List[List[Tuple[int,int]]]):
    board_dict = _board_to_dict(board)
    
    for path in paths:
        # Path is a List[Tuple[int,int]]
        # aka list of board coordinates
        for step in path:
            x,y = step
            instruction = board_dict[x][y]
            _keyboard_instruction(instruction)

    return

if __name__ == "__main__":
    print("test")