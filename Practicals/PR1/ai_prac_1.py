import random

board = []
def initialise():
  board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
  ]
  print("Intialised")
  return board

board = initialise()
board

def usermove():
  x = int(input())
  y = int(input())
  if(board[x][y] == 0):
    board[x][y] = 1
  else:
    print("Spot Occupied Already")
    usermove()

usermove()
board

board = initialise()
board

def computermove():
  x = random.randint(0, 2)
  y = random.randint(0, 2)
  if(board[x][y] == 0):
    board[x][y] = 2
    print("Computer Played")
  else:
    computermove()

computermove()
board

def won(ch):
  if(board[0][0]==board[0][1] and board[0][1]==board[0][2] and ch==board[0][0]):
    return True
  if(board[1][0]==board[1][1] and board[1][1]==board[1][2] and ch==board[1][0]):
    return True
  if(board[2][0]==board[2][1] and board[2][1]==board[2][2] and ch==board[2][0]):
    return True
  if(board[0][0]==board[1][0] and board[1][0]==board[2][0] and ch==board[0][0]):
    return True
  if(board[0][1]==board[1][1] and board[1][1]==board[2][1] and ch==board[0][1]):
    return True
  if(board[0][2]==board[1][2] and board[1][2]==board[2][2] and ch==board[0][2]):
    return True
  if(board[0][0]==board[1][1] and board[1][1]==board[2][2] and ch==board[0][0]):
    return True
  if(board[0][2]==board[1][1] and board[1][1]==board[2][0] and ch==board[0][2]):
    return True

  return False

def showmat():
  for i in board:
    for j in i:
      print(j, end=" ")
    print()

  print()

def playgame():
  # board = initialise()
  for i in range(0,8):
    if(i%2 == 0):
      usermove()
      showmat()
      if(won(1)):
        print("User Won")
        return
    else:
      computermove()
      showmat()
      if(won(2)):
        print("Computer Won")
        return

  print("Tie Between Players")

showmat()

board = initialise()
playgame()

board = initialise()
playgame()

board = initialise()
playgame()

import time
def computermove1():
  x = random.randint(0, 2)
  y = random.randint(0, 2)
  if(board[x][y] == 0):
    board[x][y] = 1
    print("Computer1 Played")
  else:
    computermove1()

def computermove2():
  x = random.randint(0, 2)
  y = random.randint(0, 2)
  if(board[x][y] == 0):
    board[x][y] = 2
    print("Computer2 Played")
  else:
    computermove2()


def playgame():
  # board = initialise()
  for i in range(0,9):
    if(i%2 == 0):
      time.sleep(1)
      computermove1()
      showmat()
      if(won(1)):
        print("Computer 1 Won")
        return
    else:
      time.sleep(1)
      computermove2()
      showmat()
      if(won(2)):
        print("Computer 2 Won")
        return

  print("Tie Between Players")

board = initialise()
playgame()

