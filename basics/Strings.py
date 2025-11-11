str = '''Shreyas'''
        #01234567
        #-7-6-5-4-3-2-1
print(str[-7])
print(str[-7:2])
print(str[-7:])

str1 = "Hello, World!"
str2 = "Python programming"
str3 = "  hello, python"
str4 = "12345"
str5 = "123Ash"
print(str1.capitalize())  # Capitalizes first letter
print(str2.upper())       # Converts to uppercase
print(str2.title())
print("-".join(["2024","2025","2026"]))  # Joins with hyphen
print(str3.replace("python", "world"))  # Replaces substring
print(str3.strip())
print(str1.encode())
print(str1.split(" ")) 
print(str2.find("programming"))  # Finds substring index
print(str4.isdigit())
print(str3.isdigit()) 
print(str5.isalnum())
print(str2.startswith("Python"))
print(str2.endswith("programming"))

