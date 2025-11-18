list_1 = [1, 2,2,4,1,2,4,67, 5]

list_1.sort()
print(list_1)  # [1, 1, 2, 2, 2, 4, 4, 5, 67]
print(3 in list_1)      # True
print(6 not in list_1)  # True  

print(list_1[1:4])# [1, 2, 2]
print(list_1[-3:])# [4, 5, 67]
print(list_1[1:7:2])# [1, 2, 4]