# Question 4: Fitness Program Eligibility

# Ask user for requirements

age = input("What is your age? ")
gender = input("Are you male(M) or female(F)? ")
current_member = input("Are you a current memeber (Y or N)? ")

#Use the if conditions to determine if they have eligibility by asking for age, gender, and if they are a current member

# Age has to be between 18 and 30, can be either F or M, and has to be a current member
# I knew that my variable current_member always has to be equal to Y all I had to do was write to if conditionals

if age >= "18" and age <= "30":
    if gender == "F" and current_member == "Y":
        print("Eligible for the Women's Beginnger Program.")
    if gender == "M" and current_member == "Y":
        print("Eligible for the Men's Beginner Program.")

# Age has to be between 31 and 40, doesn't include gender, but does include the current member status
# I know that gender doesn't affect this set of conditionals so it wasn't necessary to include but you either had to be a current member or not
        
if age >= "31" and age <= "50":
    if current_member == "Y":
        print("Eligible for the Adult Fitness Program.")
    else:
        print("Membership required for Adult Fitness Program.")

# Age has to be over 50, doesn't include gender, and neither does it include current memeber status
# I had to simply just use the camparsion operators and then print out the response
        
if age > "50":
    print("Eligible for Senior Wellness Program.")


# Question 2: Admission to a Competitive Propgram

# Asking user for their score
score = input("What is your score out of 100? ")
# Asking user for their gpa
gpa = input("What is your gpa? ")
#Asking the user if the take extracurricular activities
extra = input("Do you take extracurricular activites? (Y or N) ")

# The score has to be 90 or above and the gpa has to be 3.5 and above to display that they qualify.
# Extracurriculars are not needed
if score >= "90":
    if gpa >= "3.5":
        print("You qualify for admission!")

# The person needs to have a score of 80 or higher, extracurriculars, and a gpa of 3.0 or greater. 
# If they do not meet these rerquirements they will be presented with message that says they do not qualify.
if score >= "80":
    if gpa >= "3.0" and extra == "Y":
        print("You qualify for admission withe extracurriculars.")
    if gpa < "3.0" and extra == "Y":
        print("You need a higher gpa to qualify with extracurriculars")
    else:
        print('Unfortunately, you do not qualify.')



    
    