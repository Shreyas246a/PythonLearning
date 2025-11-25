class Mentor:
    def define_states(self):
        self.name = "Shreyas"
        self.subject = "CSE"
        self.experience = 5
    def __init__(self):
        self.name = "Default Name"
        self.subject = "Default Subject"
        self.experience = 0

    def display_states(self):
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")
        print(f"Experience: {self.experience} years")

mentor1 = Mentor()
#mentor1.define_states()
mentor1.display_states()
print(mentor1.name)
print(mentor1.subject)
print(mentor1.experience)