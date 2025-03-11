# # Input a list of integers and try to check whether it is in order or not
# number_list = []
# ind = 0
# while ind < 4:
#     name = input("Enter a number: ")
#     if name.isnumeric():
#         name = int(name)
#         number_list.append(name)
#         ind += 1
#     else:
#         print("Please type correct input")
#         continue
# print(number_list)

# index_0 = 0
# index_1 = 1
# if number_list[index_0] < number_list[index_1]:
#     index_0 += 1
#     index_1 += 1
#     if number_list[index_0] < number_list[index_1]:
#         index_0 += 1
#         index_1 += 1
#         if number_list[index_0] < number_list[index_1]:
#             index_0 += 1
#             index_1 += 1
#             print("in ascending order")
#     elif number_list[index_0] > number_list[index_1] or number_list[index_0] == number_list[index_1]:
#         print("Not in a certain order")
# elif number_list[index_0] == number_list[index_1]:
#     index_0 += 1
#     index_1 += 1
#     if number_list[index_0] == number_list[index_1]:
#         index_0 += 1
#         index_1 += 1
#         if number_list[index_0] == number_list[index_1]:
#             index_0 += 1
#             index_1 += 1
#             print("all number are equal")
#     elif number_list[index_0] < number_list[index_1] or number_list[index_0] > number_list[index_1]:
#         print("Not in a certain order")
# elif number_list[index_0] > number_list[index_1]:
#     index_0 += 1
#     index_1 += 1
#     if number_list[index_0] > number_list[index_1]:
#         index_0 += 1
#         index_1 += 1
#         if number_list[index_0] > number_list[index_1]:
#             index_0 += 1
#             index_1 += 1
#             print("in descending order")
#     elif number_list[index_0] < number_list[index_1] or number_list[index_0] == number_list[index_1]:
#         print("Not in a certain order")


# Another solution:
number_list = []
while True:
    name = input("Enter a number: (or type 'done' to finish)")
    if name.lower() == 'done':
        break
    elif name.lstrip("-").isnumeric():
        number_list.append(int(name))
    else:
        print("Invalid input. Please enter a valid integer")

if not number_list:
    print("No numbers entered")
elif number_list == sorted(number_list):
    print("In ascending order")
elif number_list == sorted(number_list, reverse = True):
    print("In descending order")
elif len(set(number_list)) == 1:
    print("All numbers are equal")
else:
    print("The list is not in a certain order")