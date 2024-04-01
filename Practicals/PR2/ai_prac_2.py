# -*- coding: utf-8 -*-

# To find if solvable or not.

def flatten(matrix):
    return [element for row in matrix for element in row]

def count_inversions(state):
    flattened_state = flatten(state)
    inversions = 0
    for i in range(len(flattened_state)):
        for j in range(i + 1, len(flattened_state)):
            if flattened_state[i] != 0 and flattened_state[j] != 0 and flattened_state[i] > flattened_state[j]:
                inversions += 1
    return inversions

def is_solvable(initial_state, final_state):
    inversions_initial = count_inversions(initial_state)
    inversions_final = count_inversions(final_state)
    return inversions_initial % 2 == inversions_final % 2

from collections import deque

goal = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
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

    while open_list:
        current_state, level = open_list.popleft()

        print(f"Level {level}:")
        for row in current_state:
            print(row)
        print()

        if goal_state(current_state):
            print("Goal state found.")
            for row in current_state:
                print(row)
            print(f"Total levels: {level}")
            return

        explored.add(tuple(map(tuple, current_state)))

        successors = generate(current_state)
        for s in successors:
            if tuple(map(tuple, s)) not in explored and s not in [state for state, _ in open_list]:
                open_list.append((s, level + 1))

    print("No solution found.")

initial_state = [
        [1,2,5],
        [3,4,8],
        [6,7,0]
    ]

if(is_solvable(initial_state,goal)):
    print("It is solvable.\n");
    bfs(initial_state)
else:
    print("It is not solvable.\n");

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

        if goal_state(current_state):
            print("Goal state found.")
            for row in current_state:
                print(row)
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

bfs(initial_state)

