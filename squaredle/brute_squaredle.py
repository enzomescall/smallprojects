# Brute forcing Squardle
import time
import pyautogui as py

def find_paths(gridsize, length):
    def is_valid_move(x, y):
        return 0 <= x < gridsize and 0 <= y < gridsize

    def find_paths_recursive(x, y, path):
        if len(path) == length:
            paths.append(path[:])
            return

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  # Skip the current square
                new_x, new_y = x + dx, y + dy
                if is_valid_move(new_x, new_y) and (new_x, new_y) not in path:
                    path.append((new_x, new_y))
                    find_paths_recursive(new_x, new_y, path)
                    path.pop()

    paths = []
    for i in range(gridsize):
        for j in range(gridsize):
            find_paths_recursive(i, j, [(i, j)])

    return paths

def get_parameters():
    py.FAILSAFE = True

    print("in 2 seconds place mouse on top left square") 
    time.sleep(2)
    topleft = py.position()

    print("in 2 seconds place mouse on bottom right square")
    time.sleep(2)
    bottomright = py.position()

    print("How wide is the square?")
    x = input()

    print("How many letters in the longest word?")
    longest = int(input())

    return topleft, bottomright, x, longest

def run_game(topleft, bottomright, x, longest):
    # Calculating width of each square
    width = (bottomright[0] - topleft[0]) / (int(x)-1)
    # Calculating height of each square
    height = (bottomright[1] - topleft[1]) / (int(x)-1)

    gap = (width + height) / 2

    # Generating grid of square coordinates
    grid = []
    for i in range(int(x)):
        grid.append([])
        for j in range(int(x)):
            grid[i].append((topleft[0] + j*gap, topleft[1] + i*gap))    

    length = 4
    while length < longest + 1:
        paths = find_paths(int(x), length)      

        for path in paths:
            py.mouseDown(grid[path[0][0]][path[0][1]])
            for i in range(len(path)):
                py.moveTo(grid[path[i][0]][path[i][1]])
            py.mouseUp()

        length += 1

if __name__ == "__main__":
    topleft, bottomright, x, longest = get_parameters()

    if input("Press y to start: ") == "y":
        run_game(topleft, bottomright, x, longest)