# REGULAR EXPRESSIONS
# They are used for:
# Search specific string in a large amount of data
# Verify if string has proper format
# Find string and replace with another
# Format data into proper form for importing

import re

if re.search("ape", "The ape was happy"):
    print("There is an ape")

# findAll() -> finds all the matches

allApes = re.findall("ape.", "The ape was at the apex")

for i in allApes:
    print(i)

# . -> matches any one char or any one space

theStr = "The ape was at the apex"

for i in re.finditer("ape.", theStr):
    locTuple = i.span()
    print(locTuple)
    print(theStr[locTuple[0]:locTuple[1]])

# Match one of any of several letters

# [] -> matches any chars between them

animalStr = "Cat rat mat pat"

allAnimals = re.findall("[Crmfp]at", animalStr)
print(allAnimals)

# Match ranges of characters

someAnimals = re.findall("[c-mC-M]at", animalStr)
print(someAnimals)

someAnimals = re.findall("[^Cr]at", animalStr)
print(someAnimals)

# Replacing Strings

owlFood = "rat cat mat pat"

# Anything that can be  an owl food should be replaced by the word 'owl'

regex = re.compile("[cr]at")
owlFood = regex.sub("owl", owlFood)
print(owlFood)

# Solving '\' problem

# say we are trying to get string '\\stuff'

randStr = "Here is \\stuff"

print("Find \\stuff:", re.search("\\stuff", randStr))

# Does not work

# use raw string: treats '\' as special

print("Find \\stuff:", re.search(r"\\stuff", randStr))

# Matching any single char
# . -> matches any char
# How to match a '.' ?

randStr = "F.B.I. R.A.W. CIA"

print("Matches:", re.findall('.\..\..\.', randStr))

# any character followed by . then any character followed by . then any character followed by .

# Match for whitespace

randStr = '''This is a long
string that goes
on for many lines
'''

print(randStr)

# Remove newlines

regex = re.compile("\n")
randStr = regex.sub(" ", randStr)
print(randStr)






