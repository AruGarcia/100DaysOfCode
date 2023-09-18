import csv


# class Costumer:
#     def __init__(self, name, membership_type):
#         self.name = name
#         self.membership_type = membership_type
#
#     def update_membership(self, new_membership):
#         self.membership_type = new_membership


# # num01 = Costumer("Aruana", "Silver")
# # print(num01.name, num01.membership_type)
# #
# # num02 = Costumer("Eleonora", "Gold")
# # print(num02.name, num02.membership_type)

# costumers = [
#     Costumer("Aruanã", "Silver"),
#     Costumer("Eleonora", "Gold")
# ]
#
# print(costumers[1].membership_type)
# costumers[1].update_membership("Black")
# print(costumers[1].membership_type)

# class Car:
#     def __init__(self, color, seats):
#         self.color = color
#         self.seats = seats
#
#     def enter_race_mode(self):
#         self.seats = 2
#         return self.seats
#
#
# fusca = Car("blue", 5)
#
# print(fusca.color, fusca.seats, fusca.enter_race_mode())


class Item:
    pay_rate = 0.8  # atributos de classe
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Price {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

        # print(f"name = {self.name}, price = R${self.price}, quantity = {self.quantity}")
        # print(f"total price = R${self.calculate_total_price()}")

    def calculate_total_price(self):
        """
        This function calculate total price of the buy.
        :return: value of the buy.
        """
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"


# item1 = Item("Phone", 100, 1)
# item2 = Item("Computer", 1000, 1)
#
# print(f"name = {item1.name}, price = R${item1.price}, quantity = {item1.quantity}")
# print(f"Real price = R${item1.calculate_total_price()}")
# item1.apply_discount()
# print(f"Discount price = R${item1.price}")
#
# print(f"name = {item2.name}, price = R${item2.price}, quantity = {item2.quantity}")
# print(f"Real price = R${item2.calculate_total_price()}")
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(f"Discount price = R${item2.price}")

# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

Item.instantiate_from_csv()
print(Item.all)
