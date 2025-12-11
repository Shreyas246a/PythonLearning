def divide(a,b):
    res = a / b
    return res

try:
    result = divide(10, 0)
    print("Result:", result)
except ZeroDivisionError or Exception:
    print("Error: Division by zero is not allowed.")



class AgeException(Exception):
    def __init__(self, *args):
        super().__init__(*args)

def age_check(age):
    if age < 0:
        raise AgeException("Age cannot be negative.")
    return True

try:
    age = -5
    age_check(age)
except AgeException as e:
    print("AgeException:", e)
