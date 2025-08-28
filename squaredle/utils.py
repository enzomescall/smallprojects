import pyautogui as py
import time
from typing import List, Tuple

def _input_grid(grid_width: int) -> List[str]:
    grid: List[str] = []


    for i in range(0, grid_width):
        print("What letters in row " + str(i+1) + "?")
        row = input()

        if len(row) == grid_width:
            grid.append(row)
        else:
            print("Error: row length does not match grid size")
            return None # type: ignore
        
    return grid

def get_parameters_mouse():
    py.FAILSAFE = True

    print("in 2 seconds place mouse on top left square") 
    time.sleep(2)
    topleft = py.position()

    print("in 2 seconds place mouse on bottom right square")
    time.sleep(2)
    bottomright = py.position()

    return topleft, bottomright

def get_grid(input_grid: bool = True):
    print("How wide is the square?")
    x = int(input())

    print("How many letters in the longest word?")
    longest: int = int(input())

    grid: List[str] = []

    if input_grid:
        return x, longest, _input_grid(x)

    return x, longest, []