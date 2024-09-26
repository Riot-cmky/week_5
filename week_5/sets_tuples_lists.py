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

fruits.remove("apple")
# removes element

fruits.insert(0,"kiwi")
#puts something right there and moves everything over

fruits.sort()
# It orders everything in alphabetical order

fruits.reverse()
# reverse alphabetical order

fruits.clear()
#removes everything

fruits.index("apple")
print(fruits)

# print(fruits[::2]) 
# every second element

# print(fruits[0]) 
# prints the relative word

# print(fruits[::-1]) 
# makes it backwards


# for fruit in fruits:
#     print(fruit)
# interation. 


