# Given a string of characters inputing from the computer. Please find the character has
# the lowest point based on Unicode point by using ord()
num = input("Enter a list of characters: ")
position_min = None
index_min = None
for item in num:
    print(f"The {item} has ord {ord(item)} ")
    item_position = ord(item)
    if position_min is None:
        position_min = item_position
        index_min = num.index(item)
    else:
        if position_min > item_position:
            position_min = item_position
            index_min = num.index(item)
print(f"The character {num[index_min]} has the lowest point, which is {position_min}")

#