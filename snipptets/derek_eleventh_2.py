# Exception Handling

try:
    # PROBLEMATIC CODE GOES HERE
    aList = [1, 2, 3]
    print(aList[3])

except IndexError:
    print("Index Out of Bounds !!")

except:
    print("Unknown error occurred")


# CUSTOM EXCEPTIONS

class DogNameError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


try:
    dogName = input("What is ur dog's name? ")
    if any(char.isdigit() for char in dogName):
        raise DogNameError

except DogNameError:
    print("Dog's name cant contain a no")

# FINALLY

num1, num2 = input("Enter 2 nos to divide: ").split()

try:
    quotient = int(num1) / int(num2)
    print("{}/{}={}".format(num1, num2, quotient))
except ZeroDivisionError:
    print("Cant divide by 0")

else:
    # IF EXCEPTION DOES NOT OCCUR
    print("all ok :)")

finally:
    print("End of Code")


# CREATE FILE mydata2
# OPEN FILE WITHOUT USING WITH
# CATCH FILENOTFOUND


try:
    myFile = open("mydata.txt", encoding="utf-8")
except FileNotFoundError as ex:
    print("That file was not found")
    print(ex.args)

else:
    print("File Data:")
    print(myFile.read())
    myFile.close()
finally:
    print("End of Code")



