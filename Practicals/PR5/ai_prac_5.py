# -*- coding: utf-8 -*-
import random
import copy

class Node:
    def __init__(self, board, player):
        self.board = board
        self.player = player
        self.children = []

def initialize():
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    return board

def user_move(board):
    x = int(input("Enter row number (0-2): "))
    y = int(input("Enter column number (0-2): "))
    if 0 <= x < 3 and 0 <= y < 3:
        if board[x][y] == 0:
            board[x][y] = 1
            return True
        else:
            print("Spot Occupied Already")
            return False
    else:
        print("Invalid input. Please enter numbers between 0 and 2.")
        return False

def computer_move(board):
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    if board[x][y] == 0:
        board[x][y] = 2
        return True
    else:
        return False

def won(board, ch):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == ch or \
           board[0][i] == board[1][i] == board[2][i] == ch:
            return True
    if board[0][0] == board[1][1] == board[2][2] == ch or \
       board[0][2] == board[1][1] == board[2][0] == ch:
        return True
    return False

def show_board(board):
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print()

def generate_tree(node, player):
    if won(node.board, 1) or won(node.board, 2) or not any(0 in row for row in node.board):
        return

    for i in range(3):
        for j in range(3):
            if node.board[i][j] == 0:
                new_board = copy.deepcopy(node.board)
                new_board[i][j] = player
                child_node = Node(new_board, 3 - player)  # Switch player
                node.children.append(child_node)
                generate_tree(child_node, 3 - player)

def print_tree(node, depth=0):
    print("Depth:", depth)
    show_board(node.board)
    print("Player:", node.player)
    print("Children:", len(node.children))
    print()
    for child in node.children:
        print_tree(child, depth + 1)

def play_game():
    root = Node(initialize(), 1)  # Assume player 1 starts
    generate_tree(root, 1)
    print_tree(root)

play_game()

import copy

class Node:
    def __init__(self, board, player):
        self.board = board
        self.player = player
        self.children = []

def won(board, ch):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == ch or \
           board[0][i] == board[1][i] == board[2][i] == ch:
            return True
    if board[0][0] == board[1][1] == board[2][2] == ch or \
       board[0][2] == board[1][1] == board[2][0] == ch:
        return True
    return False

def draw(board):
    return not any(0 in row for row in board)

def show_board(board):
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print()

def generate_tree(node, player):
    if won(node.board, 1) or won(node.board, 2) or draw(node.board):
        return

    for i in range(3):
        for j in range(3):
            if node.board[i][j] == 0:
                new_board = copy.deepcopy(node.board)
                new_board[i][j] = player
                child_node = Node(new_board, 3 - player)  # Switch player
                node.children.append(child_node)
                generate_tree(child_node, 3 - player)

def print_tree(node, depth=0):
    print("Depth:", depth)
    show_board(node.board)
    print("Player:", node.player)
    print("Children:", len(node.children))
    print()
    for child in node.children:
        print_tree(child, depth + 1)

def generate_from_state(board, player):
    root = Node(board, player)
    generate_tree(root, player)
    print_tree(root)

# Example usage:
board = [
    [1, 1, 0],
    [2, 1, 0],
    [0, 2, 2]
]
player = 1
generate_from_state(board, player)

import copy

class Node:
    def __init__(self, board, player, parent=None):
        self.board = board
        self.player = player
        self.parent = parent
        self.children = []

def won(board, ch):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == ch or \
           board[0][i] == board[1][i] == board[2][i] == ch:
            return True
    if board[0][0] == board[1][1] == board[2][2] == ch or \
       board[0][2] == board[1][1] == board[2][0] == ch:
        return True
    return False

def draw(board):
    return not any(0 in row for row in board)

def show_board(board):
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print()

def generate_tree(node, player):
    if won(node.board, 1) or won(node.board, 2) or draw(node.board):
        return

    for i in range(3):
        for j in range(3):
            if node.board[i][j] == 0:
                new_board = copy.deepcopy(node.board)
                new_board[i][j] = player
                child_node = Node(new_board, 3 - player, parent=node)  # Switch player
                node.children.append(child_node)
                generate_tree(child_node, 3 - player)

def print_tree(node, depth=0):
    print("Depth:", depth)
    show_board(node.board)
    print("Player:", node.player)
    print("Children:", len(node.children))
    print()
    for child in node.children:
        print_tree(child, depth + 1)

def generate_from_state(board, player):
    root = Node(board, player)
    generate_tree(root, player)
    print_tree(root)

# Example usage:
board = [
    [1, 1, 0],
    [2, 1, 0],
    [0, 2, 2]
]
player = 1
generate_from_state(board, player)

import copy

class Node:
    def __init__(self, board, player, parent=None):
        self.board = board
        self.player = player
        self.parent = parent
        self.children = []

def won(board, ch):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == ch or \
           board[0][i] == board[1][i] == board[2][i] == ch:
            return True
    if board[0][0] == board[1][1] == board[2][2] == ch or \
       board[0][2] == board[1][1] == board[2][0] == ch:
        return True
    return False

def draw(board):
    return not any(0 in row for row in board)

def is_terminal(node):
    return won(node.board, 1) or won(node.board, 2) or draw(node.board)

def evaluate(board):
    if won(board, 1):
        return -1
    elif won(board, 2):
        return 1
    else:
        return 0

def generate_tree(node, player):
    if is_terminal(node):
        return evaluate(node.board)

    scores = []
    for i in range(3):
        for j in range(3):
            if node.board[i][j] == 0:
                new_board = copy.deepcopy(node.board)
                new_board[i][j] = player
                child_node = Node(new_board, 3 - player, parent=node)
                node.children.append(child_node)
                score = generate_tree(child_node, 3 - player)
                scores.append(score)

    if player == 1:
        return max(scores)
    else:
        return min(scores)

def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print()

def find_best_move(node, player):
    best_score = -float('inf') if player == 1 else float('inf')
    best_move = None
    for child in node.children:
        score = generate_tree(child, 3 - player)
        if player == 1:
            if score > best_score:
                best_score = score
                best_move = child.board
        else:
            if score < best_score:
                best_score = score
                best_move = child.board
    return best_move

# Example usage:
board = [
    [1, 1, 0],
    [2, 1, 0],
    [0, 2, 2]
]
player = 1

root = Node(board, player)
generate_tree(root, player)
best_move = find_best_move(root, player)
print("Best Move:")
print_board(best_move)

import copy

class Node:
    def __init__(self, board, player, parent=None):
        self.board = board
        self.player = player
        self.parent = parent
        self.children = []
        self.value = None  # Initialize value attribute

def won(board, ch):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == ch or \
           board[0][i] == board[1][i] == board[2][i] == ch:
            return True
    if board[0][0] == board[1][1] == board[2][2] == ch or \
       board[0][2] == board[1][1] == board[2][0] == ch:
        return True
    return False

def draw(board):
    return not any(0 in row for row in board)

def is_terminal(node):
    return won(node.board, 1) or won(node.board, 2) or draw(node.board)

def evaluate(board):
    if won(board, 1):
        return -1, "Win"
    elif won(board, 2):
        return 1, "Loss"
    elif draw(board):  # If the game is a draw
        return 0, "Tie"
    else:
        return None, None

def generate_tree(node, player):
    result, _ = evaluate(node.board)
    if result is not None:  # If the game is won or drawn
        return result

    scores = []
    for i in range(3):
        for j in range(3):
            if node.board[i][j] == 0:
                new_board = copy.deepcopy(node.board)
                new_board[i][j] = player
                child_node = Node(new_board, 3 - player, parent=node)
                node.children.append(child_node)
                score = generate_tree(child_node, 3 - player)
                scores.append(score)

    if player == 1:
        node.value = max(scores) if scores else 0  # Set value to 0 if no possible moves
    else:
        node.value = min(scores) if scores else 0  # Set value to 0 if no possible moves
    return node.value

def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print()

def print_minimax_values(node):
    terminal_value, terminal_state = evaluate(node.board)
    print("Player:", node.player)
    print("Board:")
    print_board(node.board)
    print("Minimax Value:", node.value)
    print("Number of Children:", len(node.children))
    if terminal_value is not None:
        print("Terminal State:", terminal_state)
    print()
    for child in node.children:
        print_minimax_values(child)

# Example usage:
board = [
    [1, 1, 0],
    [2, 1, 0],
    [0, 2, 2]
]
player = 1

root = Node(board, player)
generate_tree(root, player)
print("Minimax Values of all nodes:")
print_minimax_values(root)

import copy

class Node:
    def __init__(self, board, player, parent=None, depth=0):
        self.board = board
        self.player = player
        self.parent = parent
        self.children = []
        self.value = None  # Initialize value attribute
        self.depth = depth  # Assign depth attribute

def won(board, ch):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == ch or \
           board[0][i] == board[1][i] == board[2][i] == ch:
            return True
    if board[0][0] == board[1][1] == board[2][2] == ch or \
       board[0][2] == board[1][1] == board[2][0] == ch:
        return True
    return False

def draw(board):
    return not any(0 in row for row in board)

def is_terminal(node):
    return won(node.board, 1) or won(node.board, 2) or draw(node.board)

def evaluate(board):
    if won(board, 1):
        return -1, "Win"
    elif won(board, 2):
        return 1, "Lose"
    elif draw(board):  # If the game is a draw
        return 0, "Tie"
    else:
        return None, None

def generate_tree(node, player):
    if is_terminal(node):  # If the node is a terminal node
        result, _ = evaluate(node.board)
        return result

    scores = []
    for i in range(3):
        for j in range(3):
            if node.board[i][j] == 0:
                new_board = copy.deepcopy(node.board)
                new_board[i][j] = player
                child_node = Node(new_board, 3 - player, parent=node, depth=node.depth + 1)  # Update depth
                node.children.append(child_node)
                score = generate_tree(child_node, 3 - player)
                scores.append(score)

    if player == 1:
        node.value = max(scores) if scores else 0  # Set value to 0 if no possible moves
    else:
        node.value = min(scores) if scores else 0  # Set value to 0 if no possible moves
    return node.value

def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print()

def print_minimax_values(node):
    terminal_value, terminal_state = evaluate(node.board)
    print("Player:", node.player)
    print("Board:")
    print_board(node.board)
    print("Minimax Value:", node.value if node.value is not None else "None")
    print("Depth:", node.depth)  # Print depth
    print("Number of Children:", len(node.children))  # Print number of children
    if terminal_state is not None:
        print("Terminal State:", terminal_state)
        print("Score:", terminal_value)
    print()
    for child in node.children:
        print_minimax_values(child)

# Example usage:
board = [
    [1, 1, 0],
    [2, 1, 0],
    [0, 2, 2]
]
player = 1

root = Node(board, player)
generate_tree(root, player)
print("Minimax Values of all nodes:")
print_minimax_values(root)

"""##Code"""

import math

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def evaluate(board):

    for i in range(3):

        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 'X':
                return 10
            elif board[i][0] == 'O':
                return -10

        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'X':
                return 10
            elif board[0][i] == 'O':
                return -10

    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] == 'X':
            return 10
        elif board[1][1] == 'O':
            return -10

    return 0

def is_moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False

def minimax(board, depth, is_maximizing):
    score = evaluate(board)


    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best_score = max(best_score, minimax(board, depth + 1, False))
                    board[i][j] = ' '
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best_score = min(best_score, minimax(board, depth + 1, True))
                    board[i][j] = ' '
        return best_score

def find_best_move(board):
    best_score = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_score = minimax(board, 0, False)
                board[i][j] = ' '
                if move_score > best_score:
                    best_score = move_score
                    best_move = (i, j)

    return best_move


initial_board = [
    ['X', 'O', ' '],
    ['X', ' ', 'O'],
    ['O', ' ', ' ']
]

print("Initial Board:")
print_board(initial_board)

current_board = initial_board
while is_moves_left(current_board):
    best_move = find_best_move(current_board)
    current_board[best_move[0]][best_move[1]] = 'X'

    print(f"\nMove: {best_move}")
    print_board(current_board)

    if evaluate(current_board) != 0:
        break

if evaluate(current_board) == 10:
    print("\nAI wins!")
elif evaluate(current_board) == -10:
    print("\nYou win!")
else:
    print("\nIt's a draw!")

