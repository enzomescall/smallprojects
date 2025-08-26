import os
from typing import List, Tuple, Set, Dict


class TrieNode:
    __slots__ = ("children", "is_word")
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_word: bool = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True

    def has_prefix(self, prefix: str) -> bool:     
        node = self.root
        for ch in prefix:
            node = node.children.get(ch)
            if node is None:
                return False
        return True

    def has_word(self, word: str) -> bool:
        node = self.root
        for ch in word:
            node = node.children.get(ch)
            if node is None:
                return False
        return node.is_word

def build_trie_from_file(path: str, min_len: int = 1, max_len: int = 1000) -> Trie:
    trie = Trie()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            w = line.strip().lower()
            if not w:
                continue
            if min_len <= len(w) <= max_len:
                trie.insert(w)
    return trie

# goated
_NEIGHBORS = [(-1,-1), (-1,0), (-1,1),
              ( 0,-1),         ( 0,1),
              ( 1,-1), ( 1,0), ( 1,1)]

def find_words_on_board(
    board: List[str],
    trie: Trie,
    min_len: int,
    max_len: int,
    return_paths: bool = True
) -> Tuple[Set[str], Dict[str, List[Tuple[int,int]]]]:
    """
    board: list of equal-length strings, e.g. ["evcr","itet","cprp","esoe"]
    returns:
        words: set of found words (lowercase)
        paths: map word -> one path list of (r,c) positions (if return_paths=True)
    """
    if not board:
        return set(), {}

    rows, cols = len(board), len(board[0])
    grid = [[ch.lower() for ch in row] for row in board]

    # Precompute in-bounds neighbors for each cell
    nbrs = [[] for _ in range(rows * cols)]
    def idx(r, c): return r * cols + c
    for r in range(rows):
        for c in range(cols):
            i = idx(r, c)
            for dr, dc in _NEIGHBORS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    nbrs[i].append(idx(nr, nc))

    found: Set[str] = set()
    paths: Dict[str, List[Tuple[int,int]]] = {}

    visited = [False] * (rows * cols)

    def dfs(i: int, prefix: str, path: List[int]):
        # prefix pruning
        if not trie.has_prefix(prefix):
            return

        # if current prefix is a word in range, record it
        if len(prefix) >= min_len and len(prefix) <= max_len and trie.has_word(prefix):
            if prefix not in found:
                found.add(prefix)
                if return_paths:
                    # store one path; convert to (r,c)
                    rc_path = [(p // cols, p % cols) for p in path]
                    paths[prefix] = rc_path

        if len(prefix) == max_len:
            return  # can't grow further

        # continue DFS
        for j in nbrs[i]:
            if not visited[j]:
                visited[j] = True
                rj, cj = divmod(j, cols)
                dfs(j, prefix + grid[rj][cj], path + [j])
                visited[j] = False

    # Start DFS from every cell
    for r in range(rows):
        for c in range(cols):
            start = idx(r, c)
            visited[start] = True
            dfs(start, grid[r][c], [start])
            visited[start] = False

    return (found, paths if return_paths else {})

# -----------------------
# Example usage
# -----------------------

if __name__ == "__main__":
    board = [
        "EVCR",
        "ITET",
        "CPRP",
        "ESOE",
    ]

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    WORDS_PATH = os.path.join(BASE_DIR, "words.txt")


    MIN_L, MAX_L = 3, 8
    trie = build_trie_from_file(WORDS_PATH, min_len=MIN_L, max_len=MAX_L)
    words, paths = find_words_on_board(board, trie, MIN_L, MAX_L, return_paths=True)

    # show a few results
    print(f"found {len(words)} words")
    for w in sorted(list(words))[:20]:
        print(w, "->", paths[w])
