class People:
    def __init__(self,name1,age1,country):
        self.name = name1 # Class Attribute
        self.age = age1
        self.country = country
    
    def say(self):
        print("Hello World!")
    def introduce(self,country):
        print(f"Hi, my name is {self.name}, {self.age} years old. I am from {self.country}")

student1 = People("Lan",20,"Aus","France")

student1.introduce("Australia")
