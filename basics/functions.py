# No arguments + No return value
def sqr():
    num = 1
    print(num * num)

sqr() #1

# No arguments + return value
def sqr():
    num = 2
    return num * num

print(sqr()) #4

# arguments + no return value
def sqr(num):
    print(num * num)

sqr(3) #9

# arguments + return value
def sqr(num):
    return num * num

res = sqr(10)
print(res) #100