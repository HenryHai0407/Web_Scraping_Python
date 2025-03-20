# Working with File in Python
#
# file_name = "dictionary1\sinhvien.txt"

# try:
#     with open(file_name,"r") as f:
#         reading_f = f.readline() # Read a first line
#         reading_f1 = f.readline() # If we alreay run readline(), this line will read the NEXT line
#         r2 = f.readlines() # Return a LIST of all sentences
#         print(reading_f)
#         print(f"-------------")
#         print(reading_f1)
#         print(r2)
# except FileNotFoundError:
#     print(f"Error: The file {file_name} does not exist")
# except Exception as e:
#     print(f"An error occurred: {e}")

# ------
file_name = "dictionary1\\numbers.txt"

with open(file_name) as f:
    reading_f1 = f.readlines()
    print(reading_f1)

number_list = []

for line in reading_f1:
    line1 = line.strip().split(",")
    for number in line1:
        number_list.append(number)
print(number_list)

print(f"Maximum number is {max(number_list)}")
print(f"Minimum number is {min(number_list)}")

number_dict = {}
for number in number_list:
    if number in number_dict.keys():
        number_dict[number] += 1
    else:
        number_dict[number] = 1

max_frequency = []
for k,v in number_dict.items():
    if v == max(number_dict.values()):
        max_frequency.append(k)
print(", ".join(max_frequency),f"is(are) numbers with highest occurencies")

no_frequency = []
for k,v in number_dict.items():
    if v == 1:
        no_frequency.append(k)

no_frequency_sorted = sorted(no_frequency,reverse=True)
print(no_frequency_sorted)
index = 0
top_10 = []
for number in no_frequency_sorted:
    if index < 10:
        number = int(number)
        top_10.append(number)
        index += 1

print(f"The average number of top 10 highest numbers with no duplicate is {round(sum(top_10)/len(top_10),0)}")

no_frequency_sorted_ascending = sorted(no_frequency)
print(no_frequency_sorted_ascending)
index1 = 0
top_10_as = []
for number in no_frequency_sorted_ascending:
    if index1 < 10:
        if number == '0':
            continue
        else:
            number = int(number)
            top_10_as.append(number)
            index1 += 1
print(top_10_as)
print(f"The average number of top 10 lowest numbers with no duplicate is {round(sum(top_10_as)/len(top_10_as),0)}")