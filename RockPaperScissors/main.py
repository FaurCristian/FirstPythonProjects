import random

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
game_images = [rock, paper, scissors]
player_choice = int(input ("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice =random.randint(0,2)
if player_choice > 2 or player_choice < 0:
    print("You enter a invalid number")
else:
    print(game_images[player_choice])
    print(game_images[computer_choice])

    if player_choice == computer_choice:
        print("This is a drow!")
    elif player_choice == 0 and  computer_choice == 1:
        print("You lose!")
    elif player_choice == 0 and computer_choice == 2:
        print("You win!")
    elif player_choice == 1 and computer_choice == 0:
        print("You win!")
    elif player_choice == 1 and computer_choice == 2:
        print("You lose!")
    elif player_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif player_choice == 2 and computer_choice == 1:
        print("You win!")