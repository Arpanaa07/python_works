#Chapter 1
print("Hello Python!")

#Chapter 2-variables, data types
message = ("Hello Python world!")
print(message)

#changing value
message = "Hello Python Crash Course!"
print(message)

#name cases
name = "winnie harlow"
print(name.title())
print(name.upper())
print(name.lower())

#variables in strings
first_name = "winnie"
last_name = "harlow"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

#adding whitespace
print("Java")
print("\tJava")
print("Languages:\nJava\nGo\nRust")

#stripping
favorite_language = ' java '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

#quote
famous_person = "Marie Curie"
message = f'{famous_person} once said, “Nothing in life is to be feared, it is only to be understood.”'
print(message)

#numbers
print(5 + 4)
print(6 - 1)
print(4 * 2)
print(8 / 4)
print(4 ** 3)
print((3 + 2) * 3)

#floats
print(0.5 + 0.4)
print(3 * 0.3)

#constants/comments
MAX_USERS = 10000  # a constant

#Chapter 3-Lists

#list of devices
devices = ['iphone', 'samsung', 'pixel', 'nokia']
print(devices[0].title())

#modifying elements
brands = ['dell', 'hp', 'asus']
brands[0] = 'lenovo'

#adding elements
brands.append('acer')

#inserting elements
brands.insert(0, 'msi')

#deleting elements
del brands[0]

#popping elements
last_brand = brands.pop()

#sorting
languages = ['python', 'java', 'c++', 'ruby']
languages.sort()
languages.sort(reverse=True)

#temporary sort
print(sorted(languages))

#length of list
print(len(languages))

#Chapter 4- working with lists

#looping
magicians = ['nina', 'zack', 'jules']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

#range
for value in range(3, 7):
    print(value)

#list of numbers
numbers = list(range(20, 25))

#even numbers
even_numbers = list(range(6, 16, 2))

#squares
squares = []
for value in range(5, 10):
    squares.append(value**2)

#list comprehensions
squares = [value**2 for value in range(5, 10)]

#slicing
players = ['alex', 'bella', 'chris', 'diana', 'evan']
print(players[0:3])
print(players[:4])
print(players[2:])

#copying lists
my_foods = ['sushi', 'ramen', 'dumplings']
friend_foods = my_foods[:]

#tuples
dimensions = (600, 200)
print(dimensions[0])

#reassigning tuple
dimensions = (900, 400)
for dimension in dimensions:
    print(dimension)

#styling
languages = ['python', 'java', 'go']
for language in languages:
    print(language.title())

pets = ['dog', 'cat', 'rabbit']
for pet in pets:
    print(f"I like {pet}s!")
print("I really love animals!")

#Chapter 5-If statements

# if
cars = ['mercedes', 'volvo', 'kia', 'renault']
for car in cars:
    if car == 'kia':
        print(car.upper())
    else:
        print(car.title())

#checking conditions
age = 30
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 20

#in, not in
requested_toppings = ['jalapenos', 'onions', 'spinach']
'jalapenos' in requested_toppings  # True
'bacon' not in requested_toppings  # True

#boolean
game_active = True
can_edit = False

#Chapter 6
student = {'name': 'Ava', 'age': 21}
print(student['name'])

student['major'] = 'Computer Science'
print(student)

profile = {}
profile['username'] = 'techgirl'
profile['email'] = 'ava@example.com'

user_info = {'username': 'neo99', 'status': 'active'}
for key, value in user_info.items():
    print(f"{key}: {value}")

users = {
    'user1': {'name': 'Liam', 'city': 'Paris'},
    'user2': {'name': 'Zoe', 'city': 'Berlin'}
}

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
print(f"You ordered a {pizza['crust']}-crust pizza with:")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

#Chapter 7
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

prompt = "If you tell us who you are, we can personalize the messages you see."
name = input(prompt)
print(f"\nHello, {name}!")

age = input("How old are you? ")
age = int(age)

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and I will repeat it back to you:"
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

while True:
    city = input("\nPlease enter the name of a city you have visited: ")
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

x = 1
while x <= 5:
    print(x)
    x += 1  # avoid infinite loop

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while 'cat' in pets:
    pets.remove('cat')

responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

#Chapter 8
def greet_user():
    print("Hello!")

def greet_user(username):
    print(f"Hello, {username.title()}!")

def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
describe_pet('harry', 'hamster')

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

#Chapter 9
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Lucy', 3)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

class Car:
    def __init__(self, make, model, year):
        self.manufacturer = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#Chapter 10
filename = 'pi_digits.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

with open(filename, 'a') as file_object:
    file_object.write("I also love exploring data.\n")
    file_object.write("I love making apps.\n")

try:
    with open('alice.txt') as f:
        contents = f.read()
except FileNotFoundError:
    print("Sorry, the file doesn't exist.")

def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt']
for filename in filenames:
    count_words(filename)

#Chapter 11- Testing the code
def get_formatted_name(first, last):
    full_name = f"{first} {last}"
    return full_name.title()

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\nNeatly formatted name: {formatted_name}")

import unittest

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()
