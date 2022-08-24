from queue_custom import Queue
from helper import get_path, paths, is_valid_pos


def bfs(maze, start, goal):
    # Use queue as a data structure
    queue = Queue()
    visited = {start: None}
    queue.enqueue(start)

    while not queue.is_empty():
        curr = queue.dequeue()
        if curr == goal:
            return get_path(visited, start, goal)

        for direction in paths.keys():
            row_offset, col_offset = paths[direction]
            neighbour = curr[0] + row_offset, curr[1] + col_offset
            if is_valid_pos(maze, neighbour) and neighbour not in visited:
                queue.enqueue(neighbour)
                visited[neighbour] = curr

    return None


if __name__ == "__main__":
    _maze = [[0] * 3 for _ in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    op = bfs(_maze, start_pos, goal_pos)
    print(op)
