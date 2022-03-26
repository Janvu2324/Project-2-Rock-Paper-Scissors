rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random


game_choice=[rock,paper,scissors]


user_choice=int(input('What do you choose? Type 0 for Rock,1 for Paper and 2 for scissors.\n'))


if(user_choice>=3 or user_choice<0):
  print('You type Invalid number. You loose.')
else:
  
  print(game_choice[user_choice])
  computer_choice=random.randint(0,2)
  print('computers choice :')
  print(game_choice[computer_choice])


  if(user_choice == 0 and computer_choice == 2):
    print('You win')
  elif(user_choice == 2 and computer_choice ==       1):
    print('You win')
  elif(user_choice == 1 and computer_choice ==       0):
    print('You win')
  elif(user_choice == computer_choice):
    print('It is a Draw')
  else:
    print('You loose')


  


