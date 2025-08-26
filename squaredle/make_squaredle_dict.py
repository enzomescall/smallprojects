# Read in TWL06.txt file, removing all words under 4 letters, sorting by length

def read_file():
    with open("TWL06.txt", "r") as f:
        words = f.read().splitlines()
    words = [word for word in words if len(word) >= 4]
    words.sort()
    words.sort(key=len, reverse=True)
    return words

# Write words to file, one per line
def write_file(words):
    with open("words.txt", "w") as f:
        for word in words:
            f.write(word.lower() + "\n")

if __name__ == "__main__":
    words = read_file()
    write_file(words)