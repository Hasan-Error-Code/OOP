"""Class object Constructor attributes methods()"""
class Student:
    def __init__(self, name, Id):
        self.name = name
        self.id = Id
        # print("a student object created")

# variable = class_name
s1 = Student("Hasan", 14654)
s2 = Student("Habiba", 1234)

print(s2.name)
print(s1.name)