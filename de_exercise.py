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