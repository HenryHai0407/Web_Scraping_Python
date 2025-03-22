class People:
    def __init__(self,name1,age1):
        self.name = name1 # Class Attribute
        self.age = age1
    
    def say(self):
        print("Hello World!")
    def introduce(self,country):
        print(f"Hi, my name is {self.name}, {self.age} years old. I am from {country}")
        # country variables above is located IN def introduce(self,country)
student1 = People("Lan",20)

student1.introduce("Australia")


# -----------

class Student:
    def __init__(self,student_id,surname,first_name,dob,score,class_name,address):
        self.student_id = student_id
        self.surname = surname
        self.first_name = first_name
        self.dob = dob
        self.score = float(score)
        self.class_name = class_name
        self.address = address
    
    def __str__(self):
        return f"{self.first_name} {self.surname} ({self.student_id}) - Score: {self.score}"

# Read student from file
students = []

with open("class_object\student1.txt","r") as f:
    next(f)
    for line in f:
        data = line.strip().split(",") # Split by comma
        student = Student(*data)
        students.append(student)

# for student in students:
#     print(student.__dict__)
# -> Turn the object into a dictionary

top_student = max(students, key = lambda stu: stu.score)
print(f"The student with the highest score is:\n{top_student}")

# ---------------------
# Find the students with a score above 90
high_scorers = [student for student in students if student.score > 90]

for s  in high_scorers:
    print(f"{s.student_id}: {s.first_name} {s.surname} - Score: {s.score}")
print(f"-----------------------------------------")
# -----------------------
# Sort students by score (Descending Order)
sr_students = sorted(students, key = lambda s: s.score, reverse=True)
print(f"Descending order")
for s in sr_students:   
    print(f"{s.student_id}: {s.first_name} {s.surname} - Score: {s.score}")