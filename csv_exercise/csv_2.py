import csv

file_name = "csv_exercise\\students.csv"
dict = {}
with open(file_name) as f:
    lines = csv.DictReader(f)
    for line in lines:
        print(line)
        sur_name = line['name'][:line['name'].find(" ")]
        if sur_name == 'Le' or sur_name == 'Do' or line['name'].find("a") != -1 and sur_name not in dict:
            dict[sur_name] = [int(line['mark'])]
        elif sur_name == 'Le' or sur_name == 'Do' or line['name'].find("a") != -1 and sur_name in dict:
            dict[sur_name].append(int(line['mark']))

max_score = 0
for k,v in dict.items():
    if max(v) > max_score:
        max_score = max(v)
    else:
        continue
print(max_score)

student_surname_list = []
for k,v in dict.items():
    if max_score in v:
        student_surname_list.append(k)
print(f"Surname of student who has the highest score is {student_surname_list}")