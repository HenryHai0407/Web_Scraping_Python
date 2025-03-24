import csv

# Read
file_name = "csv_exercise\\accounts.csv"
# with open(file_name) as f:
#     lines = csv.reader(f)
#     for line in lines:
#         line[4] = line[4].replace("\n"," ")
#         print(line)

# DictReader
# score_list = []
# score_list_female = []
# with open(file_name) as f1:
#     lines2 = csv.DictReader(f1)
#     for line1 in lines2:
#         line1['address'] = line1['address'].replace("\n"," ")
#         score_list.append(float(line1['score']))
#         if int(line1['id']) % 2 == 0 and line1['gender'] == 'Female':
#             score_list_female.append(float(line1['score']))

# avg_score_class = (sum(score_list)/len(score_list))

# print(f" The average score of the class is {round(avg_score_class,2)}")

# # Calculate the average score by gender in Hanoi
# avg_score_female = (sum(score_list_female)/len(score_list_female))

# print(f"The average score by gender in Hanoi is {round(avg_score_female,2)}")

# Exercise 2: Export the student data having score > 8 as JSON type by address
address_dict = {}
with open(file_name) as f2:
    lines3 = csv.DictReader(f2)
    for line3 in lines3:
        line3['address'] = line3['address'].replace("\n"," ")
        if float(line3['score']) > 70 and line3['address'] not in address_dict:
            address_dict[line3['address']] = [line3['score']]
        elif float(line3['score']) > 70 and line3['address'] in address_dict:
            address_dict[line3['address']].append(line3['score'])
print(address_dict)