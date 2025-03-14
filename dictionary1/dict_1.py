dict_1 = {
    "name": "Tan Do",
    "age": 20,
    "class": "Python"
}

# for k,v in dict_1.items():
#     print(k,v)

# dict_2 = [(k,v) for k,v in dict_1.items()]
# print(dict_2)

# for key in dict_1:
#     print(key, ":",dict_1[key])

# print("\n".join(map(lambda kv: f" {kv[0]}: {kv[1]}", dict_1.items())))

students = [
    {"name": "Le Hoang", "age": 20},
    {"name": "Nguyen Hoang", "age": 22},
    {"name": "Tran Le", "age": 21},
    {"name": "Bui Pham Minh Anh", "age": 23},
    {"name": "Le Van Do", "age": 24},
    {"name": "Le Van Do", "age": 23},
    {"name": "Tran Le Thanh Tuan", "age": 22},
    {"name": "Le Minh Thanh", "age": 20},
    {"name": "Nguyen Ly Tien", "age": 27},
    {"name": "Bui Chau", "age": 26},
    {"name": "Tran Hoang Lan", "age": 21},
    {"name": "Hoang Ngoc", "age": 23},
    {"name": "Hoang Ngoc", "age": 23},
    {"name": "Hoang Ngoc", "age": 23},
    {"name": "Hoang Ngoc", "age": 23},
]
#3
def find_students_having_the_same_age(students):
    age_group = {}
    for student in students:
        age = student["age"]
        if age in age_group:
            age_group[age].append(student)
        else:
            age_group[age] = [student]

    duplicate_ages = {age: group for age, group in age_group.items() if len(group) > 1}
    print(duplicate_ages)

    for age, separated_group in duplicate_ages.items():
        print(f"For the group has age {age}: ")
        for sli in separated_group:
            print(f"{sli['name']}")

# find_students_having_the_same_age(students)

#2: average age
def find_average_age(students):
    age_list = []
    for student in students:
        age = student["age"]
        age_list.append(age)
    age_avg = int(round(sum(age_list)/len(age_list),0))
    # print(f" Average age of students in the class is {age_avg}")
    age_groups = {}
    for student in students:
        age = student["age"]
        if age in age_groups:
            age_groups[age].append(student)
        else:
            age_groups[age] = [student]
    avg_age_group = [v for k,v in age_groups.items() if age_avg == k]
    print(f"Students who have the same age with the average age ({age_avg}) are: ")
    for item in avg_age_group:
        for it in item:
            print(it["name"])


#1: students having the lowest age, students having the highest age
def find_the_highest_and_lowest_age(students):
    age_group = {}
    for student in students:
        age = student["age"]
        if age in age_group:
            age_group[age].append(student)
        else:
            age_group[age] = [student]

    key_max = 0
    key_min = 100
    for k in age_group.keys():
        if k > key_max:
            key_max = k
    for k in age_group.keys():
        if k < key_min:
            key_min = k

    max_age_group = [v for k,v in age_group.items() if key_max == k]
    min_age_group = [v for k,v in age_group.items() if key_min == k]
    print(f" The students who have the highest age {key_max}: ")
    for item in max_age_group:
        for it in item:
            print(it["name"])
    print(f" The students who have the lowest age {key_min}: ")
    for item in min_age_group:
        for it in item:
            print(it["name"])

#1: Second solution
def find_the_highest_and_lowest_age1(students):
    age_group = {}
    for student in students:
        age = student["age"]
        if age in age_group:
            age_group[age].append(student)
        else:
            age_group[age] = [student]
    key_max = max(age_group.keys())
    key_min = min(age_group.keys())

    # Get students with highest and lowest age
    max_age_st = [student["name"] for student in age_group[key_max]]
    min_age_st = [student["name"] for student in age_group[key_min]]

    # Print results in one line
    print(f"The students who have the highest age {key_max} are: {", ".join(max_age_st)}")
    print(f"The students who have the lowest age {key_min} are: {", ".join(min_age_st)}")

# find_the_highest_and_lowest_age1(students)

#4: add key,values with class: "CodeTheps" and teacher: "Tan Do"
def update_students_list(students):
    for student in students:
        if "class" not in student.keys():
            student["class"] = "CodeTheps"
        if "teacher" not in student.keys():
            student["teacher"] = "Tan Do"
        else:
            pass
    #print(students)

update_students_list(students)

#5: add first_name, last_name in dictionary
def add_first_last_name(students):
    for student in students:
        name = student["name"]
        if "last_name" not in student.keys():
            student["last_name"] = name[:name.find(" ")]
        if "first_name" not in student.keys():
            student["first_name"] = name[name.find(" ")+1:]

add_first_last_name(students)

#6: The most popular last_name in the list
def most_popular_surname(students):
    popular_dict = {}
    for student in students:
        last_name = student["last_name"]
        if last_name in popular_dict:
            popular_dict[last_name] += 1
        else:
            popular_dict[last_name] = 1
    print(popular_dict)
    max1 = max(popular_dict.values())
    print(max1)

    popular_list = [k for k,v in popular_dict.items() if v == max1]
    print(popular_list)
    print(f"The most popular surname in the class is(are) {", ".join(popular_list)} with {max1} occurencies")

most_popular_surname(students)



