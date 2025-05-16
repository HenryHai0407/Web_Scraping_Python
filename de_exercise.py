# olst = ['Huynh','Ngoc','Phien']
# print(olst)
# olst.reverse()
# print(olst)


####2

# olt = []
# ostr = "Huynh Ngoc Phien"
# for x in ostr:
#     if x != " ":
#         olt.append(x)
# olt.reverse()

# for x in olt:
#     print(x)

####3

# olt = []
# ostr = "Huynh Ngoc Phien"
# for x in ostr:
#     if x != " ":
#         olt.append(x)

# for x in olt:
#     if  x not in ('a','e','i','o','u','y'):
#         print(x)

#3 mutta toinen ratkaisu:
print([x for x in "Huynh Ngoc Phien" if x != " " and x not in ('a','e','i','o','u','y')])

####4
olt = []
ostr = "Huynh Ngoc Phien"
for x in ostr:
    olt.append(x)
olt.reverse()

stradd = ""
for x in olt:
    stradd += x
print(stradd)

####5
list2 = [4,7,2,3,5,9,10]
a = 0
for x in list2:
    if x >= a:
        a = x
    else:
        continue
print(a)

###5 toinen ratkaisu:
from functools import reduce
b = reduce(lambda x,y: x if x>=y else y, [4, 7, 2, 3, 5, 9, 10], 0)
print(b)