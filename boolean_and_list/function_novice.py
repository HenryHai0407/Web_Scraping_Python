# Pham vi bien trong function
a = ["Hanoi","Hue","Phu Quoc"]

def say():
    # when we use "global a" inside def function, it will turn the Func into Global
    # then the variable will be global in 2 sides
    a[0] = "Saigon"
    print(f"Func: {a}")

say()
print(f"Global: {a}")
