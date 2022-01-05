#!/usr/bin/env python

"""
DFS: Depth First Search
As long as it is movable, move; else back to the last position, then try.
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


def maze_path(x1, y1, x2, y2):
    stack = [(x1, y1)]

    while len(stack) > 0:
        cur_node = stack[-1]
        # already reach the destination
        if cur_node[0] == x2 and cur_node[1] == y2:
            for p in stack:
                print(p)
            return True

        # down/up/left/right
        for direction in directions:
            next_node = direction(cur_node[0], cur_node[1])
            # the path is accessible
            if maze[next_node[0]][next_node[1]] == 0:
                stack.append(next_node)
                # mark the passed node with 2
                maze[next_node[0]][next_node[1]] = 2
                break

        # all the direction are not accessed
        else:  # for...else: when "break" is triggered, else will not be executed.
            maze[next_node[0]][next_node[1]] = 2
            stack.pop()
    else:
        print('find no way !')
        return False


maze_path(1, 1, 8, 8)


