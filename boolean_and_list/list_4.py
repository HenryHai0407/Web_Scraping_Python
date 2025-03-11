# par = input("Enter the paragraph: ")
# taboo_list =["hate","damn"]
# par1 = par.split()
# for word in par1:
#     if word in taboo_list:
#         par2 = par.replace(word,"****")
# print(par2)


# Given a list that has full name of 20 students, find the most common surname
# name_list = []
# sur_list = []
# idx = 0
# while idx < 20:
#     par = input("Enter a name: ")
#     if type(par) == str:
#         idx += 1
#         name_list.append(par)
# print(name_list)
# # Extract surname list
# for name in name_list:
#     name1 = name[:name.find(" ")]
#     sur_list.append(name1)
# print(sur_list)
# # Create f and dict to append key-value pairs
# f = {}
# for num in sur_list:
#     f[num] = f.get(num,0) + 1
# m = max(f, key = f.get)
# print(f"The most frequent surname appearing in the list is: {m}")


# Given a following list, find a numerical order of student who has a highest score in the list
ds = """
Nguyen Van Nam, 9
Tran Minh, 8
Tran Van Anh, 10
Tran Quang, 9
Nguyen Hai, 10
Tran Lan, 11
"""
ds_list = ds.strip().split("\n")
name_max = []
score_max = -1 
# 1st solution
# for item in ds_list:
#     name, score = item.rsplit(", ",1)
#     score = int(score)
#     if score > score_max:
#         name_max = [name]
#         score_max = score
#     elif score == score_max:
#         name_max.append(name)

# print(f"The student(s) {', '.join(name_max)} has/have the highest score with {score_max}")

# 2nd solution
student_data = []
for index, item in enumerate(ds_list,start=1):
    name, score = item.rsplit(", ",1)
    score = int(score)
    student_data.append((index,name,score))

    if score > score_max:
        name_max = [(index,name)]
        score_max = score
    elif score == score_max:
        name_max.append((index,name))
print(student_data)
print("Student list in numerical order")
for idx, name, score in student_data:
    print(f"{idx}.{name} - {score}")

top_score = ", ".join([f"{idx}.{name}" for idx,name in name_max])
print(f"\nThe student(s) with highest score: {top_score} with {score_max} points")
