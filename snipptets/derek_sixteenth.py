import re
# Did you find a match
# if re.search("REGEX", yourString)

# Get list of matches
# print("Matches :", len(re.findall("REGEX", yourString)))

# Get a pattern object
# regex = re.compile("REGEX")

# Substitute the match
# yourString = regex.sub("substitution", yourString)

# [ ]   : Match what is in the brackets
# [^ ]  : Match anything not in the brackets
# .     : Match any 1 character or space
# +     : Match 1 or more of what proceeds
# \n    : Newline
# \d    : Any 1 number
# \D    : Anything but a number
# \w    : Same as [a-zA-Z0-9_]
# \W    : Same as [^a-zA-Z0-9_]
# \s    : Same as [\f\n\r\t\v]
# \S    : Same as [^\f\n\r\t\v]
# {5}   : Match 5 of what proceeds the curly brackets
# {5,7} : Match values that are between 5 and 7 in length

# ---------- Matching Zero or One ----------

# Match 0 or 1 of specific thing with '?'
randStr = "cat cats"
# We want to match for cat as well as cats
# ?: Matches 0 or 1 of whatever proceeds it
regexp = re.compile("[cat]+s?")
matches = re.findall(regexp, randStr)
print(matches)

# Match 0 or more with '*'

randStr = "doctor doctors doctor's"
regexp = re.compile("[doctor]+['s]*")
matches = re.findall(regexp, randStr)
print(matches)

# ----PROBLEM----
# NewLines in windows are represented by \n or \r\n
# Match them in the string below

randStr = '''Just some words
and some more\r
and more
'''

regexp = re.compile("[\w\s]+[\r]?\n")
matches = re.findall(regexp, randStr)
print(matches)

# Greedy and Lazy Matching

randStr = "<name>Life on Mars</name><name>Freaks and Geeks</name>"

# We want output:
# ['<name>Life on Mars</name>', '<name>Freaks and Geeks</name>']

regexp = re.compile("<name>.*</name>")
matches = re.findall(regexp, randStr)
print(matches)

# here output is:
# ['<name>Life on Mars</name><name>Freaks and Geeks</name>']
# * is greedy. It grabs biggest match possible

# We have to make it lazy

regexp = re.compile("<name>.*?</name>")
matches = re.findall(regexp, randStr)
print(matches)

# Using sub expressions

regexp = re.compile("<name>(.*?)</name>")
matches = re.findall(regexp, randStr)
print(matches)


# WORD BOUNDARIES

# Used to define where our matches both start and end

# \b: Matches start as well as end of a word

randStr = "ape at the apex"
regexp = re.compile(r"ape")
matches = re.findall(regexp, randStr)
print(matches)
# Output: ['ape', 'ape']
# We want to match exactly 'ape' not 'ape...'
regexp = re.compile(r"\bape\b")
matches = re.findall(regexp, randStr)
print(matches)


# String Boundaries

# ^: match beginning of string
# $: End of string

randStr = "Match everything up to @"
regexp = re.compile(r"^.*[^@]")
matches = re.findall(regexp, randStr)
print(matches)

randStr = "@ Get this part only"
regexp = re.compile(r"[^@\s].*$")
matches = re.findall(regexp, randStr)
print(matches)

randStr = '''Ape is big
Turtle is slow
Cheetah is fast
'''

regexp = re.compile(r"[^@\s].*$")
matches = re.findall(regexp, randStr)
print(matches)

















