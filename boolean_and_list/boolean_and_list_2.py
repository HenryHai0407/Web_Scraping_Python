# Given a string of characters inputing from the computer. Please find the character has
# the lowest point based on Unicode point by using ord()
# num = input("Enter a list of characters: ")
# position_min = None
# index_min = None
# for item in num:
#     print(f"The {item} has ord {ord(item)} ")
#     item_position = ord(item)
#     if position_min is None:
#         position_min = item_position
#         index_min = num.index(item)
#     else:
#         if position_min > item_position:
#             position_min = item_position
#             index_min = num.index(item)
# print(f"The character {num[index_min]} has the lowest point, which is {position_min}")

# 
# par = input("Enter the paragraph: ")
# position_min = None
# position_max = None
# index_min = None
# index_max = None
# for item in par:
#     print(f"The {item} has {ord(item)} ")
#     item_position = ord(item)
#     if position_min is None:
#         position_min = item_position
#         index_min = par.index(item)
#     elif position_max is None:
#         position_max = item_position
#         index_max = par.index(item)
#     else:
#         if position_min > item_position:
#             position_min = item_position
#             index_min = par.index(item)
#         elif position_max < item_position:
#             position_max = item_position
#             index_max = par.index(item)
# print(f"The character {par[index_min]} has the lowest point, which is {position_min}")
# print(f"The character {par[index_max]} has the lowest point, which is {position_max}")

#2 Find word has total Unicode point value
# par = input("Enter the paragraph: ")
# par1 = par.split()
# word_count_list = []
# word_count = 0
# index_max = None
# for word in par1:
#     for ch in word:
#         word_count = word_count + ord(ch)
#     word_count_list.append(word_count)
#     word_count = 0
# print(word_count_list) # Check the values in the list
# position_max = None
# # Solution 1:
# # for nub in word_count_list:
# #     nub = int(nub)
# #     if position_max is None:
# #         position_max = nub
# #         index_max = word_count_list.index(nub)
# #     else:
# #         if position_max < nub:
# #             position_max = nub
# #             index_max = word_count_list.index(nub)
# # Solution 2:
# for idx, nub in enumerate(word_count_list):
#     if position_max is None or position_max < nub:
#         position_max = nub
#         index_max = idx
# print(f"Word has the highest total Unicode point value is: {par1[index_max]} with {position_max} point")

#3 Find the word has the highest average Unicode point in the list
par = input("Enter the paragraph: ")
par1 = par.split()
word_count_list = []
word_point = 0
word_count = 0
index_max = None
position_max = None
for word in par1:
    for ch in word:
        word_point = word_point + ord(ch)
        word_count += 1
    word_avg = word_point / word_count
    word_avg = round(word_avg,2)
    word_count_list.append(word_avg)
    word_count = 0
print(word_count_list)
for idx,nub in enumerate(word_count_list):
    if position_max is None or position_max < nub:
        position_max = nub
        index_max = idx
print(f"Word has the highest average Unicode point value is {par1[idx]} with {position_max} points")

