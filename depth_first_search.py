from stack import Stack
from helper import get_path, paths, is_valid_pos


def dfs(maze, start, goal):
    stack = Stack()
    stack.push(start)
    visited = {start: None}
    while not stack.is_empty():
        curr = stack.pop()
        if curr == goal:
            return get_path(visited, start, goal)
        for direction in paths.keys():
            row_offset, col_offset = paths[direction]
            neighbour = curr[0] + row_offset, curr[1] + col_offset
            if is_valid_pos(maze, neighbour) and neighbour not in visited:
                stack.push(neighbour)
                visited[neighbour] = curr

    return None


if __name__ == '__main__':
    _maze = [[0] * 3 for _ in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(_maze, start_pos, goal_pos)
    print(result)
