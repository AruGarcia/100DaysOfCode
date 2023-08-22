# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# chose_letter = []

list_password = []

# Selecionar as letras, numeros e simbolus aleatóriamente e salvar em uma lista.
for num in range(nr_letters):
    number = random.randint(0, 51)
    select_letter = letters[number]
    list_password.append(select_letter)

for num in range(nr_numbers):
    number_number = random.randint(0, 9)
    select_number = numbers[number_number]
    list_password.append(select_number)

for num in range(nr_symbols):
    symbol = random.randint(0, 8)
    select_symbol = symbols[symbol]
    list_password.append(select_symbol)


string_list_password = ''.join(list_password)
print(f'Easy level password: {string_list_password}')

# Shuffle e crir uma nova lista com numeros embaralhados.

nr_total = nr_letters + nr_numbers + nr_symbols

nr_list = []

for num in range(0, nr_total):
    nr_list.append(num)

shuffle_list = []
while nr_total > 0:
    shuffle_number = random.choice(nr_list)
    shuffle_list.append(list_password[shuffle_number])
    list_password.remove(list_password[shuffle_number])
    nr_list.remove(nr_list[-1])
    nr_total = nr_total - 1


string_list_password = ''.join(shuffle_list)
print(f'Hard level password: {string_list_password}')
