# Instructions
#
# You are going to write a program that tests the compatibility between two people.
#
# To work out the love score between two people:
#
#     Take both people's names and check for the number of times the letters in the word TRUE occurs.
#
#     Then check for the number of times the letters in the word LOVE occurs.
#
#     Then combine these numbers to make a 2 digit number.
#
# For Love Scores less than 10 or greater than 90, the message should be:
#
# "Your score is **x**, you go together like coke and mentos."
#
# For Love Scores between 40 and 50, the message should be:
#
# "Your score is **y**, you are alright together."
#
# Otherwise, the message will just be their score. e.g.:
#
# "Your score is **z**."

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

lower_name1 = name1.lower()
lower_name2 = name2.lower()

join_names = lower_name1 + lower_name2

numT = join_names.count("t")
numR = join_names.count("r")
numU = join_names.count("u")
numE = join_names.count("e")

somaTRUE = str(numT + numR + numU + numE)

numL = join_names.count("l")
numO = join_names.count("o")
numV = join_names.count("v")
numE = join_names.count("e")

somaLOVE = str(numL + numO + numV + numE)

combine = int(somaTRUE + somaLOVE)

if combine < 10 or combine > 90:
    print(f"Your score is {combine}, you go together like coke and mentos.")
elif 40 <= combine <= 50:
    print(f"Your score is {combine}, you are alright together.")
else:
    print(f"Your score is {combine}.")
