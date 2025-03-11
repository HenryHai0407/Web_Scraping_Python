fruits = ("apple","banana","pineapple","kiwi","orange","apple","kiwi")

# ft = set(fruit)
# #1
# print(ft)
# count = 0
# for item in ft:
#     count += 1
# print(count)

#2
# f_list = ()
# for idx, item in enumerate(fruit):
#     fruit_count = (item,fruit.count(item))
#     fruit_count = tuple(fruit_count)
#     f_list += fruit_count
# print(f_list)

fruit_counts = {}
for fruit in fruits:
    fruit_counts[fruit] = fruit_counts.get(fruit,0) + 1

num_types = len(fruit_counts)

min_fruits = min(fruit_counts, key=fruit_counts.get)
max_fruits = max(fruit_counts, key=fruit_counts.get)

print(f"Total number of fruit types: {num_types}")
print(f"Fruit with the highest count: {max_fruits} ({fruit_counts[max_fruits]} times)")
print(f"Fruit with the lowest count: {min_fruits} ({fruit_counts[min_fruits]} times)")