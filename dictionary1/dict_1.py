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
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
    {"name": "Lan", "age": 21},
    {"name": "Charlie", "age": 23},
    {"name": "Bob", "age": 24},
    {"name": "David", "age": 22},
    {"name": "Eve", "age": 20},
    {"name": "Li", "age": 27},
    {"name": "An", "age": 26},
    {"name": "Steven", "age": 21},
    {"name": "Marry", "age": 23},
]

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