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
#difference, intersection
# set1 = {10,20,30,40,50,11,12}
# set2 = {11,12,13,14,15}
# set3 = {77,88,99,22,55,30,40,50}

# set1 = list(set1)
# set2 = list(set2)
# set3 = list(set3)
# set5 = []
# for item in set1:
#     set5.append(item)
# for item in set2:
#     set5.append(item)
# for item in set3:
#     set5.append(item)

# print(set5)
# dict1 = {}
# for item in set5:
#     dict1[item] = dict1.get(item,0) + 1
# print(dict1)

# # dict1.keys(), dict1.values(), dict1.items()
# count_max = 0
# for k,v in dict1.items():
#     if v > count_max:
#         number_max = [k]
#         count_max = v
#     elif v == count_max:
#         number_max.append(k)
# print(f"The most frequent occurence of {number_max} is {count_max}")
# # This method could help us to generate many numbers which have the same most frequent occurency

# Given a collection of car model of Mercedes and its prices, please show model and its corresponding price. As we know that model S type is the most supreme one, and the other types' prices will be determined based on its ord()
# mercedes_models = ("A-Class", "B-Class", "C-Class", "E-Class", "S-Class")

# base_price = 100000
# car_prices = {}
# for model in mercedes_models:
#     if model == "S-Class":
#         car_prices[model] = base_price
#     else:
#         model_price = sum(ord(char) for char in model)*100
#         car_prices[model] = model_price


# print("Mercedes Models and Prices: ")
# for model, price in car_prices.items():
#     print(f"{model}: ${price}")

#4:
# tuple_1 = ("CodeTheps","0868880797","Tan","Do")
# tuple_2 = [i for item in enumerate(tuple_1)]
# print(f"Item {tuple}")

# We have a tuple_1 tuple, please print its values and its indexes within 2 coding rows

# print("\n".join(f"Index {i}: {value}" for i, value in enumerate(tuple_1)))

#5:
# list_1 = ["a","b","c","d"]
# tuple_2 = (95,96,97,98)
# print("\n".join(f"Index {i}: {value}" for i, value in enumerate(list_1)))
# print("\n".join(f"Index {i}: {value}" for i,value in enumerate(tuple_2)))

#6:
# set_1 = {3,2,4,1,5,6,7,9,0,8}
# # for item in set_1:
# #     if item % 2 == 0:
# #         print(item/2)
# #     elif item % 2 == 1:
# #         print(item**2)

# set_2 = [item / 2 if item % 2 == 0 else item**2  for item in set_1]
# print(set_2)

#7:
list1 = [1,2,3,4,5,50,14,17,11,6,10,20,40,8,50,10,60,88,88,90,98]
as_list = sorted(list1)
de_list = sorted(list1,reverse = True)
print(as_list)
print(de_list)

m = max(as_list)
print(m)
min = min(as_list)
print(min)
