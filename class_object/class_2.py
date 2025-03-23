class People:
    def __init__(self,name1,age1):
        self.name = name1 # Class Attribute
        self.age = age1
    
    def say(self):
        print("Hello World!")
    def introduce(self,country):
        print(f"Hi, my name is {self.name}, {self.age} years old. I am from {country}")
        # country variables above is located IN def introduce(self,country)
# student1 = People("Lan",20)
# student1.introduce("Vietnam")

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

# top_student = max(students, key = lambda stu: stu.score)
# print(f"The student with the highest score is:\n{top_student}")

# # ---------------------
# # Find the students with a score above 90
# high_scorers = [student for student in students if student.score > 90]

# for s  in high_scorers:
#     print(f"{s.student_id}: {s.first_name} {s.surname} - Score: {s.score}")
# print(f"-----------------------------------------")
# # -----------------------
# # Sort students by score (Descending Order)
# sr_students = sorted(students, key = lambda s: s.score, reverse=True)
# print(f"Descending order")
# for s in sr_students:   
#     print(f"{s.student_id}: {s.first_name} {s.surname} - Score: {s.score}")

class Teacher:
    def __init__(self,class_name,class_type,teacher):
        self.class_name = class_name
        self.class_type = class_type
        self.teacher = teacher
    
    def __str__(self):
        return f"Teacher {self.teacher} in charges of {self.class_name} - {self.class_type}"

teachers = []
with open("class_object\classid.txt","r") as f1:
    next(f1)
    for line1 in f1:
        data = line1.strip().split(",")
        teacher = Teacher(*data)
        teachers.append(teacher)

## ------------------------------------------------------------
# Step 1: Calculate the average score for each class
from collections import defaultdict
class_scores = defaultdict(list)

for student in students:
    class_scores[student.class_name].append(student.score)

class_avg_scores = {class_name: sum(scores)/len(scores) for class_name, scores in class_scores.items()}

# Step 2: Map class scores to teachers
teacher_scores = []
for teacher in teachers:
    if teacher.class_name in class_avg_scores:
        avg_score = class_avg_scores[teacher.class_name]
        teacher_scores.append((teacher.teacher, teacher.class_name, avg_score))

# Step 3: Sort by highest average score and get top 3 teacher
top_teachers = sorted(teacher_scores,key =lambda x: x[2],reverse=True)[:3]
# Step 4: Print results
print("\nTop 3 Teachers with Highest Average Student Score:")
for rank, (teacher_name, class_name, avg_score) in enumerate(top_teachers, 1):
    print(f"{rank}. {teacher_name} (Class: {class_name}) - Avg Score: {avg_score:.2f}")

## =========
# Task 3:
teachers_info = []
class Teacher_Info:
    def __init__(self,teacher,teacher_surname,teacher_firstname,teacher_dateofbirth,teacher_address):
        self.teacher = teacher
        self.teacher_surname = teacher_surname
        self.teacher_firstname = teacher_firstname
        self.teacher_dateofbirth = teacher_dateofbirth
        self.teacher_address = teacher_address
    
    def __str__(self):
        return f"{self.teacher} has a full name of {self.teacher_firstname} {self.teacher_surname}, birthing in {self.teacher_dateofbirth} and living in {self.teacher_address}"

with open("class_object\\teacherid.txt","r") as f3:
    next(f3)
    for line2 in f3:
        data = line2.strip().split(",")
        t_i = Teacher_Info(*data)
        teachers_info.append(t_i)  

# Count the number of students in each class
class_dict = {}
for student in students:
    if student.class_name in class_dict.keys():
        class_dict[student.class_name] += 1
    else:
        class_dict[student.class_name] = 1

teacher_class = []
for teacher in teachers:
    if teacher.class_name in class_dict.keys():
        teacher_class.append((teacher.teacher, teacher.class_name,class_dict[teacher.class_name]))

print(teacher_class)
# Teacher with its number of students
task2 = {}
for t in teacher_class:
    if t[0] in task2:
        task2[t[0]] += t[2]
    else:
        task2[t[0]] = t[2]
print(task2)

# Teacher with its number of class and that teacher doesn't teach more than 3 classes
task3 = {}
for t in teacher_class:
    if t[0] in task3:
        task3[t[0]] += 1
    else:
        task3[t[0]] = 1
print(task3)

for k,v in task3.items():
    if v < 3:
        print(f"Teacher {k} has {task2[k]} students")

