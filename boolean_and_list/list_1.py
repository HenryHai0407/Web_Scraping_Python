# car = {
# "brand": "BMW",
# "model": "C200",
# "year": "2024",
# "owner": "Hoang Hai"
# }

# car['type'] = "4-wheel"

# # for item in car.values():
# #     print(item)

# # for k,v in car.items():
# #     print(f"Key is {k} and its value is: {v}")


# car.update({"is_new": True})
# print(car)

# car_2 = car.copy()
# print(car_2)

# car.pop("year")
# print(car)
word_count = 0
word_length = 0
list_index = None
nor_list = [78,2,5,7,89,111,"apple","banana","candy","donkey","iloveyou"]
# for item in nor_list:
#     if type(item) == str:
#         for ch in item:
#             word_count = word_count + 1
#         if word_length < word_count:
#             word_length = word_count
#             list_index = nor_list.index(item)
#             word_count = 0
#         else:
#             word_count = 0
# print(f"String has the longest length is {nor_list[list_index]} with {word_length}")
smallest = None
list_index1 = None
for item in nor_list:
    if type(item) == int:
        if smallest is None or smallest > abs(item):
            smallest = abs(item)
            list_index1 = nor_list.index(item)            
print(f"An integer has a lowest absolute value {nor_list[list_index1]} with {smallest} point")