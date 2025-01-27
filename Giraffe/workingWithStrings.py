

print("Giraffe Academy")

# to print out new line \n
print("Giraffe\nAcademy")

# to print out " mark \"
print("Giraffe\"Academy")

# to print out /
print("Giraffe/Academy")

# store value in variable and call it
phrase = "Giraffe Academy"
print(phrase)

# concatenation (appending another string)
phrase = "Giraffe Academy"
print(phrase, "is cool")

# call function, lower/upper case
phrase = "Giraffe Academy"
print(phrase.lower())
print(phrase.upper())

# call function, check upper/lower case, will return true/false
print(phrase.isupper())

# call 2 functions, change it to upper then check upper/lower case, will return true/false
print(phrase.upper().isupper())

# to check how many characters
print(len(phrase))

# to get the specific letter
print(phrase[0])
print(phrase[8])

# index function, specific character located
print(phrase.index("Ac"))

# replace function
print(phrase.replace("Giraffe", "Elephant"))

