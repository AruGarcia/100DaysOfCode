#from replit import clear
from art import logo

print(logo)
# HINT: You can call clear() to clear the output in the console.

bidders = {}


def new_bid():

    new_name = input('What is your name? ')
    new_bid = float(input('What is your bid? $'))
    bidders[new_name] = new_bid


finish_game = True

while finish_game:
    new_bid()

    other_bidders = input("Are there other bidders? Type 'yes' or 'no'. \n")

    if other_bidders == 'yes':
        pass #clear()
    else:
        finish_game = False

winner = max(bidders, key=bidders.get)
winning_bid = bidders[winner]

print(f"The winner is {winner} with a bid of ${winning_bid}.")




# people = [
#     {"name": "Alice", "height": 160},
#     {"name": "Bob", "height": 175},
#     {"name": "Charlie", "height": 170},
#     {"name": "David", "height": 182}
# ]
# tallest_person = max(people, key=lambda person: person["height"])
# print(tallest_person)  # Saída: {"name": "David", "height": 182}







# people = [
#     {"name": "Alice", "height": 160},
#     {"name": "Bob", "height": 175},
#     {"name": "Charlie", "height": 170},
#     {"name": "David", "height": 182}
# ]

# # Inicialize as variáveis para a pessoa mais alta
# tallest_person = None
# max_height = 0

# # Itere através da lista de pessoas
# for person in people:
#     height = person["height"]
#     if height > max_height:
#         max_height = height
#         tallest_person = person

# if tallest_person is not None:
#     print(tallest_person)
# else:
#     print("Nenhuma pessoa na lista.")








# # Inicialize as variáveis do vencedor e do lance vencedor
# winner = None
# winning_bid = 0

# # Itere através do dicionário de licitantes
# for bidder, bid in bidders.items():
#     if bid > winning_bid:
#         winner = bidder
#         winning_bid = bid

# # Verifique se há um vencedor
# print(f"The winner is {winner} with a bid of ${winning_bid}.")
