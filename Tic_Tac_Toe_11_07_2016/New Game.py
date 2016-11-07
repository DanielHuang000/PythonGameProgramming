import TicTacToelib as T


Grid = {(1,1):' ',(1,2):' ',(1,3):' ',(2,1):' ',
 (2,2):' ',(2,3):' ',(3,1):' ',(3,2):' ',(3,3):' '}

count = 0
while not T.rules(Grid) and count<9:
  if count%2==0:
   Grid = T.getInput(Grid, 'O')
   T.form(Grid)
   if T.rules(Grid):
    print("O wins")

  if count%2==1:
   Grid = T.getInput(Grid, 'X')
   T.form(Grid)
   if T.rules(Grid):
    print("X wins")
  count+=1
if not T.rules(Grid) and count==9:
 print("Tie")
print("Game over")



