# Iterables, Iterators, List comprehensions, Generator Functions, Generators Expressions

# Iterable: List of Values

# Iterable is object with method __iter__
# This returns an iterator
# An iterator is an object with method __next__

import random

simpleString = iter("Sample")
print("Char:", next(simpleString))
print("Char:", next(simpleString))


# Add iterator behavior to a custom class

class Alphabet:
    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.letters) - 1:
            raise StopIteration

        self.index += 1
        return self.letters[self.index]


alpha = Alphabet()

for letter in alpha:
    print(letter)


# -----PROBLEM-----
# Create a class that returns values from Fibonacci
# sequence each time next is called

class Fibonacci:
    def __init__(self):
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        fibNum = self.first + self.second
        self.first = self.second
        self.second = fibNum
        return fibNum


FibSeq = Fibonacci()
for i in range(10):
    print("Fib:", next(FibSeq))

# List Comprehensions

# Maps and List Comprehensions

print(list(map(lambda x: x * 2, range(1, 11))))
print([i * 2 for i in range(1, 11)])

# Filters and List Comprehensions

print(list(filter(lambda x: x % 2 != 0, range(1, 11))))
print([x for x in range(1, 11) if x % 2 != 0])

# List comprehension that acts like map and filter

# Generate 50 values
# Take each to power of 2
# Return multiples of 8

myList = []
for i in range(50):
    randomNum = random.randint(1, 9)
    myList.append(randomNum)

print(myList)

myList = [x ** 2 for x in myList]
print(myList)
myList = [x for x in myList if x % 8 == 0]
print(myList)

# Multiple for loops
# Multiply all values in one list with all values in another list

print([x * y for x in range(1, 3) for y in range(11, 16)])

# List comprehensions inside List comprehensions

# Generate a list of 10 values
# Multiply them by 2
# return multiples of 8

print([x * 2 for x in range(10) if (x * 2) % 8 == 0])
# OR
print([x for x in [i * 2 for i in range(10)] if x % 8 == 0])

# Generate 50 values bw 1 and 1000
# Return multiples of 9


myList = []
for i in range(50):
    randomNum = random.randint(1, 1000)
    myList.append(randomNum)
print([x for x in myList if x % 9 == 0])

# Shorter way
print([x for x in [random.randint(1, 1001) for i in range(50)] if x % 9 == 0])

# Working with multi dimensional lists

multiList = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

# print 2nd col

print([x[1] for x in multiList])

# print principal diagonal

print([multiList[i][i] for i in range(len(multiList))])


# Generator Functions

# Used when  we want to get a large no of results
# But we do not want to slow down our program by creating them all at same time

# Create generator that calculates primes and returns prime each time we ask for it

def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def gen_primes(max_number):
    for num1 in range(2, max_number):
        if isPrime(num1):
            yield num1


prime = gen_primes(50)

print("Prime:", next(prime))
print("Prime:", next(prime))
print("Prime:", next(prime))
print("Prime:", next(prime))
print("Prime:", next(prime))


# Generator expressions
# Look just like list comprehensions but return results one at a time

double = (x * 2 for x in range(10))
print("Double:", next(double))
print("Double:", next(double))
print("Double:", next(double))
print("Double:", next(double))


for num in double:
    print(num)
    # Note from where it starts printing

