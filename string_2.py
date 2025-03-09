# names = "John, Peter, Mary, Tom, Alice"
# count = 0
# for ch in names.split(", "):
#     count += 1
#     print(f"{count}. {ch}")
# print(f"Total: {count} names")

# ----------------------------------------------

# names = """ james Born \n
# John doe \n
# Peter parker \n
# Mary jane \n
# tom cruise \n
# alice Cooper
# """
# names2 = [name.strip().title() for name in names.strip().split(" \n")]
# print(names2)

# count = 0
# for ch in names2:
#     count += 1
#     print(f"{count}-{ch.split()[-1].upper()}-{ch.split()[0]}")

# ----------------------------------------------
# Given a paragraph, find the first word that starts with 'a' and the last word that ends with 'c' that:/
# 1. It has the longest length
# 2. It has the shortest length
#-----------------------------------------------
# par = "ngay mai co anh c kia ko em c"
# print(len(par))

# # Find the first 'a'
# par1 = par.find("a")

# # Find the farthest 'c'
# par2 = par.rfind("c")

# # Find the shortest length of the string that starts with 'a' and ends with 'c'
# shortest_word = ""
# min_length = float('inf')
# for i in range(par1, par2 + 1):
#     if par[i] == 'a':
#         for j in range(i, par2 + 1):
#             if par[j] == 'c':
#                 current_word = par[i:j + 1]
#                 if len(current_word) < min_length:
#                     min_length = len(current_word)
#                     shortest_word = current_word

# print(f"The shortest word is {shortest_word} and its length is {len(shortest_word)}")

# # Find the second farthest 'c'
# second_par2 = par.rfind("c", 0, par2)
# if second_par2 != -1:
#     second_word = par[par1:second_par2 + 1]
#     print(f"The second word is {second_word} and its length is {len(second_word)}")
# else:
#     print("There is no second 'c' in the paragraph.")

# # Find the second farthest 'c'
# second_par2 = par.rfind("c", 0, len(par) - par2 - 1)
# if second_par2 != -1:
#     second_word = par[par1:second_par2 + 1]
#     print(f"The second word is {second_word} and its length is {len(second_word)}")
# else:
#     print("There is no second 'c' in the paragraph.")
# ----------------------------------------------
# paragraph = "Today I met a new guy who is the person living near our house. He is a nice guy but something triggers him, he getting crazy and says fuck off and damn everytime he wants"
# word_list = ["fuck", "damn"]
# paragraph = paragraph.split()
# paragraph1 = ' '.join(paragraph)
# word = "*****"
# word_count = 0
# for a in paragraph:
#     for b in word_list:
#         if a == b:
#             paragraph1 = paragraph1.replace(a,word)
#             word_count += 1
# rate = (word_count / len(paragraph))* 100
# print(f"The violation rate is {rate:.2f}%")
# if rate > 5:
#     print("This publication violates the community standards")
# else:
#     print("This publication is acceptable to publish")
# ---------------------
# par = "The sun today is very sunny I would say because because because the car is quiet and no no car car leads to no no no pollution"
# par = par.split()
# word_list =[]
# print(par.count("no"))
# count_list = []

# word_count = 0
# for word in par:
#     word_count = par.count(word)
#     count_list.append(word_count)
#     word_list.append(word)
# print(count_list)
# print(word_list)

# print(max(count_list))
# highest = []

# for index in range(0,len(count_list)):
#     if count_list[index] == max(count_list):
#         highest.append(index)
# print(highest)

par = "The sun today is very sunny I would say because the car is quiet and no leads to pollution"
par = par.split()

# Using Dictionary
word_counts = {}
for word in par:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Sorted Dictionary to Pair List
sorted_words = sorted(word_counts.items(), key =lambda x: x[1], reverse=True)
top_words = sorted_words[:5]
total_words = len(par)
top_word_total = sum(count for _, count in top_words)
threshold = 0.5 * total_words
print(top_word_total)
print(threshold)
if top_word_total <= threshold:
    print(top_words)
    print("Frequent words do not exceed 50% limit")
else:
    print("Most frequent words exceed 50% limit!")