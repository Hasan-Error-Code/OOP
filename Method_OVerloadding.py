class Calculator:
    def product(self, num1, num2 = None, num3 = None):
        if num1 != None and num2 != None and num3 != None:
            print("num1 * num2 * num3:",num1 * num2 * num3) 
        else:
            print("num1 * num2:",num1 * num2)


c1 = Calculator()
c1.product(4, 6, 7)
c2 = Calculator()
c2.product(2, 8)