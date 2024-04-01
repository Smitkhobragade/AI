# -*- coding: utf-8 -*-

def getInvCount(arr):
    inv_count = 0
    empty_value = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count


def isSolvable_8(puzzle) :

    inv_count = getInvCount([j for sub in puzzle for j in sub])

    return (inv_count % 2 == 0)

"""## Using Simple BFS"""

from collections import deque

goal = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

def goal_state(state):
    return state == goal

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate(state):
    successors = []
    empty_i, empty_j = find_zero(state)

    def move(direction):
        nonlocal successors
        new_i, new_j = empty_i + direction[0], empty_j + direction[1]
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row.copy() for row in state]
            new_state[empty_i][empty_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_i][empty_j]
            successors.append(new_state)

    move_up = (-1, 0)
    move_down = (1, 0)
    move_left = (0, -1)
    move_right = (0, 1)

    move(move_up)
    move(move_down)
    move(move_left)
    move(move_right)

    return successors

def bfs(initial_state):
    open_list = deque([(initial_state, 0)])
    explored = set()
    nodes_generated = 0  # Counter for nodes generated

    while open_list:
        current_state, level = open_list.popleft()

        print(f"Level {level}:")
        for row in current_state:
            print(row)
        print()

        if goal_state(current_state):
            print("Goal state found.")
            print(f"Total levels: {level}")
            print(f"Total nodes generated: {nodes_generated}")  # Print total nodes generated
            return

        explored.add(tuple(map(tuple, current_state)))

        successors = generate(current_state)
        nodes_generated += len(successors)  # Increment the counter by the number of successors generated
        for s in successors:
            if tuple(map(tuple, s)) not in explored and s not in [state for state, _ in open_list]:
                open_list.append((s, level + 1))

    print("No solution found.")

initial_state = [
    [0, 2, 5],
    [1, 3, 8],
    [6, 4, 7]
]

if(isSolvable_8(initial_state)):
    print("It is solvable.\n");
    bfs(initial_state)
else:
    print("It is not solvable.\n");

"""##using H1 || Misplaced Tiles"""

from collections import deque

def goal_reached(state, goal):
    return state == goal

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate(state):
    successors = []
    empty_i, empty_j = find_zero(state)

    def move(direction):
        nonlocal successors
        new_i, new_j = empty_i + direction[0], empty_j + direction[1]
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row.copy() for row in state]
            new_state[empty_i][empty_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_i][empty_j]
            successors.append(new_state)

    move_up = (-1, 0)
    move_down = (1, 0)
    move_left = (0, -1)
    move_right = (0, 1)

    move(move_up)
    move(move_down)
    move(move_left)
    move(move_right)

    return successors

def misplaced_tiles(state, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j] and state[i][j] != 0:
                count += 1
    return count

def a_star_h1_8(initial_state):
    goal = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    open_list = [(initial_state, 0, misplaced_tiles(initial_state, goal))]
    explored = set()
    nodes_generated = 0

    while open_list:
        open_list.sort(key=lambda x: x[1] + x[2])  # Sort by f(n) = g(n) + h(n)
        current_state, level, _ = open_list.pop(0)

        print(f"Level {level}:")
        for row in current_state:
            print(row)
        print()

        if goal_reached(current_state, goal):
            print("Goal state found.")
            print(f"Total levels: {level}")
            print(f"Total nodes generated: {nodes_generated}")
            return

        explored.add(tuple(map(tuple, current_state)))

        successors = generate(current_state)
        nodes_generated += len(successors)
        for s in successors:
            if tuple(map(tuple, s)) not in explored:
                open_list.append((s, level + 1, misplaced_tiles(s, goal)))

    print("No solution found.")

initial_state = [
    [0, 2, 5],
    [1, 3, 8],
    [6, 4, 7]
]

if(isSolvable_8(initial_state)):
    print("It is solvable.\n");
    a_star_h1_8(initial_state)
else:
    print("It is not solvable.\n");

"""##USING H2 || Manhattan Distance"""

from collections import deque

def goal_reached(state, goal):
    return state == goal

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate(state):
    successors = []
    empty_i, empty_j = find_zero(state)

    def move(direction):
        nonlocal successors
        new_i, new_j = empty_i + direction[0], empty_j + direction[1]
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row.copy() for row in state]
            new_state[empty_i][empty_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_i][empty_j]
            successors.append(new_state)

    move_up = (-1, 0)
    move_down = (1, 0)
    move_left = (0, -1)
    move_right = (0, 1)

    move(move_up)
    move(move_down)
    move(move_left)
    move(move_right)

    return successors

def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                value = state[i][j]
                goal_row, goal_col = find_position(goal, value)
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance

def find_position(state, value):
    for i in range(3):
        for j in range(3):
            if state[i][j] == value:
                return i, j

def a_star_h2_8(initial_state):
    goal = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    open_list = [(initial_state, 0, manhattan_distance(initial_state, goal))]
    explored = set()
    nodes_generated = 0

    while open_list:
        open_list.sort(key=lambda x: x[1] + x[2])  # Sort by f(n) = g(n) + h(n)
        current_state, level, _ = open_list.pop(0)

        print(f"Level {level}:")
        for row in current_state:
            print(row)
        print()

        if goal_reached(current_state, goal):
            print("Goal state found.")
            print(f"Total levels: {level}")
            print(f"Total nodes generated: {nodes_generated}")
            return

        explored.add(tuple(map(tuple, current_state)))

        successors = generate(current_state)
        nodes_generated += len(successors)
        for s in successors:
            if tuple(map(tuple, s)) not in explored:
                open_list.append((s, level + 1, manhattan_distance(s, goal)))

    print("No solution found.")

initial_state = [
    [0, 2, 5],
    [1, 3, 8],
    [6, 4, 7]
]

if(isSolvable_8(initial_state)):
    print("It is solvable.\n");
    a_star_h2_8(initial_state)
else:
    print("It is not solvable.\n");

"""#### Comparision of A* Algo and BFS

for (8 Puzzle):
- BFS: 530 States
- A*(h1): 25 States
- A*(h2): 22 States

## 15 Puzzle Problem
"""

def getInvCount(arr):
    inv_count = 0
    empty_value = -1
    for i in range(0, 16):
        for j in range(i + 1, 16):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count


def isSolvable(puzzle) :

    inv_count = getInvCount([j for sub in puzzle for j in sub])

    return (inv_count % 2 == 0)

"""##BFS (15 Puzzle)

## Using BFS
"""

from collections import deque

goal = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0]
]

def goal_state(state):
    return state == goal

def find_zero(state):
    for i in range(4):
        for j in range(4):
            if state[i][j] == 0:
                return i, j

def generate(state):
    successors = []
    empty_i, empty_j = find_zero(state)

    def move(direction):
        nonlocal successors
        new_i, new_j = empty_i + direction[0], empty_j + direction[1]
        if 0 <= new_i < 4 and 0 <= new_j < 4:
            new_state = [row.copy() for row in state]
            new_state[empty_i][empty_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_i][empty_j]
            successors.append(new_state)

    move_up = (-1, 0)
    move_down = (1, 0)
    move_left = (0, -1)
    move_right = (0, 1)

    move(move_up)
    move(move_down)
    move(move_left)
    move(move_right)

    return successors

def bfs_15(initial_state):
    open_list = deque([(initial_state, 0)])
    explored = set()
    nodes_generated = 0

    while open_list:
        current_state, level = open_list.popleft()

        if goal_state(current_state):
            print("Goal state found.")
            for row in current_state:
                print(row)
            print(f"Total levels: {level}")
            print(f"Total nodes generated: {nodes_generated}")
            return

        explored.add(tuple(map(tuple, current_state)))

        successors = generate(current_state)
        nodes_generated += len(successors)  # Increment the counter by the number of successors generated
        for s in successors:
            if tuple(map(tuple, s)) not in explored and s not in [state for state, _ in open_list]:
                open_list.append((s, level + 1))

    print("No solution found.")

initial_state = [
    [1, 2, 3, 4],
    [5, 6, 0, 7],
    [9, 10, 11, 8],
    [13, 14, 15, 12]
]

if(isSolvable(initial_state)):
    print("It is solvable.\n");
    bfs_15(initial_state)
else:
    print("It is not solvable.\n");

"""**CASE I : Finding state in finite time (Solvable)**"""

initial_state = [
        [1, 2, 3, 4],
        [5, 6, 0, 7],
        [9, 10, 11, 8],
        [13, 14, 15, 12]
    ]

if(isSolvable(initial_state)):
    print("It is solvable.\n");
    bfs_15(initial_state)
else:
    print("It is not solvable.\n");

"""**CASE II : Finding State in Non Finite Time (Solvable)**"""

initial_state = [
        [5, 1, 2, 3],
        [9, 10, 6, 4],
        [13, 0, 7, 8],
        [14, 15, 11, 12]
    ]

if(isSolvable(initial_state)):
    print("It is solvable.\n");
    bfs_15(initial_state)
else:
    print("It is not solvable.\n");

"""Above Case Runs Infinitely for the input given.

## Using A* algo || H1 (Misplaced Tiles)
"""

from queue import PriorityQueue

goal = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0]
]

def goal_state(state):
    return state == goal

def find_zero(state):
    for i in range(4):
        for j in range(4):
            if state[i][j] == 0:
                return i, j

def generate(state):
    successors = []
    empty_i, empty_j = find_zero(state)

    def move(direction):
        nonlocal successors
        new_i, new_j = empty_i + direction[0], empty_j + direction[1]
        if 0 <= new_i < 4 and 0 <= new_j < 4:
            new_state = [row.copy() for row in state]
            new_state[empty_i][empty_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_i][empty_j]
            successors.append(new_state)

    move_up = (-1, 0)
    move_down = (1, 0)
    move_left = (0, -1)
    move_right = (0, 1)

    move(move_up)
    move(move_down)
    move(move_left)
    move(move_right)

    return successors

def misplaced_tiles(state):
    count = 0
    for i in range(4):
        for j in range(4):
            if state[i][j] != goal[i][j] and state[i][j] != 0:
                count += 1
    return count

def a_star_15_h1(initial_state):
    open_list = PriorityQueue()
    open_list.put((misplaced_tiles(initial_state), 0, initial_state, [initial_state]))
    explored = set()
    nodes_generated = 0

    while not open_list.empty():
        _, depth, current_state, path = open_list.get()

        if goal_state(current_state):
            print("Goal state found at depth:", depth)
            print("Path to reach the goal:")
            for state in path:
                for row in state:
                    print(row)
                print()
            print(f"Total nodes generated: {nodes_generated}")
            return True

        explored.add(tuple(map(tuple, current_state)))

        successors = generate(current_state)
        nodes_generated += len(successors)

        for s in successors:
            if tuple(map(tuple, s)) not in explored:
                open_list.put((misplaced_tiles(s) + depth + 1, depth + 1, s, path + [s]))

    print("No solution found.")
    return False

initial_state = [
    [1, 2, 3, 4],
    [5, 6, 0, 7],
    [9, 10, 11, 8],
    [13, 14, 15, 12]
]

if(isSolvable(initial_state)):
    print("It is solvable.\n");
    a_star_15_h1(initial_state)
else:
    print("It is not solvable.\n");

"""**CASE I : Finding state in finite time (Solvable)**"""

initial_state = [
        [1, 2, 3, 4],
        [5, 6, 0, 7],
        [9, 10, 11, 8],
        [13, 14, 15, 12]
    ]

if(isSolvable(initial_state)):
    print("It is solvable.\n");
    a_star_15_h1(initial_state)
else:
    print("It is not solvable.\n");

"""**CASE II : Finding State in Non Finite Time (Solvable)**"""

initial_state = [
        [5, 1, 2, 3],
        [9, 10, 6, 4],
        [13, 0, 7, 8],
        [14, 15, 11, 12]
    ]

if(isSolvable(initial_state)):
    print("It is solvable.\n");
    a_star_15_h1(initial_state)
else:
    print("It is not solvable.\n");

"""##Using A* Algo || H2 (Manhattan Distance)"""

from queue import PriorityQueue

goal = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0]
]

def goal_state(state):
    return state == goal

def find_zero(state):
    for i in range(4):
        for j in range(4):
            if state[i][j] == 0:
                return i, j

def generate(state):
    successors = []
    empty_i, empty_j = find_zero(state)

    def move(direction):
        nonlocal successors
        new_i, new_j = empty_i + direction[0], empty_j + direction[1]
        if 0 <= new_i < 4 and 0 <= new_j < 4:
            new_state = [row.copy() for row in state]
            new_state[empty_i][empty_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_i][empty_j]
            successors.append(new_state)

    move_up = (-1, 0)
    move_down = (1, 0)
    move_left = (0, -1)
    move_right = (0, 1)

    move(move_up)
    move(move_down)
    move(move_left)
    move(move_right)

    return successors

def manhattan_distance(state):
    distance = 0
    for i in range(4):
        for j in range(4):
            if state[i][j] != 0:
                value = state[i][j]
                goal_row, goal_col = find_position(goal, value)
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance

def find_position(state, value):
    for i in range(4):
        for j in range(4):
            if state[i][j] == value:
                return i, j

def a_star_15_h2(initial_state):
    open_list = PriorityQueue()
    open_list.put((manhattan_distance(initial_state), 0, initial_state, [initial_state]))
    explored = set()
    nodes_generated = 0

    while not open_list.empty():
        _, depth, current_state, path = open_list.get()

        if goal_state(current_state):
            print("Goal state found at depth:", depth)
            print("Path to reach the goal:")
            for state in path:
                for row in state:
                    print(row)
                print()
            print(f"Total nodes generated: {nodes_generated}")
            return True

        explored.add(tuple(map(tuple, current_state)))

        successors = generate(current_state)
        nodes_generated += len(successors)

        for s in successors:
            if tuple(map(tuple, s)) not in explored:
                open_list.put((manhattan_distance(s) + depth + 1, depth + 1, s, path + [s]))

    print("No solution found.")
    return False

initial_state = [
    [1, 2, 3, 4],
    [5, 6, 0, 7],
    [9, 10, 11, 8],
    [13, 14, 15, 12]
]

if(isSolvable(initial_state)):
    print("It is solvable.\n");
    a_star_15_h2(initial_state)
else:
    print("It is not solvable.\n");

initial_state = [
        [5, 1, 2, 3],
        [9, 10, 6, 4],
        [13, 0, 7, 8],
        [14, 15, 11, 12]
    ]

a_star_15_h2(initial_state)

"""**CASE I : Finding state in finite time (Solvable)**"""

initial_state = [
        [1, 2, 3, 4],
        [5, 6, 0, 7],
        [9, 10, 11, 8],
        [13, 14, 15, 12]
    ]

if(isSolvable(initial_state)):
    print("It is solvable.\n");
    a_star_15_h2(initial_state)
else:
    print("It is not solvable.\n");

"""**CASE II : Finding State in Non Finite Time (Solvable)**"""

initial_state = [
        [5, 1, 2, 3],
        [9, 10, 6, 4],
        [13, 0, 7, 8],
        [14, 15, 11, 12]
    ]

if(isSolvable(initial_state)):
    print("It is solvable.\n");
    a_star_15_h2(initial_state)
else:
    print("It is not solvable.\n");



initial_state = [
    [5, 1, 2, 3],
    [9, 6, 7, 4],
    [13, 10, 11, 8],
    [14, 15, 0, 12]
]

if(isSolvable(initial_state)):
    print("It is solvable.\n");
    a_star_15_h2(initial_state)
else:
    print("It is not solvable.\n");

if(isSolvable(initial_state)):
    print("It is solvable.\n");
    a_star_15_h1(initial_state)
else:
    print("It is not solvable.\n");

if(isSolvable(initial_state)):
    print("It is solvable.\n");
    bfs_15(initial_state)
else:
    print("It is not solvable.\n");

"""## Analysis of Nodes Generated

<table width=100%>
  <tr>
    <th></th>
    <th>8 Puzzle</th>
    <th>15 Puzzle Case 1</th>
    <th>15 Puzzle Case 2</th>
    <th>15 Puzzle Case 3</th>
  </tr>
  <tr>
    <td>BFS</td>
    <td>530</td>
    <td>100</td>
    <td>∞</td>
    <td>12998</td>
  </tr>
  <tr>
    <td>A* (H1)</td>
    <td>25</td>
    <td>10</td>
    <td>46</td>
    <td>30</td>
  </tr>
  <tr>
    <td>A* (H2)</td>
    <td>22</td>
    <td>10</td>
    <td>46</td>
    <td>30</td>
  </tr>
</table>

"""

