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