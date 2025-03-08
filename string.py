# # While loop with break statement
# while True:
#     a = input("Please enter a number for length: ")
#     b = input("Please enter another number for width: ")
#     a = int(a)
#     b = int(b)
#     if a > b:
#         c = a * b
#         print(f"Area is {c}")
#         break
#     else:
#         print("a is not greater than b. Please enter the numbers again.")

# while True:
#     a = input("Please enter a length of rectangle: ")
#     b = input("Please enter a width of rectangle: ")
#     a = int(a)
#     b = int(b)
#     if a > b:
#         print(f"Perimeter of rec is {2*(a+b)}")
#     else:
#         print("a is not greater than b. Please enter the numbers again.")

# c = input("Please enter a radius for circle: ")
# c = int(c)
# print(f"Area of circle is {3.14*c*c}")

# a = 2
# b = 22
# c = a == b
# if c:
#     print("a is equal to b")
# else:
#     print("a is not equal to b")
#     if a > b:
#         print("a is greater than b")
#     else:
#         print("a is less than b")
# print("End of program")

# ------

# fruit_list = ["apple", "banana", "cherry"]
# for item in fruit_list:
#     print(item1)

# name  = "Hoang Hai"
# for character in name:
#     print(character)

# ---------------------------
# while True:
#     try:
#         e = input("Please enter a number: ")
#         e = int(e)
#         if e % 2 == 0:
#             print("Even number")
#         else:
#             print("Odd number")
#     except ValueError:
#         print("Invalid input.")

# ---------------------------
# hour = input("Please enter your working hour: ")
# hour = int(hour)
# rate = 2

# if hour > 40: 
#     salary = 40 * rate + (hour - 40) * rate * 1.5
#     print(f"Your salary is {salary}, you overworked {hour - 40} hours")
# else:
#     salary = hour * rate
#     print(f"Your salary is {salary}")

# ---------------------------
a = []
for i in range(0,1000):
    if i % 3 == 0 and i % 5 == 0:
        a.append(i)
print(count(a))  
