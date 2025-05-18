# # Lesson 3:
# list1 = [1,2,3,4,5]

# list1.append(50)
# print(list1)
# list1.insert(1,100)
# print(list1)

# # # Remove the last element
# # list1.pop()
# # # Remove the specific element
# # list1.remove(50)

# # List methods: .sort(), .reverse(), .count(), .index(), .extend() (like concat)
# list2 = [80,90]
# list1.extend(list2)
# print(list1)

# print(f'The element position of 3 in the list is {list1.index(3)}')


# ----------------------------------------------
# Tuple
# Value of tuple could not be changed.
# CANNOT add more element
# Using tuple for storing unchanged data

# my_tuple = 1,3,5,7,9 # Packing
# print(my_tuple)

# a,b,c,d,e = my_tuple # Unpacking
# print(a,b,c,d,e)

# -----------------------------------------------
# Dictionary
# Call values:
# sinh_vien = {
#     'name': 'Hai',
#     'age': '29',
#     'country': 'Vietnam'
# }

# print(sinh_vien['name'])
# print(sinh_vien.get('country'))

# Deletion
# del sinh_vien['country']
# sinh_vien.pop('age)

# Check key in dictionary
# print('name' in sinh_vien)
# print('birth_day' in sinh_vien)

# Dictionary loop for presenting key and its values
# for k,v in sinh_vien.items():
#     print(k,v)

# aa = ['This','is','an','opportunity']

# # List loop for presenting indexes and its values
# for i,name in enumerate(aa):
#     print(f'Index {i}: {name}')

# ---------------------------
# Sets
# No duplication, no indexes
# Can add more element

# ---------------------------
# 1/
# list1 = [20, 6321, 21, 1232, 3256, 2141]

# for a in range(0,len(list1)):
#     for b in range(a+1,len(list1)):
#         if list1[a] >= list1[b]:
#             list1[a],list1[b] = list1[b], list1[a]
# print(list1)

# 2/
list2 = [20, 21, 1232, 21, 3256, 6325, 2150, 20, 1232]
# counts = {a: list2.count(a) for a in set(list2)}
# print(counts)
# for k,v in counts.items():
#     if v >= 2:
#         print(k,v)

# for a in set(list2):
#     counta1 = list2.count(a)
#     if counta1 > 1:
#         print(f'{a} is present in the list {counta1} times')

# counts = {a:list2.count(a) for a in set(list2) if list2.count(a) > 1}
# for a,count in counts.items():
#     print(f"{a} is present in the list {count} time{'s' if count > 1 else ''}")

# 3/
# list2 = [20, 21, 1232, 21, 3256, 6325, 2150, 20, 1232]
# counts = {a: list2.count(a) for a in set(list2)}
# print(counts)
# counts_re = {}
# for k,v in counts.items():
#     counts_re.setdefault(v, []).append(k)
# print(counts_re)

# 3/ Second solution
# list2 = [20, 21, 1232, 21, 3256, 6325, 2150, 20, 1232]
# counts = {a: list2.count(a) for a in set(list2)}
# print(counts)
# counts_re = {v:k for k,v in counts.items()} # IT WILL BE OVERWRITTEN IF VALUES HAVE THE SAME VALUES
# print(counts_re)

# 4/
# sign = "{}[]()"
# if  '()' and '[]' and '{}' in sign:
#     print(True)
# else:
#     print(False)


# --------- Lesson 3: Homework ---------------
# 1/
# Bài này em sử dụng chatGPT để giải ạ
# def is_valid(s: str) -> bool:
#     stack = []  # Empty list to store opening brackets
#     brackets = {')': '(', '}': '{', ']': '['}  # Maps closing brackets to opening brackets
#     for char in s:
#         if char in '({[':  # If it's an opening bracket
#             stack.append(char)  # Push it onto the stack
#         elif char in ')}]':  # If it's a closing bracket
#             if not stack:  # Stack empty? No opening bracket to match, so invalid
#                 return False
#             if stack.pop() != brackets[char]:  # Pop top bracket; does it match?
#                 return False
#     return len(stack) == 0  # Valid if stack is empty (all brackets matched)


# 1/ Second solution
# def is_valid(s: str) -> bool:
#     stack = []  # Our "pile" for opening brackets
#     brackets = {')': '(', '}': '{', ']': '['}  # Which closing bracket matches which opening bracket
#     print(f"Starting with string: {s}")
#     for char in s:
#         print(f"\nProcessing character: {char}")
#         if char in '({[':
#             stack.append(char)
#             print(f"  - Found opening bracket {char}, stack is now: {stack}")
#         elif char in ')}]':
#             print(f"  - Found closing bracket {char}")
#             if not stack:
#                 print(f"  - Stack is empty, no matching opening bracket! Invalid.")
#                 return False
#             top = stack.pop()
#             print(f"  - Popped {top} from stack")
#             if top != brackets[char]:
#                 print(f"  - Mismatch: {top} doesn't match {char}! Invalid.")
#                 return False
#             print(f"  - Match found, stack is now: {stack}")
#     print(f"\nFinished processing. Stack: {stack}")
#     if stack:
#         print("  - Stack not empty, some brackets unclosed! Invalid.")
#         return False
#     print("  - Stack empty, all brackets matched! Valid.")
#     return True

# 2/
# prices = [100, 102, 98, 105, 110, 111, 150, 145, 120]

# def calculate_returns(prices):
#     i = 0
#     while i < len(prices)-1:
#         return_per = (prices[i+1]-prices[i])*100/prices[i]
#         print(f'The return price at {i+2}th day is {return_per:.2f}%')
#         i = i + 1

# calculate_returns(prices)
# # 2/ Second solution
# def calculate_returns2(prices):
#     return list(
#         map(
#             lambda x,y: ((x-y)/y)*100,prices[1:],prices[:-1]
#         ) # x: current price, y: previous price
#     )

# print(calculate_returns2(prices))


# 3/
# transactions = [
#     ('buy', 100, 200.5), 
#     ('sell', 50, 220.0), 
#     ('buy', 150, 198.7), 
#     ('sell', 100, 215.0)
# ]
# def calculate_net_position(transactions):
#     net_position = {
#         'total_buy': 0,
#         'total_sell': 0,
#         'total_buy_price': 0,
#         'total_sell_price': 0
#     }

#     for tr in transactions:
#         if tr[0] == 'buy':
#             net_position['total_buy'] += tr[1]
#             net_position['total_buy_price'] += tr[2] * tr[1]
#         elif tr[0] == 'sell':
#             net_position['total_sell'] += tr[1]
#             net_position['total_sell_price'] += tr[2] * tr[1]
#     print(net_position)
# calculate_net_position(transactions)

# is_valid('[(]')