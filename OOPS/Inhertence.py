

#Single Inheritance Example
class Employee:
    def __init__(self,eid,ename,salary,company):
        self.eid=eid
        self.ename=ename
        self.salary=salary
        self.company=company

    def display(self):
        print(f"ID: {self.eid}, Name: {self.ename}, Salary: {self.salary}, Company: {self.company}")
    
class Developer(Employee):
    def skills(self):
        print(f"{self.ename} knows Python, JavaScript, HTML, CSS")
    def coding(self):
        print(f"{self.ename} is coding...")

class Tester(Employee):
    def testing_tools(self):
        print(f"{self.ename} knows Selenium, JMeter, Postman")
    def testing(self):
        print(f"{self.ename} is testing...")

dev1 = Developer(101,"Shreyas",75000,"techCorp")
dev1.display()
dev1.skills()
dev1.coding()

print()

tester1 = Tester(201,"Anika",65000,"softSolutions")
tester1.display()
tester1.testing_tools()
tester1.testing()


#multiple Inheritance Example

class A:
    def method(self):
        print("Method A from class A")
class B(A):
   # def method(self):
    #    print("Method B from class B")
    pass

class C(B,A):
    pass

obj = C()
print(obj.mro())  # Method A from class A