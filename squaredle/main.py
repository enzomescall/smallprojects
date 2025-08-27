import time
import os
from datetime import datetime
from typing import List, Tuple, Iterable

from utils import get_parameters_mouse, get_parameters_keyboard
from mouse_mover import select_words
from trie_squaredle import Trie, TrieNode, build_trie_from_file, find_words_on_board

def run_game(WORDS_PATH: str):
    # defaults
    MIN_L = 4
    letter_grid = [
        "asuqevonex",
        "ezritnelui",
        "dtlryukayt",
        "cnalanotri",
        "oiclhcili0",
        "jtutacthbs",
        "xtienpsalt",
        "ettoriugye",
        "sdncsenlec",
        "niistiwhyx",
    ]

    topleft, bottomright, x, MAX_L, _ = get_parameters_mouse(input_grid=False) # type: ignore

    print(f"{datetime.now().strftime('%H:%M:%S')} - Building trie from {WORDS_PATH}")
    
    trie: Trie = build_trie_from_file(WORDS_PATH, min_len=MIN_L,max_len=MAX_L)
    
    print(f"{datetime.now().strftime('%H:%M:%S')} - Tree built, starting the word search")

    words, paths = find_words_on_board(letter_grid, trie, MIN_L, MAX_L)

    print(f"{datetime.now().strftime('%H:%M:%S')} - Found {len(words)} words")

    list_paths = list(paths.values())

    # mouse version
    select_words(topleft, bottomright, x, list_paths)
    print(f"{datetime.now().strftime('%H:%M:%S')} - Finished traversing {len(paths)} paths")


if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    WORDS_PATH = os.path.join(BASE_DIR, "words.txt")

    run_game(WORDS_PATH)
