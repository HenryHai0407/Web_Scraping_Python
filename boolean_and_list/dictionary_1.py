car = {
"brand": "BMW",
"model": "C200",
"year": "2024",
"owner": "Hoang Hai"
}

car['type'] = "4-wheel"
print(car)

for item in car.values():
    print(item)

for k,v in car.items():
    print(f"Key is {k} and its value is: {v}")