import threading,time

def print1(list1):
    for i in list1:
        print(i)


def print1(list2):
    for i in list2:
        print(i)
        time.sleep(1)


list1 = [1,2,3,4,5]
list2 = ['A','B','C','D','E']

t1 = threading.Thread(target=print1,args=(list1,))
t1.setDaemon(True)
t2 = threading.Thread(target=print1,args=(list2,))
t1.start()
t2.start()