# class Got:
#     def __init__(self, color, action):
#         self.color = color
#         self.action = action
#         self.eat = ""

#     def view(self, compier):
#         print("The", self.color, "Got is", self.action, "now")
#         print(compier)

#     def compier(self, ct):
#         if ct.action == self.action:
#             print("Both are", self.action)
#         else:
#             print("The are different")

# g1 = Got("black", "jumping")
# g2 = Got("Brown", "siting")
# g3 = Got("green", "jumping")

# g1.compier()

class Cat:
    def __init__(self, color, action):
        self.color = color
        self.action = action
    def view(self):
        print(self.color, "cat is", self.action)

    def compier(self, ct):
        if self.action == ct.action:
            print("Both cat are", self.action)
        else:
            print("They are diffrent")

c1 = Cat("White", "Humping")
c2 = Cat("Brown", "Sitting")

c1.view()
c2.view()
c1.compier(c2)