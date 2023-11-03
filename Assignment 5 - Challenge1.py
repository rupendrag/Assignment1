class point:
    def __init__(self):
        pass
    def user_input(self):
        self.x = float(input("Enter 1st Number"))
        self.y = float(input("Enter 2nd Number"))
        self.z = float(input("Enter 3rd Number"))
    def SqSum(self):
        sqx = self.x**2
        sqy = self.y**2
        sqz = self.z**2
        return sqx+sqy+sqz
    
given_num = point()
given_num.user_input()
result = given_num.SqSum()
print(result)