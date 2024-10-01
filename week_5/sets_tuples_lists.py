# collections = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# # Set = {} unordered and immuntable, but Add/Remove OK. NO duplicates
# # Tuple = ordered and unchangeable. Duplicates OK. Faster

# fruits = ["apple", "orange", "banana", "coconut", "tomato", "mangao", "watermelon", "grapes"]

# # print(dir(fruits))
# # gives me all the attributes for the list

# # print(help(fruits))
# # gives a manuel of all the things that you can do with lists(gives you helpful documentation)

# # print(len(fruits)) 
# # prints the lenght

# # print("apple" in fruits)
# # tells me if a element is in my list or not

# # fruits[0] = "pineapple"
# # fruits[3] = "lemon"
# # fruits[-1] = "dates"
# # this changes the values

# # fruits.append("pineapple")
# # fruits.append("honeydew_melon")
# # fruits.append("blueberry")
# # adds a element to the end of the list

# # fruits.remove("apple")
# # removes element

# # fruits.insert(0,"kiwi")
# #puts something right there and moves everything over

# # fruits.sort()
# # It orders everything in alphabetical order

# # fruits.reverse()
# # reverse alphabetical order

# # fruits.clear()
# #removes everything

# # fruits.index("apple")
# # print(fruits)

# # print(fruits[::2]) 
# # every second element

# # print(fruits[0]) 
# # prints the relative word

# # print(fruits[::-1]) 
# # makes it backwards


# # for fruit in fruits:
# #     print(fruit)
# # interation. 


# cars = ["Ford", "Volvo", "BMW"]
# # add 4 new cars to the list
# # cars.append("Bugatti")
# # cars.append("Ram")
# # cars.append("Dodge")
# # cars.append("Mitsubishi")
# # # # print out the list of cars in a f-string
# # # # that says "The cars in the list are: "
# # # print(f"The cars in the list are: + {cars}")
# # # # replace the last element in the list with another car
# # # cars[-1] = "Fiat"
# # # # print out the list of cars in an f-string
# # # print(f"The cars in the list are: + {cars}")

# # # # replace the 3rd elemnet in the list with another car
# # # cars[2] = "alfa romeo"
# # # # print out the list of cars in an f-strong
# # # print(f"The cars in the list are: + {cars}")

# # #insert a new care in the 2nd position
# # cars.insert(0,"Maserati")
# # #print out the list of cars in an f-string
# # print(f"The cars in the list are: + {cars}")

# # #remove the 3rd element in the list
# # cars.remove("Volvo")
# # # print out the list of cars in an f-string
# # print(f"The cars in the list are: + {cars}")

# # #check if the list contains "Ford"
# # for car in cars: 
# #     requestCar = input("Enter a car: ")
# #     cars.append(requestCar)
# #     print(f"The cars in the list are: + {cars}")
# #     if len(cars) == 10:
# #         print("You have reached the maximun number of cars.")
# #         break


# # CHALLENGE
# # # create a list of friends
# # friends = ["Pedro"]
# # # add 4 new friends in the list in the list by requesting the user to enter new names
# # for friend in friends:
# #     requestFriend = input(("Enter a friend: "))
# #     friends.append(requestFriend)
# #     if len(friends) == 4:
# #         print(friends)
# #         print(f"The friends in the list are: + {friends}") 
# #         break
# # # print out the list of friends in a f-string
# # print(f"The friends in the list are: + {friends}")
# # # replace the last element in the list with another friend
# # friends[-1] = "Gio"
# # # print out the list of friends in a f-string
# # print(f"The friends in the list are: + {friends}")
# # # replace the 3rd element in the list with another friend
# # friends[2] = "Adrian"
# # # print out the list of friends in a f-string
# # print(f"The friends in the list are: + {friends}")
# # # insert a new friend in the 2nd position
# # friends.insert(1, "Aaliyah")
# # # print out the list of friends in a f-string
# # print(f"The friends in the list are: + {friends}")

# #######################sets#####################
# # sets are unordered and unindexed
# # # they are fefined using curly brackets
# # # the do not allow duplicates
# # fruits = {"apple", "banana", "mango", "cherry", "watermelon"}
# # print(fruits)
# # # print(dir(fruits)) # methods that can be used with sets
# # # print(help(fruits)) # documentation/methods that can be used with sets
# # # print(len(fruits)) # number of elements in the set
# # # print("volvo" in fruits) # checks if the element is in the set

# # #add a element to the set
# # print(fruits.add("orange"))
# # print(fruits)
# # print(fruits.add("kiwi"))
# # print(fruits)

# # # add multiple elements to the set
# # print(fruits.update(["orange", "kiwi", "pineapple"]))
# # print(fruits)

# # # remove an element fromn the set
# # print(fruits.remove("banana"))
# # print(fruits)
# # print(fruits.pop()) # removes the last element of the set
# # print(fruits)
# # print(fruits.clear()) #clears the set
# # print(fruits)
# # # When do we use sets?
# # sets are useful when you want to store a collection of items that should npot changed, and you do not care about the order of the items.
# #example: a collection of unique items
# social_security_numbers = {123456789, 987654321, 113456789}
# # remove the last element in this set
# print(social_security_numbers.pop())
# # add another social security number
# print(social_security_numbers.add(512349876))
# print(social_security_numbers)
# print(social_security_numbers.add(512649876))
# print(social_security_numbers)

# # ###################TUPLES####################
# # # tuples are immutable and are defined using parenthesis
# # # Create a tuple called mp_tuple with the following values
# my_tuple = (1,2,3,4,5,6,7,8,10)
# # print(my_tuple)
# # print(my_tuple.count(2)) # count the number of times it shows up
# # # thw value 2 appears in the tuple
# # print(dir(my_tuple)) # methods that can be used with tuples
# # print(help(my_tuple)) # documentation/methods that can be used with tuples
# # print(len(my_tuple)) # number of elements in the tuple
# # print( 2 in my_tuple) # check if the element is in the tuple
# # # When are tuples useful?
# # # Tuples are used when you want to store a collection of items that should not be changed, such as days of the week, months of the year, etc.
# # # if you wnat to find the index of a value in a tuple
# # print(my_tuple.index(2))
# # lymeric = " peter piper picked a peck of pickled peppers"
# # # convert the string into a tuple
# # # split it first
# # lymeric_tuple = tuple(lymeric.split())
# # print(lymeric_tuple)
# # # find how many times the word "peppers" appears in the table


# #loops with tuples
# for item in my_tuple:
#     print(item) # prints each number individually

###########################DICTIONARIES#########

# dictionaries are unordered, changeable and indexed
# they are defined using curly brackets
# they haves keys and values
# a collective of (key:values) pairs, no duplicates
# keys are unique
# values can be of any data type
capitals = {"Kenya":"Nairobi",
            "Uganda":"Kampala",
            "Tanzania":"Dodoma",
            "Rwanda":"Kigali",
            "China":"Beijing",
            "USA":"Washington DC"}
# print(capitals)
# print(dir(capitals)) # attributes that can be used with dictionaries
# print(help(capitals)) # documentation/methods that can bve used with dictionaries
# print(len(capitals)) # number of items in the dictionary 

#if you want to check the value of a key in a dictionary
print(capitals["Kenya"])
print(capitals.get("Kenya"))
# add an item to the dictionary # two ways
capitals["South Africa"] = "Pretoria"
print(capitals)

capitals.update({"Nigeria":"Abuja"})
# add three more countries and their capitals to the dictionary
capitals.update({"Russia":"Moscow"})
capitals.update({"France":"Paris"})
capitals.update({"Japan":"Tokyo"})
print(capitals)



capitals.pop("China") # removes and item ffrom the dictionary
print(capitals)
#clear the dictionary
# capitals.clear() # do not run this
# loop through the dictionary
for key in capitals:
    print(f"these are now the {key}")

# print the value in the dictionary
for value in capitals.values():
    print(value)

# print the key value pairs in the dictioanry
items_all = capitals.items() # the key value pairs
for key, value in items_all:
    print(f"{key} is the capitol of {value}")

