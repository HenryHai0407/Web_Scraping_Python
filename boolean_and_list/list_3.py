from collections import Counter
idx = 0
score_list = []
while idx < 10:    
    score = input("Please enter student score: ")
    if score.isnumeric():
        score_list.append(int(score))
        idx += 1
    else:
        print("Invalid input. Please input correct value!")
        continue

#1:
a_sl = sorted(score_list)
d_sl = sorted(score_list,reverse=True)
print(a_sl)
print(d_sl)

#2:
# top5_list = []
# ai = 0
# while ai < 4:
#     top5_list.append(d_sl[ai])
#     ai += 1
# print(f"List top 5: {top5_list}")

top5_d_sl = d_sl[:5]
print(f"top 5 highest: {top5_d_sl}")
top5_lowest_d_sl = a_sl[:5]
print(f"top 5 highest: {top5_lowest_d_sl}")

#3:
score_list_1 = Counter(score_list)
print(score_list_1)
score_list_common = score_list_1.most_common(5)
for item in score_list_common:
    print(f"For {item[0]}, it has {item[1]} occurences")

#3 second solution: Using Dictionary
f = {}
for num in score_list:
    f[num] = f.get(num,0) + 1
print(f)
m = max(f, key=f.get)
print(m)