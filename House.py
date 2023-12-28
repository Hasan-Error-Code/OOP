class House:
    def __init__(self):
        self.window = 4
        self.door = 2

    def view(self):
        print("Window:", self.window, "Door:", self.door)
        
h1 = House()
h2 = House()

h1.door = 3
h2.window = 6

print(h1.view())
print(h2.view())