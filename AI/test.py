# Program to build a dictionary

# Given dictionary
dictionary = {"mutable":"can change", "immutable":"can not change",
        "abandon":"give up", "splendid":"magnificent",
        "admire":"praise", }

dictionary['set'] = 'collection of well-defined objects'

# Taking input from the $USER
print("Hello!")
word = input("Enter a word to search in the Dictionary : ")

# What is entered by the user, i.e. shownm
print("Given word is : " + word)

# Prints the meaning
print("It means : " + dictionary[word])
