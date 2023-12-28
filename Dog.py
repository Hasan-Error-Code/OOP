class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def update_color(self, color):
        self.color = color

    def poke(self):
        #print(f"{self.color, self.name},is smiling")
        print(self.color, self.name, "is smiling")
    
d1 = Dog("Rover", "Brown")
d2 = Dog("Tomy", "White")
d2.color = "Red"
d1.poke()
d2.poke()

print(d1.__dict__)
print(dir(d1))