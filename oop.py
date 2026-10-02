class student:
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def display(self):
        print("name:", self.name)
        print("age:", self.age)
        print("roll number:", self.roll_no)
        return " "
s1 = student("ram", 21, 101)
s2 = student("shyam", 23, 102)
print(s1.display())
print(s2.display())






