# utilities for board games
import math

def create_board(rows, columns, fill_board = "0"):
  """creates a desired matrix board and fills it with fill_board. By default its '0' returns it"""
  board = []
  for row in range(0, rows):
    row = []
    for column in range(0, columns):
      row.append(fill_board)
    board.append(row)
  return board

def draw_board(board):
  """prints the board to the console"""
  for row in board: # loops through the board rows 
    print("|" ,end="") # draws a vertical line at left edge of board, for each row
    for column in row: # loops through each value in the current row index
      print(" ", column, end= "") # gives some space and draws the value in the column position
    print("  |") # draws a vertical line at the right edge of the board, for each row

    print("| " ,end="") # places a wall to the left of the board
    for column in row: # loops through each value in the current row index
      print(" -", end= " ") # gives some space and draws the value in the column position
    print(" |")

def fill_postion(board, row_postion, column_postion, value):
  "fill the postion given on the board with the value"
  board[row_postion][column_postion] = value

def unfill_postion(board, row_postion, column_postion, value= "0"):
  board[row_postion][column_postion] = value
       
def equals(*postions):
  """Takes in multiple arugments and check if those are all equal. returns boolean value"""
  previous = ""
  matching = False
  for postion in range(0, len(postions)):
    if postion == 0:
      previous = postions[postion]
      continue

    if postions[postion] == previous:
      matching = True
    else:
      return False
  
  return matching
