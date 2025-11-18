#Tuples - ordered, homo/hetero, allow duplicaties, indexing, Imutable

cars = ("kia", "Benz", "Audi", "kia")
print(cars, len(cars), type(cars))
# print(cars[1.0]) #Benz
print(cars[-2]) #Audi
a = cars.count("kia")
print(a) #2
b = cars.index("Audi")
print(b)
# cars[0] = "BMW"

stu_info = ("Gamana", 23, 6.8, 4 + 5j, True, 1)
print(stu_info, type(stu_info))
stu_list = list(stu_info)
stu_list[0] = "Nithin"
print(stu_list, type(stu_list))

#Access Elements
nums = (1, 3, 5, 7)
print(nums)

for x in nums:
    print(x)

for y in range(len(nums)):
    print(y)

i = 0
while i < len(nums):
    print(nums[i])
    i = i + 1

#not a tuple
fruits = ("apple")
print(fruits, type(fruits))

# a tuple
fruits = ("apple", ) * 3
print(fruits, type(fruits))