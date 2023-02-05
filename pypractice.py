places = {
  1: "1",
  2: "2",
  3: "3",
  4: "4",
  5: "5",
  6: "6",
  7: "7",
  8: "8",
  9: "9"
}


def draw_board(places):
  board = (f"|{places[1]}|{places[2]}|{places[3]}|\n"
           f"|{places[4]}|{places[5]}|{places[6]}|\n"
           f"|{places[7]}|{places[8]}|{places[9]}|")
  print(board) #draw board on console



turn = 1 #defalut to player 1 


def turns(turn):
  if turn % 2 == 0:
    return "X"
  else:
    return "O"

done = False #win check flag
def win_check(places):
  if {places[1]}=={places[2]}=={places[3]}:
    print(f"player {int(turn%2)+1} is the winner!!")
    return True
  elif {places[4]}=={places[5]}=={places[6]}:
    print(f"player {int(turn%2)+1} is the winner!!")
    return True
  elif {places[1]}=={places[4]}=={places[7]}:
    print(f"player {int(turn%2)+1} is the winner!!")
    return True
  elif {places[7]}=={places[8]}=={places[9]}:
    print(f"player {int(turn%2)+1} is the winner!!")
    return True
  elif {places[7]}=={places[5]}=={places[3]}:
    print(f"player {int(turn%2)+1} is the winner!!")
    return True
  elif {places[1]}=={places[5]}=={places[9]}:
    print(f"player {int(turn%2)+1} is the winner!!")
    return True



  

  #main logic loop
while True:
  userinp = input(f"player {int(turn%2)} enter a digit between 0-8: ")
  if userinp == "q":
    break

  if int(userinp) in places and userinp.isdigit() == True:
    if not places[int(userinp)]in {"X","O"}:
      turn+=1
      places[int(userinp)]= turns(turn)
      draw_board(places)
      # win_check(places)
    if  win_check(places) == True:
      break
    if turn > 8:
      done = True
      break


  
  else:
    print("enter a single digit!")
if done == True:
  print("the match was Draw...(TRY AGAIN!!!)")

