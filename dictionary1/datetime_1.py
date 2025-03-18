from datetime import datetime, date


# #1: Inform the number of students has its birthday in the next month
# student_birthday = []
# index = 0
# while index < 5:
#     birthDay = input("Enter the birthday of student: ")
#     student_birthday.append(birthDay)
#     index += 1

# bd_count = 0
# for each_Birthday in student_birthday:
#     each_Birthday1 = datetime.strptime(each_Birthday, "%d%m%Y").date()
#     today = date.today()
#     if today.month + 1 == each_Birthday1.month:
#         bd_count += 1
# print(f" The number of students having the birthday in the next month is {bd_count}")

# #2
# t1 = datetime(2018,7,12,12,10,00)
# t2 = datetime(2015,12,23,10,11,9)
# t3 = t1 - t2
# print(t3)

#3
# bd_str = input("Enter your birthday (ddmmYYYY): ")
# bd = datetime.strptime(bd_str, "%d%m%Y").date()

# today = date.today()

# print(bd)
# print(today)
# # a/
# # bd_year = today.year - bd.year
# # print(bd_year)
# # b/
# age = today.year - bd.year
# if today.month < bd.month or (today.month == bd.month and today.day < bd.day):
#     age -= 1
# print(f"You are {age} years old")

#4
str="""
name,age,address,gender,mark,class,teacher
Le Hoang,22012000,Ha Noi,M,10,A2,Alice
Nguyen Ngoc Quynh,21022001,Ho Chi Minh,F,6,A1,Alice
Tran Minh Tuan,21031998,Ha Noi,M,9,A3,Alice
Nguyen Bao Hoang,12022000,Ho Chi Minh,M,8,A1,Mark
Le Van Do,19032002,Ha Noi,M,9,A6,Alice
Do Tan,20082000,Ha Noi,M,7,A7,Mark&Alice
Tran Le Nguyen Anh,12112000,Ho Chi Minh,F,9,A3,Ben
Le Ngoc,02121999,Ha Noi,M,10,A2,Alice
Le Lan,09022001,Ha Noi,M,10,A2,Mark
Le Long,01092002,Ha Noi,M,10,A2,Alice
Pham The Hien,10121999,Ho Chi Minh,F,5,A3,Alice
"""

stu_list = []
str1 = str.strip().split("\n")
print(str1)
for index,item in enumerate(str1):
    if index > 0:
        stu_list.append(item)
print(stu_list)

def highest_number_of_students(stu_list):
    class1 = {}
    for student in stu_list:
        student1 = student.split(",")
        classroom = student1[5]
        if classroom in class1.keys():
            class1[classroom] += 1
        else:
            class1[classroom] = 1
    print(class1)

    m = max(class1, key = class1.get)
    print(f"Class has the most student is {m} with {class1[m]} students")

def most_active_teacher(stu_list):
    teacher1 = {}
    for teacher in stu_list:
        teacher11 = teacher.split(",")
        classroom = teacher11[6]
        if classroom in teacher1.keys():
            teacher1[classroom] += 1
        else:
            teacher1[classroom] = 1
    print(teacher1)

    m = max(teacher1, key = teacher1.get)
    print(f"Teacher who teach most classes is {m} with {teacher1[m]} classes")



