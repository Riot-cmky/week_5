# Exercise 1: Simple Conditional

lang = input('What is your favorite programming language?: ')

if lang == 'Python': 
    print('You love Python! ')
else:
    print('Different choice')

# Exercise 2: Grading System
    
grade = input('Enter a score: ')

if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
        print('C')
elif grade >= 60:
    print('D')
else:
    print('F')
     

# Exercise 3: Admin Login

user = 'Admin'
logged_in = False

if user == 'Admin' or logged_in:
    print("Welcome admin! ")
elif user == "Admin" and logged_in:
    print('Please Log In')

# Exercise 4: Object Identify Check

a = [1,5,7]
b = a

print(id(a))
print(id(b))
print(a is b)