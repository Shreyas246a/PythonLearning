# Write a program to check if a given number is positive.
# If it is positive, print "Positive number".
from re import match


num = 10
if num > 0:
    print("Positive number")

#Write a program to check if a student has passed an exam.
# Passing marks = 40
marks = 55
if marks >=40:
    print("Passed the exam")
else:
    print("Failed the exam")

#Write a program to check whether a number is even or odd.

num=2
if(num%2!=0):
    print("Odd")
else:
    print("Even")

#Write a program to check whether a person is eligible to vote.
# (Eligible if age >= 18)
age = 17
if(age>=18):
    print("Eligible to vote")
else:
    print("Not eligible to vote")
#Write a program to check whether a number is positive or negative.

# Write a program to determine the grade of a student based on marks.
# 90 and above -> A
# 75 to 89 -> B
# 60 to 74 -> C
# below 60 -> Fail

stmarks = 66

if(stmarks >= 90):
    print("Grade A")
elif(stmarks >= 75):
    print("Grade B")
elif(stmarks >= 60):
    print("Grade C")
else:
    print("Fail")

#Write a program to determine the type of triangle based on sides.
# All sides equal → Equilateral
# Two sides equal → Isosceles
# All sides different → Scalene


#Write a program to display the largest of three numbers.
print("Largest of three numbers")
x = int(input("Enter first number: "))
y = int(input("Enter first number: "))
z = int(input("Enter first number: "))

if(x>y & x>z):
    print("Largest is ", x)
elif(y>z & y>x):
    print("Largest is ", y)
else:
    print("Largest is ", z)

#Nested If
#Write a program to check if a number is positive.
# If it’s positive, then check if it’s even or odd.
print()
print("Check Positive, Even, Odd")
num2 = 8
if(num2 >0):
    if(num2%2==0):
        print("Even")
    else:
        print("Odd")
else:
    print("Negative Number")

#Write a program that checks if the username is "admin".
# If yes, then check if the password is "1234".
# If both match, print "Login Successful".
# Otherwise, print appropriate messages.
print()
username = "admin"
password = "1234"
if(username is "admin"):
    if(password is "1234"):
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Incorrect Username")

#Switch
#Write a program to display the day of the week using numbers.
# 1 → Monday, 2 → Tuesday, ..., 7 → Sunday
day = 3
print();
print("Day of the week is: ", end="")
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")    


# Write a program that displays messages based on user input:
# 'a' → "Add"
# 'b' → "Browse"
# 'c' → "Cancel"
# anything else → "Invalid option"

match 'a':
    case 'a':
        print("Add")
    case 'b':
        print("Browse")
    case 'c':
        print("Cancel")
    case _:
        print("Invalid option")



# Practice Questions on for loop, while loop, nested loops,
# and loop control statements.
# ===============================================

# -------------------------------
# FOR LOOP
# -------------------------------

# Q1: Write a program to print numbers from 1 to 5 using a for loop.
for i in range(1,6):
    print(i)
arr = [10, 20, 30, 40, 50]
# Q2: Write a program to print even numbers between 1 and 10.

for i in range(1, 11):
    if(i%2==0):
        print(i,end=" ")
# Q3: Write a program to print the square of numbers from 1 to 5.
for i in range(1, 6):
    print(i**2,end=" ")
# Q4: Write a program to display the multiplication table of a number.
print("Multiplication Table")
num = 5
for i in range(1, 11):
    print(num, "*", i, "=", num*i)

# -------------------------------
# WHILE LOOP
# -------------------------------

# Q5: Write a program to print numbers from 1 to 5 using a while loop.

# Q6: Write a program to find the sum of first 10 natural numbers.

# Q7: Write a program to print numbers from 10 down to 1 using a while loop.

# Q8: Write a program to count the number of digits in a given number.


# -------------------------------
# NESTED LOOP
# -------------------------------

# Q9: Write a program to print the following pattern using nested for loops:
# Output:
# *
# * *
# * * *

# Q10: Write a program to print the multiplication table for numbers 1 to 3.


# -------------------------------
# LOOP CONTROL STATEMENTS
# -------------------------------

# Q11: Write a program that prints numbers from 1 to 10,
# but stops when it reaches 6 using break.

# Q12: Write a program that prints numbers from 1 to 10,
# but skips printing 5 using continue.

# Q13: Write a program using pass inside a loop.
# (Print numbers greater than 3, do nothing for numbers <= 3.)


# -------------------------------
# REAL-LIFE EXAMPLES
# -------------------------------

# Q14: Write a program to find the factorial of a number using a loop.

# Q15: Write a program to reverse a number using a while loop.
