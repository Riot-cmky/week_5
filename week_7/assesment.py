# Week 7 Assement: Oscar Levya & Devin Branch

# Ask the user for input (text, article, quote, etc)
text = input("Give me a random text:").lower()
print(text)

# Ask the use for three random letters
letter1 = input("Enter a random lowercase letter: ").lower()
letter2 = input("Enter a random lowercase letter: ").lower()
letter3 = input("Enter a random lowercase letter: ").lower()

# Store letter counts in a list
lettercount = [letter1, letter2, letter3]

# Display how many times these letters occur in the text
for letter in lettercount:
    print(text.count(letter))

# Display how many words are in the text
textWords = text.split()
print(textWords)
print("There is a total of" , len(textWords) , "words in the text.")

# Find the first and last letters of the text using indexing
first_letter = (text[0])
last_letter = (text[-1])
print("The first letter in the text was " + first_letter + ".")
print("The last letter of the text is " + last_letter + ".")

# Reverse the text and join with spaces
print(" ".join(text[::-1]))

# Check for "python" in the text using dictionaries
print("python" in text)