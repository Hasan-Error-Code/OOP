class Student:
    def __init__(self, *info):
        if len(info) == 3:
            self.name = info[0]
            self.id = info[1]
            self.gpa = info[2]
        elif len(info) == 2:
            self.name = info[0]
            self.id = info[1]
        elif len(info) == 1:
            self.name = info[0]

s1 = Student("Caro", 33, 3.95)
s2 = Student("Bob", 11)
s3 = Student("Mike")
s4 = Student()