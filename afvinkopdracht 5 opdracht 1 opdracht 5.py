import random
def rock_paper_scissors():
    '''if random number is 1 the computer chooses rock,
if the random number is 2 the computer chooses paper
and if the random number is 3 the computer chooses scissors'''
computer = random.randint(1,3)
player = input('please enter Rock, Paper or Scissors')

if player.lower()=="rock":
    player = 1
elif player.lower()=="paper":
    player = 2
elif player.lower()=="scissors":
    player = 3

#Rock = 1
#Paper = 2
#Scissors = 3

print(player)
print(computer)
if computer == 1:
    print('The computer chooses Rock')
    if player == computer:
        print('Please enter Rock, Paper or Scissors')
    elif player == 2:
        print('The player wins')
    else:
        print('The computer wins')
elif computer == 2:
    print('The computer chooses Paper')
    if player == computer:
        print('Please enter Rock,Paper or Scissors')
    elif player == 1:
        print('The computer wins')
    else:
        print('The player wins')
else:
    print('The computer chooses Scissors')
    if player == computer:
        print('Please enter Rock,Paper or Scissors')
    elif player == 1:
        print('The Player wins')
    else:
        print('The computer wins')

while computer == player:
    computer = random.randint(1,3)
    player = input('Please enter Rock, Paper or Scissors')


print(player)
print(computer)
if computer == 1:
    print('The computer chooses Rock')
    if player == computer:
        print('Please enter Rock, Paper or Scissors')
    elif player == 2:
        print('The player wins')
    else:
        print('The computer wins')
elif computer == 2:
    print('The computer chooses Paper')
    if player == computer:
        print('Please enter Rock,Paper or Scissors')
    elif player == 1:
        print('The computer wins')
    else:
        print('The player wins')
elif computer == 3:
    print('The computer chooses Scissors')
    if player == computer:
        print('Please enter Rock,Paper or Scissors')
    elif player == 1:
        print('The Player wins')
    else:
        print('The computer wins')
else:
    print('Its a tie')


def main():
    rock_paper_scissors()
main()






#if computer == 1:
#    print('The computer chooses Rock')
 #   if player == Rock:
  #      elif player == Paper
   #         print('The player wins')
    #            elif player = Scissors
     #               print('The computer wins')
#elif computer == 2:
#    print('The computer chooses Paper')
 #   if player =: 
  #      print('')
#elif computer == 3:
 #   print('The computer chooses Scissors')
  #  if player == Rock:
   #     print('The computer wins')
    #        elif player == Paper:
     #           print('The player wins')
      #              elif player == Scissors:
       #                 print('Please choose R')
