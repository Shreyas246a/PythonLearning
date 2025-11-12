
def greet_user(name,city,age):
    print(f"Hello, {name}! You are {age} years old and live in {city}.")


greet_user("Alice","New York",30)   
greet_user("Bob","Los Angeles",25)
greet_user("Charlie","Chicago",35)


def area_of_rectangle(length=1, width=1):
    return length * width

input_length = float(input("Enter the length of the rectangle: "))
input_width = float(input("Enter the width of the rectangle: "))
area = area_of_rectangle(input_length, input_width)
print(f"The area of the rectangle is: {area}")