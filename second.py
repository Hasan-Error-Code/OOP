class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def details(self):
        print("Name:", self.name, "ID:", self.id)

s1 = Student("Hasan", 121)
s2 = Student("Habiba", 123)
s3 = Student("Shanaz", 124)

# print("Name:", s1.name, "ID:", s1.id)
# print("Name:", s2.name, "ID:", s2.id)

print(s1.details())
print(s2.details())
print(s3.details())