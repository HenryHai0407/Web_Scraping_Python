# fruits = ("apple","banana","pineapple","kiwi","orange","apple","kiwi")

# # ft = set(fruit)
# # #1
# # print(ft)
# # count = 0
# # for item in ft:
# #     count += 1
# # print(count)

# #2
# # f_list = ()
# # for idx, item in enumerate(fruit):
# #     fruit_count = (item,fruit.count(item))
# #     fruit_count = tuple(fruit_count)
# #     f_list += fruit_count
# # print(f_list)

# fruit_counts = {}
# for fruit in fruits:
#     fruit_counts[fruit] = fruit_counts.get(fruit,0) + 1

# num_types = len(fruit_counts)

# min_fruits = min(fruit_counts, key=fruit_counts.get)
# max_fruits = max(fruit_counts, key=fruit_counts.get)
# # 
# print(f"Total number of fruit types: {num_types}")
# print(f"Fruit with the highest count: {max_fruits} ({fruit_counts[max_fruits]} times)")
# print(f"Fruit with the lowest count: {min_fruits} ({fruit_counts[min_fruits]} times)")

tuple_1 = ("apple","orange","kiwi","pineapple","grapes","watermelon","banana","strawberry")
tuple_2 = (10,30,40,25,35,76,54,53)
index = 0

# price_max = 0
# price_min = 0
# while index < len(tuple_1):
#     for item in tuple_1:
#         print(f"The price of {item} is {tuple_2[index]} dollars")
#         if price_max == 0 or price_max < tuple_2[index]:
#             f_max = []
#             f_max.append(item)
#             price_max = tuple_2[index]
#         if price_min == 0 or price_min > tuple_2[index]:
#             f_min = []
#             f_min.append(item)
#             price_min = tuple_2[index]
#         index += 1
# print(f"Fruit {" ".join(f_max)} has highest price: {price_max}")
# print(f"Fruit {" ".join(f_min)} has lowest price: {price_min}")

# Second way: Using Dictionary
# dict1 = {}
# index = 0
# while index < len(tuple_1):
#     for item in tuple_1:
#         dict1[item] = dict1.get(item,0) + tuple_2[index]
#         index += 1
# print(dict1)

# m = max(dict1, key=dict1.get)
# print(f"The price of {m} is highest with {dict1[m]}")
# min = min(dict1, key=dict1.get)
# print(f"The price of {min} is lowest with {dict1[min]}")

# ------------------------------------------
