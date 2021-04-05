player = 1
winner = None
times = 0
last_index = 0
board = ["-","-","-","-","-","-","-","-","-"]
print (board[0], "|", board[1], "|", board[2] )
print (board[3], "|", board[4], "|", board[5] )
print (board[6], "|", board[7], "|", board[8] )

def check_win():
  global winner
  if times >= 9:
      winner = "draw"
      return True
  if (board[0] == board[1] == board [2] != "-") or (board[3] == board[4] == board [5]!= "-") or (board[6] == board[7] == board [8]!= "-"):
      print(board[0])
      winner ="Player 1" if board[last_index] == "X" else "Player 2"
      return True
  if (board[0] == board[3] == board [6]!= "-") or (board[1] == board[4] == board [7]!= "-") or (board[2] == board[5] == board [8]!= "-"):
      winner ="Player 1" if board[last_index] == "X" else "Player 2"
      return True
  if (board[0] == board[4] == board [8]!= "-") or (board[2] == board[4] == board [6]!= "-"):
      winner ="Player 1" if board[last_index] == "X" else "Player 2"
      return True

while True:
  if check_win():
    print(f"{winner} won")
    break
  try:
    ip = int(input(f"Player {player} turn:")) - 1
  except:
    print("Invalid input")
    continue
  if ip >= 9 or board[ip] != "-":
    print("Invalid input")
    continue
  last_index = ip
  times = times + 1
  board[ip] = "X" if player == 1 else "O"
  if player == 1: 
   player = 2
  else: 
   player = 1 
  print (board[0], "|", board[1], "|", board[2] )
  print (board[3], "|", board[4], "|", board[5] )
  print (board[6], "|", board[7], "|", board[8] ) 
