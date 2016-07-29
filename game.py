turn = 1
board = [
              "_", "_", "_",
              "_", "_", "_",
              "_", "_", "_"
            ]

# I am going to want to change these player1 and 2 to slack usernames.
# pieces = {
#   "player1": "X",
#   "player2": "O",
# }
def players_turn(turn, pieces):
  if turn % 2 == 0:
    return pieces["player1"]
  else:
    return pieces["player2"]

def draw_board():
  print(" %s | %s | %s " % (board[0],board[1],board[2]))
  print(" %s | %s | %s " % (board[3],board[4],board[5]))
  print(" %s | %s | %s " % (board[6],board[7],board[8]))
# def take_turn():
#   print("Where would you like to place your piece?")

#   # Input player's selection.
#   # Change the game board to reflect the selection.
#   # Check for victory

# def check_win(board, player_piece):
#   # Horizonal x3
#   # Vertical x3
#   # diag x2


square = 0
while square not in range(1,9):
  square = input(
            "Please input the number of the square on which you'd like to play.\nYour input should be a number within the range of 1-9\nwhere 1 corresponds to the top left square and 9 corresponds to the bottom right square.\n"
          )
  # print("in loop")

print("You've made a move at square %d" % square)
draw_board()





# All telephones have the same number scheme, right? Hold on let me google it. Yeah, all telephones do use the same number scheme except for these cool guys. ^.