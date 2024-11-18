# # while loop = execute some code WHILE some condition remains true
# while loops and for loops are forms of iteration
# iteration is the process pf repeating or looping through a set of steps or instructions
# to iterate is the verb form of iteration
# be careful of infinite loops, they will crash your program and you weill have to restart it
# infinite loops are loops that never end

# EXAMPLE 1

# name = input("Enter your name: ")

# if loop
# if name == "":
#     print("You did not enter your name")
# else:
#     print(f"Hello {name}")

# while loop runs forever until a condition is met
# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")

# print(f"Hello {name}")

# infinite loop (DO NOT USE THIS) use ctrl + c to stop it. infinite loops are bad and will crash your computer
# while name == "":
#     print("You did not enter your name")

# print(f"Hello {name}")

# EXAMPLE 2

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age cant be negative")
#     age = int(input("ENter your age: "))

# print(f"You are {age} years old")

# EXAMPLE 3

# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")

# print("bye")

# EXAMPLE 4

# num = int(input("Enter a # between 1 - 10: "))

# while num < 1 or num > 10: # Things are inside the loop when they are indented
#     print(f"{num} is not valid")
#     num = int(input("Enter a # between 1 - 10: "))

# print(f"Your number is {num}")

###################################################################################################

# # for loops = execurte a block of code a fixed number of times
# you can iterate over a range, string, sequence, etc.

# # regular for loop/ easily prints numbers in 2 lines of code
# for x in range(1, 11):
#     print(x)

# # reversed for loop
# for x in reversed(range(1, 11)):
#     print(x)

# print("HAPPY NEW YEAR!")

# # step count by 2's skips over the 2nd thing
# for x in range(1, 11, 2):
#     print(x)
# # step count by 3's skips over the 3nd thing
# for x in range(1, 11, 3):
#     print(x)

#iterate over a string
# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#     print(x)

# continue/ skips over it
# for x in range(1, 21):
#     if x == 13: # skips 13
#         continue
#     else:
#         print(x)

# for x in range(1, 21):
#     if x == 13 or x == 15 or x == 19: # skips 13, 15, and 19
#         continue
#     else:
#         print(x)

# break/ stops the program at the number
# for x in range(1, 21):
#     if x == 13: 
#         break
#     else:
#         print(x)

#Challenge #1
horror_movies = ["The Exorcist", "The Shining","The Conjuring","The Ring"]
# loop through the list of horror_moviesw
# if the name is "The Shining", print "The Shining"
# otherwise, print "The Shining was not found" 
# and print out the other names using a loop

for movie in horror_movies:
    print(movie)
    if movie == "The Shining":
        print("The Shining was found")
    else:
        print("The Shining was not found")
    

#Challenge #2
# create a list of your favorite horror movie chacrters
# loop through the  list of chacrters
# if the name is "Freddy Krueger", skip over it
# otherwise, print out the name of the chacrater
        
horror_characters = ['Pennywise','Ghostface','Jason Voorhees','Michael Myers','Freddy Krueger']

for characters in horror_characters:
    if characters == "Freddy Krueger":
        continue
    else:
        print(horror_characters)

#Challenge #3
# create a list of your favorite horror movie monsters
# loop throught the list of names
# if the name is , "The Thing", replace it with another name
# otherwise, print our the name of the monster
        
favorite_monster = ["Xenomorph", "Predator", "Shinigami", "The Thing", "Death"]

for i in range(len(favorite_monster)):
    if favorite_monster[i] == "The Thing":
        favorite_monster[i] = "Venom"  # Replacing "The Thing" with "Venom"
    else:
        print(favorite_monster[i])  # Printing the other monsters


