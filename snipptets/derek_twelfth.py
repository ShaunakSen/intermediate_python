def mult_by_2(num):
    return num * 2


# ASSIGN FUNCTION TO VAR
times_two = mult_by_2

print("4 * 2 =", times_two(4))


# PASS FUNCTION INTO A FUNCTION

def do_math(func, num):
    return func(num)


print("16 * 2 =", do_math(times_two, 16))


# DYNAMIC FUNCTIONS
def get_func_mult_by_num(num):
    # THIS FUNCTION DYNAMICALLY CREATES A FUNCTION AND RETURNS IT

    def mult_by(value):
        return num * value

    return mult_by


generated_func = get_func_mult_by_num(5)

print("5 * 10 =", generated_func(10))

# EMBED FUNCTIONS INSIDE A DATA STRUCTURE

listOfFunctions = [times_two, generated_func]

print("5 * 9 =", listOfFunctions[1](9))


# ----PROBLEM-----
# Create a func which receives a list and a func
# The func passed will return true or false if list value is odd
# the surrounding func will return a list of odd nos


def is_it_odd(num):
    if num % 2 == 0:
        return False
    return True


def change_list(myList, func):
    for item in myList:
        if func(item) is not True:
            myList.remove(item)
    return myList


bigList = [1, 2, 3, 4, 5, 6]
bigList = change_list(bigList, is_it_odd)
print(bigList)


# FUNCTION ANNOTATIONS: For documentation reasons only

def random_func(name: str, age: int, weight: float) -> str:
    print("Name:", name)
    print("Age:", age)
    print("Weight:", weight)

    return "{} is {} years old and weighs {} Kg".format(name, age, weight)


print(random_func("Mini", 20, 50))
# print(random_func(1, 2, 3))
print(random_func.__annotations__)

# ANONYMOUS FUNCTIONS USING LAMBDA

# lambda arg1, arg2, ... : expression use the args

sum_func = lambda x, y: x + y

print("Sum:", sum_func(4, 5))

can_vote = lambda age: True if age >= 18 else False

print("Can Vote:", can_vote(11))

powerList = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]

for func in powerList:
    print(func(4))

# STORE LAMBDAS INSIDE DICTIONARIES

attack = {'quick': (lambda: print('Quick Attack!')),
          'power': (lambda: print('Power Attack!')),
          'miss': (lambda: print('Missed Attack!'))
          }

attack['quick']()

import random

print(list(attack.keys()))
attackKey = random.choice(list(attack.keys()))

attack[attackKey]()

# ----PROBLEM-----
# Create random  list filled with chars H & T
# Output no of H and T

sizeOfList = 100
choiceList = ['H', 'T']
generatedList = []
for i in range(sizeOfList):
    headOrTail = random.choice(choiceList)
    generatedList.append(headOrTail)

print(generatedList)

print("Heads:", generatedList.count('H'))
print("Tails:", generatedList.count('T'))

# MAP FUNCTION
# Execute a function on each item of a list

oneTo10 = range(1, 11)
print(list(map(times_two, oneTo10)))
print(list(map(lambda x: x * 3, oneTo10)))

# Calculations against multiple lists

aList = list(map(lambda x, y: x + y, [1, 2, 3], [1, 2, 5]))
print(aList)

# FILTER
# Select items from a list based on a function

# Print even values from list

print(list(filter(lambda x: x % 2 == 0, range(1, 11))))

# ----PROBLEM-----
# Find multiples of 9 from a random 100 value list with
# values from 1 and 1000
bigList1 = []
for x in range(1, 101):
    getRandomNum = random.choice(range(1, 1001))
    bigList1.append(getRandomNum)

multiplesOf9 = list(filter(lambda x: x % 9 == 0, bigList1))
print(multiplesOf9)

# REDUCE
# takes in a list and returns a single result

from functools import reduce

# Add values in list

print(reduce(lambda x, y: x + y, range(1, 6)))
