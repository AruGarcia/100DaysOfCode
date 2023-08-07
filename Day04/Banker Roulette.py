import random

# Instructions

# You are going to write a program that will select a random
# name from a list of names. The person selected will have to
# pay for everybody's food bill.
#
# Important: You are not allowed to use the choice() function.
#
# Line 8 splits the string names_string into individual names and
# puts them inside a List called names. For this to work, you must
# enter all the names as names followed by comma then space. e.g. name, name, name
#
# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.
#
# Example Output
# Michael is going to buy the meal today!

# Hint
# You might need the help of the len() function.

# Split string method
names_string= input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# First *fork* your copy. Then copy-paste your code below this line 👇
# Finally click "Run" to execute the test


num_of_names = len(names)
random_names = random.randint(0, num_of_names)

print(names[random_names])

