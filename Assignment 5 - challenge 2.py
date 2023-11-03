class Calculator:
    def __init__(self):
        pass
    def user_input(self):
        self.num1=float(input("Enter num1 "))
        self.num2=float(input("Enter num2 "))
    def addition(self):
        return self.num1+self.num2
    def substraction(self):
        return self.num1-self.num2
    def multiplication(self):
        return self.num1*self.num2
    def division(self):
        if self.num2==0:
            print("num2 cannot be zero")
        else:
            return self.num1/self.num2
calc = Calculator()
calc.user_input()
print("Addition of num1 and num2 is:",calc.addition())
print("Substraction of num1 and num2 is:",calc.substraction())
print("multiplication of num1 and num2 is:",calc.multiplication())
print("Division of num1 and num2 is:",calc.division())