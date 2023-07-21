# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

print('Welcome to the tip calculator.\n')

bill = float(input('What was the total bill? '))
percentage = int(input('What percentage tip you like to give? 10, 12 or 15? '))

people = float(input('How many people to split the bill? '))

if percentage == 10:
    should_pay = (bill / people) * 1.1

elif percentage == 12:
    should_pay = (bill / people) * 1.12

elif percentage == 15:
    should_pay = (bill / people) * 1.15

if percentage > 15:
    print('Write a valid percentage, please.')

else:
    round_pay = round(should_pay, 2)
    print(f'Each person should pay: ${round_pay}')

