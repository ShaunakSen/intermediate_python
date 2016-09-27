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

# Match numbers

# \d : [0-9]
# \D: [^0-9]

randStr = "12345"
print("Matches:", re.findall("\d", randStr))
# Match multiple nos

print("Matches:", re.findall("\d{5}", randStr))

# Match within a range

numStr = "123 12345 123456 1234567"

# Match nos which are 5, 6 or 7 in length

print("Matches:", re.findall("\d{5,7}", numStr))


# Match any single letter or number

# \w: [a-zA-Z0-9_]
# \W: [^a-zA-Z0-9_]

# Check for valid phone no


phNum = "412-555-1212"

if re.search("\d{3}-\d{3}-\d{4}", phNum):
    print("Valid ph no")

# Check for valid first name
# Valid : 2-20 chars

if re.search("\w{2,20}", "Mini"):
    print("Valid name")

# \s: [\f\n\t\r\v]
# \s: [^\f\n\t\r\v]

# Check for valid first and last name

if re.search("\w{2,20}\s\w{2,20}", "Mini Sen"):
    print("Valid name")


# +: One or more chars

# Match for 'a' followed by 1 or more chars

print("Matches:", re.findall("a+", "a mini budhhu blaah"))

# Match email address

# 1 - 20 lowercase and uppercase letters, nos plus ._%+-
# An @ symbol
# 2-20 lowercase and uppercase letters, nos plus .-
# A period
# 2-3 lowercase and uppercase letters

emailList = "db@aol.com m@.com @apple.com db@.com"

print("Email matches:", re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", emailList))