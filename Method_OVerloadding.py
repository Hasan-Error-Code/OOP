class Calculator:
    def product(self, num1, num2 = None, num3 = None):
        if num1 != None and num2 != None and num3 != None:
            print(num1 * num2 * num3) 


c1 = Calculator()
c1.product(4, 6, 7)