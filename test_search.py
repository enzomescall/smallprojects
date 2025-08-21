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

def print_paths(paths):
    for i, path in enumerate(paths, start=1):
        print(f"Path {i}: {path}")

gridsize = 4

for length in range(4, 11):
    paths = find_paths(gridsize, length)
    print(len(paths), "paths of length", length)    

print_paths(find_paths(3, 3))