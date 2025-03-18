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

#2
t1 = datetime(2018,7,12,12,10,00)
t2 = datetime(2015,12,23,10,11,9)
t3 = t1 - t2
print(t3)