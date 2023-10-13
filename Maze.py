# Function to find all paths in the maze.
def find_all_paths(maze):
    def is_valid(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] in ['0', 'G']

    def get_neighbors(x, y):
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        return [(nx, ny) for nx, ny in neighbors if is_valid(nx, ny)]

    def find_paths_helper(x, y, path):
        if (x, y) == goal:
            all_paths.append(path)
            return

        for (nx, ny) in get_neighbors(x, y):
            if (nx, ny) not in visited:
                visited.add((nx, ny))  # Mark the neighbor as visited immediately.
                find_paths_helper(nx, ny, path + [(nx, ny)])
                visited.remove((nx, ny))  # Backtrack

    start = None
    goal = None

    # Find the start and goal positions in the maze.
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                start = (i, j)
            elif maze[i][j] == "G":
                goal = (i, j)

    if start is None or goal is None:
        return "Start or goal not found in the maze."

    visited = set()
    visited.add(start)  # Mark the start position as visited.
    all_paths = []

    # Find all paths using depth-first search.
    find_paths_helper(start[0], start[1], [start])

    return all_paths

# Function to find the shortest path among all paths.
def find_shortest_path(maze):
    all_paths = find_all_paths(maze)

    if not all_paths:
        return "No path found."

    # Find the shortest path by selecting the one with the minimum length.
    shortest_path = min(all_paths, key=len)
    return shortest_path

# Function to print the maze grid.
def print_maze(maze):
    for row in maze:
        print(' '.join(row))

# The maze represented as a 2D grid.
maze = [
    ["S", "1", "0", "0", "0", "0", "0", "1", "0"],
    ["0", "1", "0", "1", "1", "1", "0", "1", "0"],
    ["0", "1", "0", "1", "G", "0", "0", "1", "0"],
    ["0", "1", "0", "1", "1", "1", "0", "1", "0"],
    ["0", "1", "0", "1", "0", "0", "0", "0", "0"],
    ["0", "1", "0", "1", "1", "1", "1", "1", "0"],
    ["0", "0", "0", "0", "0", "1", "0", "0", "0"],
    ["0", "1", "0", "1", "1", "1", "1", "1", "0"],
    ["0", "1", "0", "0", "0", "0", "0", "0", "0"]
]

# Find all paths and the shortest path in the maze.
all_paths = find_all_paths(maze)
shortest_path = find_shortest_path(maze)

# Print all paths and the shortest path.
print("All Paths:")
for path in all_paths:
    print(path)

print("\nShortest Path:")
if isinstance(shortest_path, list):
    # Mark the shortest path with 'X' in the maze grid.
    for x, y in shortest_path:
        maze[x][y] = 'X'
    print_maze(maze)
else:
    print(shortest_path)
