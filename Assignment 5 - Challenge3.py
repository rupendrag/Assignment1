class Student:
    def _init_(self):
        self.__name = None
        self.__roll_number = None
    def getName(self):
        return self.__name
    def getRollNumber(self):
        return self.__roll_number
    def setName(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError("Invalid input for name. Name must be a string.")
        
    def setRollNumber(self, roll_number):
        if isinstance(roll_number, str):
            self.__roll_number = roll_number
        else:
            raise ValueError("Invalid input for roll number. Roll number must be a string.")

student = Student()

try:
    name = input("Enter Students name ")
    student.setName("Rupendra")
    roll_number=input("Enter Roll number")
    student.setRollNumber("123456")

    print(f"Name: {student.getName()}")
    print(f"Roll Number: {student.getRollNumber()}")
except ValueError as e:
    print(e)
