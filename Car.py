class Car:

    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.wheel = 4

    def view(self):
        print(f"The model year of this {self.name}, is {self.model}.")
        print(f"It is a {self.wheel} wheel car.")
c1 = Car("BMW", 2016)
c2 = Car("Audi", 2018)

print(c1.view())