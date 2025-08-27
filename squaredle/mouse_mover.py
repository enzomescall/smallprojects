import time
import pyautogui as py
from typing import List, Tuple, Iterable, Dict


py.FAILSAFE = True          
py.PAUSE = 0.02

def _grid_centers(
    topleft: Tuple[int, int],
    bottomright: Tuple[int, int],
    x: int # number of letters per row
) -> List[List[Tuple[int, int]]]:
    """
    Creates the coordinate grid for the squardle squares
    """
    tlx, tly = topleft
    brx, bry = bottomright
    if x <= 1:
        raise ValueError("x must be >= 2")

    step_x = (brx - tlx) / (x - 1)
    step_y = (bry - tly) / (x - 1)

    grid = []
    for i in range(x):
        row = []
        for j in range(x):
            cx = int(round(tlx + j * step_x))
            cy = int(round(tly + i * step_y))
            row.append((cx, cy))
        grid.append(row)
    return grid

def _grid_path_to_coords(
    coord_grid: List[List[Tuple[int, int]]],
    path: List[Tuple[int, int]]
) -> List[Tuple[int, int]]:
    """
    Translates the squardle path on a grid to display coordinates
    """
    return [coord_grid[s[0]][s[1]] for s in path]
    
    path_coords = []
    
    for step in path:
        grid_x = step[0]
        grid_y = step[1]

        coords = coord_grid[grid_x][grid_y]

        path_coords.append(coords)

    return path_coords

def _move_mouse_path(
    path_coords: List[Tuple[int, int]],
    hold_button: str = "left",
    per_step_duration: float = 0.101,
):
    """
    Given a path of coordinates, drags the mouse along that path
    """
    if not path_coords:
        return

    # Move to start, press, drag through, release
    sx, sy = path_coords[0]
    py.moveTo(sx, sy, duration=0.05)
    py.mouseDown(button=hold_button)
    try:
        for x, y in path_coords[1:]:
            py.moveTo(x, y, duration=per_step_duration)
    finally:
        py.mouseUp(button=hold_button)

def select_words(
    topleft: Tuple[int, int],
    bottomright: Tuple[int, int],
    letter_per_row: int,
    paths: List[List[Tuple[int,int]]],
    hold_button: str = "left",
    per_step_duration: float = 0.101,
):
    """
    just puts all the functions together
    input: output of parameters + list of paths to take
    output: mouse movement
    """
    coords_grid = _grid_centers(topleft, bottomright, letter_per_row)
    for path in paths:
        path_coords = _grid_path_to_coords(coords_grid, path)
        _move_mouse_path(path_coords, hold_button, per_step_duration)

if __name__ == "__main__":
    # we gotta test these out
    topleft = (598, 368)
    bottomright = (882, 94)
    x = 4

    from utils import get_parameters_mouse
    topleft, bottomright, x, longest, grid = get_parameters_mouse() # type: ignore
    
    grid = _grid_centers(topleft, bottomright, x)
    print(f"grid: {grid}")

    test_path: List[Tuple[int, int]] = [(0,0),(1,1),(2,2),(2,3)]

    test_path_coords = _grid_path_to_coords(grid, test_path)
    print(f"path: {test_path_coords}")

    print("testing big function")

    select_words(topleft, bottomright, 4, [test_path])