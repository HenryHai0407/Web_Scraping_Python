import requests

url = "http://jsonplaceholder.typicode.com/posts"
data = requests.get(url)
data = data.json()
print(type(data))
print(data)
for item in data:
    for k,v in item.items():
        print(f"{k} : {v}")