#Imutability

str1 = "Hello"
print(id(str1))
str2 = str1 + ", World!" # Creates a new string
str3 = str1;
print(id(str3))
print(id(str2))
print(str1 is str3);
