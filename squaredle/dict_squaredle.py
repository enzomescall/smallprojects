# Using a dictionary, finds all possible words in a grid of letters
import time
import pyautogui as py
from datetime import datetime

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def read_text_file(filename):
    filepath = os.path.join(BASE_DIR, filename)
    with open(filepath, "r") as f:
        return f.read().splitlines()

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
    x = int(input())

    grid = []
    for i in range(0, int(x)):
        print("What letters in row " + str(i+1) + "?")
        row = input()

        if len(row) == int(x):
            grid.append(row)
        else:
            print("Error: row length does not match grid size")
            return None

    print("How many letters in the longest word?")
    longest = int(input())


    return topleft, bottomright, x, longest, grid

def optimize_dictionary(letter_grid, word_dictionary):
    return word_dictionary

    # Creating smaller dictionary of words that can be formed from the letters in the grid
    letter_list = []
    for row in letter_grid:
        for letter in row:
            letter_list.append(letter)
    
    letter_list = list(set(letter_list))
    letter_list.sort()

    print("List of letters: ", letter_list, len(letter_list))

    possible_words = []
    for word in word_dictionary:
        possible_words.append(word)
        for letter in word:
            if letter not in letter_list:
                word_dictionary.pop()
                break

    # Sorting possible words by length backwards
    possible_words.sort(key=len, reverse=True)
    print("List of possible words: ", possible_words, len(possible_words))

    # Splitting dictionary into multiple lists based on length of word
    dictionary_dictionary = {}
    for word in possible_words:
        if len(word) not in dictionary_dictionary:
            dictionary_dictionary[len(word)] = []
        dictionary_dictionary[len(word)].append(word)

    print(dictionary_dictionary.keys())

    return dictionary_dictionary

def run_game(topleft, bottomright, x, longest, letter_grid, word_dictionary):
    # Calculating width of each square
    width = (bottomright[0] - topleft[0]) / (int(x)-1)
    # Calculating height of each square
    height = (bottomright[1] - topleft[1]) / (int(x)-1)

    gap = (width + height) / 2

    # Generating grid of square coordinates
    grid = []
    for i in range(x):
        grid.append([])
        for j in range(x):
            grid[i].append((topleft[0] + j*gap, topleft[1] + i*gap))    

    word_list = optimize_dictionary(letter_grid, word_dictionary)

    length = int(input("Minimum length of word to find: "))

    if input("Press y to start: ") != "y":
        print("sorry bozo")
        return
    
    while length < longest + 1:
        paths = find_paths(x, length) 
        print(datetime.now().strftime("%H:%M:%S") + " " + str(len(paths)) + " paths of length " + str(length))

        #word_list = dictionary_dictionary[length]
        for path in paths:
            # Determine what word is formed by this path
            # Example path: [(2, 2), (2, 1), (2, 0)]
            word = ""
            for square in path:
                word += letter_grid[square[0]][square[1]]

            #print(datetime.now().strftime("%H:%M:%S") + " " + word)
            if word in word_list:
                print(datetime.now().strftime("%H:%M:%S") + " " + word + " is a word")
                py.mouseDown(grid[path[0][0]][path[0][1]])
                for i in range(len(path)):
                    py.moveTo(grid[path[i][0]][path[i][1]])
                py.mouseUp()
            # else:n
            
            #     # Sleep for a second to keep from overheating
            #     time.sleep(0.01)

        length += 1

if __name__ == "__main__":
    if input("Enter debug mode (y/n): ") == "y":
        topleft = (556, 403)
        bottomright = (856, 693)
        x = 4
        longest = 8
        letter_grid = ["eclk", "ruud", "abbo", "nlyx"]

        word_dictionary = read_text_file("words.txt")

        run_game(topleft, bottomright, x, longest, letter_grid, word_dictionary)

    topleft, bottomright, x, longest, letter_grid = get_parameters() # type: ignore

    word_dictionary = read_text_file("words.txt")
    run_game(topleft, bottomright, x, longest, letter_grid, word_dictionary)