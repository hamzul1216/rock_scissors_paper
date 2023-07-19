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
import random

print("----------------------------------------------------------------------")
print("\t\tWelcome to Rock-Scissors-Paper Games!!")
print("----------------------------------------------------------------------")

input_images = [rock, scissors, paper]

user_input = int(input("What do you choose? Type: \n- 0 for Rock \n- 1 for Scissors \n- 2 for Paper \nChoose: "))
if user_input < 0 or user_input >= 3:
    print("You typed an invalid number!")
else:
    print(input_images[user_input])

    computer_input = random.randint(0, 2)
    print("Computer chose:")
    print(input_images[computer_input])

    if user_input == 0 and computer_input == 0:
        print("Draw!")
    elif user_input == 0 and computer_input == 1:
        print("You win!")
    elif user_input == 0 and computer_input == 2:
        print("You lose")
    elif user_input == 1 and computer_input == 0:
        print("You lose!")
    elif user_input == 1 and computer_input == 1:
        print("Draw!")
    elif user_input == 1 and computer_input == 2:
        print("You win! ")
    elif user_input == 2 and computer_input == 0:
        print("You win! ")
    elif user_input == 2 and computer_input == 1:
        print("You lose!")
    elif user_input == 2 and computer_input == 2:
        print("Draw!")

print("----------------------------------------------------------------------")
