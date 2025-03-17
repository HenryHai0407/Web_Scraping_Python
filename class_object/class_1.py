class Student:
    # class Attribute
    def __init__(self,name,age):
        self.name = name # instance Attribute
        self.age = age
    def introduce1(self):
        print(f"Name: {self.name}, Age: {self.age}")
    



if __name__ == "__main__":
    student1 = Student("Tuan",12)
    student1.introduce1()
