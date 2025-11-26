class Student:
    company = "ABC School"
    #constructor
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    #instance method
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}, School: {self.company}"   
    #class method
    @classmethod
    @staticmethod
    def change_company(cls, new_company):
        cls.company = new_company
    

s1 = Student("Alice", 14, "8th")
s2 = Student("Bob", 15, "9th")
print(s1.get_details())
Student.change_company("XYZ School")
print(s2.get_details(),Student.company)