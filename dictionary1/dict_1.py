dict_1 = {
    "name": "Tan Do",
    "age": 20,
    "class": "Python"
}

# for k,v in dict_1.items():
#     print(k,v)

# dict_2 = [(k,v) for k,v in dict_1.items()]
# print(dict_2)

# for key in dict_1:
#     print(key, ":",dict_1[key])

print("\n".join(map(lambda kv: f" {kv[0]}: {kv[1]}", dict_1.items())))