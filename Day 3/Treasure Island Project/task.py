print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure. But remember whoever has tried going there has never returned.")

print("You are about to reach the island by boat. Suddenly, a storm approaches.")
choice1 = input("What do you do? Type Swim or Wait: ")

if choice1 == "Swim":
    print("You safely reached the island.")

    print("You discover 2 paths...")
    choice2 = input("Type Forest for Dark Forest or Rock for Rocky Mountains: ")

    if choice2 == "Forest":
        print("You discover an abandoned campsite and a mysterious key.")
        print("An old pirate suddenly appears.")
        print("He says: I know where the treasure is. Follow me, and I'll show you.")

        choice3 = input("Type Trust, Refuse or Ask: ")

        if choice3 == "Trust":
            print("The pirate leads you into a trap.")
            print("GAME OVER")

        elif choice3 == "Refuse":
            print("You discover a hidden cave.")
            print("You finally discover an ancient temple with three doors.")

            choice4 = input("Type Red, Blue or Golden: ")

            if choice4 == "Red":
                print("You found a secret underground passage!")
                print("You found the ONE PIECE! But it's guarded by a dragon.")

                choice5 = input("Fight Dragon or Run Away: ")

                if choice5 == "Fight":
                    print("The dragon is impressed by your courage.")
                    print("It gives you the ONE PIECE!")
                    print("YOU WON!")

                elif choice5 == "Run Away":
                    print("You ran away and got killed by a bear.")
                    print("GAME OVER")

                else:
                    print("Invalid choice. GAME OVER.")

            elif choice4 == "Golden":
                print("A trap is triggered.")
                print("GAME OVER.")

            elif choice4 == "Blue":
                print("You found a room filled with gold.")
                print("You PARTIALLY WON!")

            else:
                print("Invalid choice. GAME OVER.")

        elif choice3 == "Ask":
            print("He says he doesn't know and runs away.")
            print("GAME OVER")

        else:
            print("Invalid choice. GAME OVER.")

    elif choice2 == "Rock":
        print("You encounter a dangerous obstacle and die.")
        print("GAME OVER")

    else:
        print("Invalid choice. GAME OVER.")

elif choice1 == "Wait":
    print("Your boat gets damaged, and you die.")
    print("GAME OVER")

else:
    print("Invalid choice. GAME OVER.")
