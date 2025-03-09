# numbers = (1,2,3,"a",True)
# numbers = list(numbers)
# numbers.append("1000")
# numbers = tuple(numbers)
# print(numbers)

# --------------
# Given 5 random numbers from your input. Find the highest number in the list.
index = 0
number = []
while index < 5:
    num = input("Enter a number: ")
    index += 1
    try:
        if type(int(num)) == int:
            number.append(num)
    except ValueError:
        print("Invalid input. Please input correct number type.")
        index -= 1
        continue
print(number)
position_max = None
for nub in number:
    if position_max is None:
        position_max = nub
    else:
        if int(nub) > int(position_max):
            position_max = nub
print(f"So lon nhat trong day la {position_max}")