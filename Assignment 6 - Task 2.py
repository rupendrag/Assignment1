class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def getInfo(self):
        print(f"{self.name} has a {self.coat_color} coat.")

class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, hunting_skill):
        super().__init__(name, age, coat_color)
        self.hunting_skill = hunting_skill

    def specialSkill(self):
        print(f"{self.name} has a special hunting skill: {self.hunting_skill}")

class Bulldog(Dog):
    def __init__(self, name, age, coat_color, strength):
        super().__init__(name, age, coat_color)
        self.strength = strength

    def showStrength(self):
        print(f"{self.name} is known for its strength. Strength level: {self.strength}")

dog1 = Dog("Rex", 5, "Brown")
dog2 = Dog("Luna", 3, "Black")

terrier = JackRussellTerrier("Buddy", 2, "White with brown spots", "Excellent digging")

bulldog = Bulldog("Max", 4, "Brindle", "High")

dog1.description()
dog1.getInfo()

dog2.description()
dog2.getInfo()

terrier.description()
terrier.getInfo()
terrier.specialSkill()

bulldog.description()
bulldog.getInfo()
bulldog.showStrength()