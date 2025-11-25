stu_info = {
    "name":"Shreyas",
    "ID" : 92,
    "course" : "CSE"
}
print(stu_info)
print(stu_info["course"])
print(stu_info["name"])
print(stu_info["ID"])


stu_info["course"] = "Data Science"
print(stu_info) 

stu_info["age"] = 21
print(stu_info) 
del stu_info["age"]
print(stu_info)
stu_info.popitem() #deletes last item
print(stu_info)
#length
print(len(stu_info))
print(stu_info.__len__())

print(stu_info.keys())
print(stu_info.values())
print(stu_info.get("name"))


stu_set = set(stu_info.items())
print(stu_set)  # Accessing first item of the set"])


list1 = []
list2 = list()
print(type(list1))
print(list1.__len__())
print(type(list2))
print(list2.__len__())

print()

tup = ()
tup2 = tuple()
tup3 = tuple([12,2,3,41,5])
print(type(tup))
print(tup.__len__())
print(type(tup2))
print(tup2.__len__())
print(type(tup3))
print(tup3.__len__())
print(tup3)

for i in tup3:
    print(i)


set1 = set()
set2 ={}
set3 = set(["ABCDEF"])
print(type(set1))
print(set1.__len__())
print(type(set2))
print(set2.__len__())
print(type(set3))
print(set3.__len__())
print(set3)
print(sorted(set3))


dict1 = {}
dict2 = dict()
dict3 = dict([("name","Shreyas"),("ID",92),("course","CSE")])
print(type(dict1))
print(dict1.__len__())
print(type(dict2))
print(dict2.__len__())
print(type(dict3))
print(dict3.__len__())
print(dict3)


for item in dict3.items():
    print(item[0]+ " " +str(item[1]))