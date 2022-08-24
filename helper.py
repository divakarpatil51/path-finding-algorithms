paths = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0),
}


def is_valid_pos(maze, pos):
    i, j = pos
    rows_count = len(maze)
    cols_count = len(maze[0])
    return 0 <= i < rows_count and 0 <= j < cols_count and maze[i][j] != "*"


def get_path(visited, start, goal):
    curr = goal
    path = []
    while curr != start:
        path.append(curr)
        curr = visited[curr]
    path.append(curr)
    path.reverse()
    return path

