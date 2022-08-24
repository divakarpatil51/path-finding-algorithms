from priority_queue import PriorityQueue
from helper import get_path, paths, is_valid_pos

"""
A* algorithm: A path-finding algorithm to find shortest path between two given points by using heuristics.

Vocabulary:
1. g-value: distance of current pos from start
2. h-value: estimated distance of current pos from end
3. f-value: g-value + h-value
4. Open List: contains discovered nodes and f_value. Represented by a priority queue
5. Closed list: Contains visited nodes.

Heuristics:
1. Manhattan Heuristics (taxicab heuristics): Used when we are allowed to move only in 4 directions
2. Diagonal Distance: Used when we are allowed to move only in 8 directions
3. Eucledian Distance: Used when we are allowed to move only in 8 directions
"""


def manhattan_heuristic(goal, curr):
    """
    Calculates manhattan distance between current position to goal. Use this if we are allowed to move only in
    4 directions i.e up, right, down, and left.
    """
    x1, y1 = goal
    x2, y2 = curr
    return abs(x2 - x1) + abs(y2 - y1)


def a_star_algo(maze, start, goal):
    g_value = {start: 0}  # This dict acts as closed list
    predecessors = {start_pos: None}  # Tracks the path taken by algorithm.
    pq = PriorityQueue()  # This queue acts a open list
    pq.put(start, 0)

    while not pq.is_empty():
        current_pos = pq.get()
        if current_pos == goal:
            return get_path(predecessors, start_pos, goal)
        # For now considering we can move only in 4 directions.
        for direction in ["up", "right", "down", "left"]:
            x_offset, y_offset = paths.get(direction)
            next_pos = current_pos[0] + x_offset, current_pos[1] + y_offset

            # Check if next position is valid
            if is_valid_pos(maze, next_pos):
                # G_value of next position will always be curr position + weight
                weight = 1  # Weight of the edge. For now considering it as 1.
                next_g = g_value[current_pos] + weight

                # Add node to open list only if it was not visited.
                if next_pos not in g_value or next_g < g_value[next_pos]:
                    g_value[next_pos] = next_g
                    # Calculate h_value between goal and next pos and add it in current g_value to get f_value
                    f_value = next_g + manhattan_heuristic(goal, next_pos)
                    pq.put(item=next_pos, priority=f_value)
                    predecessors[next_pos] = current_pos

    return None


if __name__ == "__main__":
    _maze = [[0] * 3 for _ in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    op = a_star_algo(maze=_maze, start=start_pos, goal=goal_pos)
    print(op)
