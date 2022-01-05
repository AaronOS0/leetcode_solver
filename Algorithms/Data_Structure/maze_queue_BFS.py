#!/usr/bin/env python
from collections import deque


"""
BFS: Breadth First Search
Every time, go every accessible path in the same time; when one of the path reach the destination, return the path.
Use queue to store every latest node of each path
Use a list[(tuple)...] to store the position of each step, at last we can traverse back to find the real path. 
"""


maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

directions = [
    lambda x, y: (x + 1, y),
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y - 1),
    lambda x, y: (x, y + 1),
]


def print_path(path):
    cur_node = path[-1]

    real_path = []
    while cur_node[2] != -1:
        real_path.append(cur_node[0:2])
        cur_node = path[cur_node[2]]

    # add the start point
    real_path.append(cur_node[0:2])
    real_path.reverse()
    print(real_path)


def maze_path(x1, y1, x2, y2):
    queue = deque()
    # (x, y, position), mark the fist position as -1
    queue.append((x1, y1, -1))
    path = []

    while len(queue) > 0:
        cur_node = queue.pop()
        path.append(cur_node)

        # reach to the destination
        if cur_node[0] == x2 and cur_node[1] == y2:
            print_path(path)
            return True

        for direction in directions:
            next_node = direction(cur_node[0], cur_node[1])
            if maze[next_node[0]][next_node[1]] == 0:
                queue.append((next_node[0], next_node[1], len(path) - 1))
                # mark as passed node
                maze[next_node[0]][next_node[1]] = 2
    else:
        print("find no way !")
        return False


maze_path(1, 1, 8, 8)
