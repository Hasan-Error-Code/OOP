class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.price = 0 

    def set_price(self, price):
        self.price = price

    def get_Price(self):
        return self.price
    
    def details(self):
        print("Book Name:", self.name,
              "\nAuthor:", self.author,
              "\nPrice:", self.price, "TK")
        
b1 = Book("Opekkha", "Humayun Ahmed")
b1.price = 540
b1.details()
print(50 * "*")
