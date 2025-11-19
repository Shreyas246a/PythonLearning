list1 = list([1,2,3,4,5])
list2 = [num*2 for num in list1]
print(list2)

sum = 0
for i in list1:
    sum += i
print(sum)