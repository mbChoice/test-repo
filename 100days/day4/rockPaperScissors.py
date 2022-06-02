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
---'    ____)____
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

user_choice = int(input("Pick 0 for rock, 1 for paper, 2 for scissors: "))
if user_choice >= 3 or user_choice < 0: 
    print(f"You typed and invalid number. You lose: {user_choice}.")
else:
    print("\nYou picked:")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer picked:")
    print(game_images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print('You won')
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You won")
    elif computer_choice == user_choice:
        print("Its a draw")
