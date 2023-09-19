import math


# 1. Write a Python program to create a class representing a Circle. Include
# methods to calculate its area and perimeter. https://www.w3resource.com/python-exercises/oop/index.php

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area_of_a_circle(self):
        return math.pi * self.radius ** 2

    def perimeter_of_a_circle(self):
        return 2 * math.pi * self.radius


circle1 = Circle(4)
circle1.area_of_a_circle()
circle1.perimeter_of_a_circle()

# print(circle1.radius)
# print(f'{circle1.area_of_a_circle():.2f}')
# print(f'{circle1.perimeter_of_a_circle():.2f}')


# 2. Write a Python program to create a person class. Include attributes like name,
# country and date of birth. Implement a method to determine the person('s age.
# https://www.w3resource.com/python-exercises/oop/index.php)

class Person:
    all = []

    def __init__(self, name: str, country: str, birth_year: int, age=0):

        assert len(name) > 0, "You can't live an empty string."
        assert len(country) > 0, "You can't live an empty string."
        assert birth_year >= 1000, "The year should be written in full, such as '1990'."

        self.name = name
        self.country = country
        self.birth_year = birth_year
        self.age = None

        Person.all.append(self)

    def years(self):
        calculated_age = 2023 - self.birth_year
        self.age = calculated_age

    def __repr__(self):
        return f"Person('{self.name}', '{self.country}', '{self.birth_year}', '{self.age})"


add_person = True
new_person = "y"

while add_person:
    if new_person == "y":
        name = (input("What is your name? ")).title()
        country = (input("Which country were you birth in? ")).title()
        birth_year = int(input("What year were you born? "))
        person = Person(name, country, birth_year)
        person.years()
        new_person = input("Do you want to add a new person? (y/n) ")
    else:
        add_person = False

# print(person1.name, person1.country, person1.birth_year)

# print(person)
# years = person.years()
# print(years)

print(Person.all)
