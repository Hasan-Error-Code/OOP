class Cat:
    def __init__(self, color, action):
        self.color = color
        self.action = action
        self.eat = ""
    def view(self):
        print(self.color, "cat is",self.action, self.eat)

c1 = Cat("White", "jumping")
c2 = Cat("Black", "seting")

print("Befor update: Result")
c1.view()
c2.view()
print("After update: Result")
c1.eat = "and eat Big Fish"
c2.eat = "and eat Small Fish"
c1.view()
c2.view()
