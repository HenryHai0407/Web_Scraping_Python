# Uncomment for each exercise when running it
# 1/
# string_input = input("Enter your string: ")
# a_list = [x for x in string_input]
# print(a_list)

# for a in set(a_list): # Using set to avoid duplication
#     counta1 = a_list.count(a)
#     print(f'{a} is present in the list of {counta1} times.')

# # Using dictionary
# counts = {a: a_list.count(a) for a in set(a_list)}
# for a,count in counts.items():
#     print(f'{a} is present in the list {count} times')

# 2/
# int_list = [1,4,6,7,12,100,16,19,25]
# max_num = -1000
# for a in int_list:
#     if a >= max_num:
#         max_num = a
# print(max_num)

# less_than_max = -1000
# for a in int_list:
#     if a != max_num:
#         if a > less_than_max:
#             less_than_max = a
# print(f'The 2nd highest element in the list: {less_than_max} ')

# 2/ Second solution:
# int_list.sort(reverse=True)
# int_list[1]

# 3/
# int_input = int(input("Enter a number: "))
# def prime_number_check(int_input):
#     if int_input <= 1:
#         return False
#     for i in range(2,int_input):
#         if int_input % i == 0:
#             return False
#         else:
#             return True

# if prime_number_check(int_input):
#     print(f"Prime number")
# else:
#     print(f"NOT a Prime number")

# 4/
# int_input = [1, 6, 4, 2, 5 , 4]

# a = 0
# list_ad = []

# for c in range(0,len(int_input)):
#     for j in range(c+1, len(int_input)):
#         if int_input[c] >= int_input[j]:
#             int_input[c], int_input[j] = int_input[j],int_input[c]

# print(int_input)

# 5/
# dict_5 = {a:[] for a in range(1,100)}
# for i,v in dict_5.items():
#     for a in range(1,i+1):
#         v.append(a)
# print(dict_5)

# 5/ Second solution
# result = {}

# for i in range(1,11):
#     result[i] = list(range(1,i+1))
# print(result)