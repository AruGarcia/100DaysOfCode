import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇

game_list = []

player01 = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors." "\n")
)

game_list.append(player01)

player02 = random.randint(0, 2)

game_list.append(player02)

if game_list[0] == 0:
    if game_list[1] == 0:
        print("Computer chose")
        print(rock)
        print("Your chose")
        print(rock)
        print("It's a draw")
    elif game_list[1] == 1:
        print("Computer chose")
        print(paper)
        print("Your chose")
        print(rock)
        print("You lose!")
    else:
        print("You win!")
        print("Computer chose")
        print(scissors)
        print("Your chose")
        print(rock)
        print("You win!")

elif game_list[0] == 1:
    if game_list[1] == 0:
        print("Computer chose")
        print(rock)
        print("Your chose")
        print(paper)
        print("You win!")
    elif game_list[1] == 1:
        print("Computer chose")
        print(paper)
        print("Your chose")
        print(paper)
        print("It's a draw")
    else:
        print("Computer chose")
        print(scissors)
        print("Your chose")
        print(rock)
        print("You win!")

else:
    if game_list[1] == 0:
        print("Computer chose")
        print(rock)
        print("Your chose")
        print(scissors)
        print("You lose!")

    elif game_list[1] == 1:
        print("Computer chose")
        print(paper)
        print("Your chose")
        print(scissors)
        print("You win!")

    else:
        print("Computer chose")
        print(scissors)
        print("Your chose")
        print(scissors)
        print("It's a draw")
