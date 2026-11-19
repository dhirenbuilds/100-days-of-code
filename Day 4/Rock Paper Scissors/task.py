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

computer_choice = [rock, paper, scissors]
computer = random.randint(0, 2)

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice < 0 or user_choice > 2:
    print("Invalid choice!")

else:
    print("Your choice:")
    print(computer_choice[user_choice])

    print("Computer chose:")
    print(computer_choice[computer])

    if user_choice == computer:
        print("Draw!")
    elif user_choice == 0 and computer == 2:
        print("You Win!")
    elif user_choice == 1 and computer == 0:
        print("You Win!")
    elif user_choice == 2 and computer == 1:
        print("You Win!")
    else:
        print("You Lose!")