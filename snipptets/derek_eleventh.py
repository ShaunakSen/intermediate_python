# STATIC AND EXCEPTION HANDLING

# STATIC METHOD: Allows access without creating objects


class Sum:
    @staticmethod
    def getSum(*args):
        total = 0
        for item in args:
            total += item

        return total


class Dog:
    # STATIC VAR
    number_of_dogs = 0

    def __init__(self, name="Timmy"):
        self.name = name
        Dog.number_of_dogs += 1

    @staticmethod
    def getNumberOfDogs():
        print("There are {} dogs".format(Dog.number_of_dogs))


def main():
    print("Sum is:", Sum.getSum(1, 2, 3))
    spot = Dog("Spot")
    snowy = Dog("Snowy")
    spot.getNumberOfDogs()
    snowy.getNumberOfDogs()


main()
