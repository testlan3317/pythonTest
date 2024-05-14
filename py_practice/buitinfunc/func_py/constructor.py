class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Roll NO.: %d\n Name: %s" % (self.roll_no, self.name))

std1 = Student("Alex", 35)
std2 = Student("Mark", 67)

std1.display()
std2.display()
