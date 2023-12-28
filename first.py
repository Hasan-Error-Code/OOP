"""Class object Constructor attributes methods()"""
class Student:
    def __init__(self, name, Id):
        self.name = name
        self.id = Id
        # print("a student object created")

# variable = class_name
s1 = Student("Hasan", 14)
s2 = Student("Habiba", 12)
s1.id = 41
print(s2.name, s2.id)
print(s1.name, s1.id)