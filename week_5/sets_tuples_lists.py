# collections = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immuntable, but Add/Remove OK. NO duplicates
# Tuple = ordered and unchangeable. Duplicates OK. Faster

fruits = ["apple", "orange", "banana", "coconut", "tomato", "mangao", "watermelon", "grapes"]

# print(dir(fruits))
# gives me all the attributes for the list

# print(help(fruits))
# gives a manuel of all the things that you can do with lists(gives you helpful documentation)

# print(len(fruits)) 
# prints the lenght

# print("apple" in fruits)
# tells me if a element is in my list or not

# fruits[0] = "pineapple"
# fruits[3] = "lemon"
# fruits[-1] = "dates"
# this changes the values

# fruits.append("pineapple")
# fruits.append("honeydew_melon")
# fruits.append("blueberry")
# adds a element to the end of the list

# fruits.remove("apple")
# removes element

# fruits.insert(0,"kiwi")
#puts something right there and moves everything over

# fruits.sort()
# It orders everything in alphabetical order

# fruits.reverse()
# reverse alphabetical order

# fruits.clear()
#removes everything

# fruits.index("apple")
# print(fruits)

# print(fruits[::2]) 
# every second element

# print(fruits[0]) 
# prints the relative word

# print(fruits[::-1]) 
# makes it backwards


# for fruit in fruits:
#     print(fruit)
# interation. 


cars = ["Ford", "Volvo", "BMW"]
# add 4 new cars to the list
# cars.append("Bugatti")
# cars.append("Ram")
# cars.append("Dodge")
# cars.append("Mitsubishi")
# # # print out the list of cars in a f-string
# # # that says "The cars in the list are: "
# # print(f"The cars in the list are: + {cars}")
# # # replace the last element in the list with another car
# # cars[-1] = "Fiat"
# # # print out the list of cars in an f-string
# # print(f"The cars in the list are: + {cars}")

# # # replace the 3rd elemnet in the list with another car
# # cars[2] = "alfa romeo"
# # # print out the list of cars in an f-strong
# # print(f"The cars in the list are: + {cars}")

# #insert a new care in the 2nd position
# cars.insert(0,"Maserati")
# #print out the list of cars in an f-string
# print(f"The cars in the list are: + {cars}")

# #remove the 3rd element in the list
# cars.remove("Volvo")
# # print out the list of cars in an f-string
# print(f"The cars in the list are: + {cars}")

# #check if the list contains "Ford"
# for car in cars: 
#     requestCar = input("Enter a car: ")
#     cars.append(requestCar)
#     print(f"The cars in the list are: + {cars}")
#     if len(cars) == 10:
#         print("You have reached the maximun number of cars.")
#         break


# CHALLENGE
# create a list of friends
friends = ["Pedro"]
# add 4 new friends in the list in the list by requesting the user to enter new names
for friend in friends:
    requestFriend = input(("Enter a friend: "))
    friends.append(requestFriend)
    if len(friends) == 4:
        print(friends)
        print(f"The friends in the list are: + {friends}")
        break
# print out the list of friends in a f-string

# replace the last element in the list with another friend
friends[-1] = "Gio"
# print out the list of friends in a f-string
print(f"The friends in the list are: + {friends}")
# replace the 3rd element in the list with another friend
friends[2] = "Adrian"
# print out the list of friends in a f-string
print(f"The friends in the list are: + {friends}")
# insert a new friend in the 2nd position
friends.insert(1, "Aaliyah")
# print out the list of friends in a f-string
print(f"The friends in the list are: + {friends}")
