import dispatch
class Calculator:
    

    @dispatch(int)
    def product(self, a):
        print("Number is:",a)
    @dispatch(int, int,)
    def product(self, a, b):
        print("Mul is:", a*b)
    @dispatch(str, str)
    def product(self, a, b):
        print(int(a)*int(b))

n1 = Calculator()
n1.product(5)
n2 = Calculator()
n2.product(5, 6)
