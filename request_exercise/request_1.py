import requests
import pandas as pd
from sqlalchemy import create_engine

url = "https://jsonplaceholder.typicode.com/posts"
params = {
    "id": 1,
    "sort": "price"
}

posts = requests.get(url)
# print(data.content)
posts = posts.json()
# #1 Take the first comment of the first post
# print(data[0]['body'])

# #2 Take comments of the newest posts
# print(data[-1]['body'])

#3
user_count = {}
for post in posts:
    if post['userId'] not in user_count:
        user_count[post['userId']] = 1
    else:
        user_count[post['userId']] += 1
print(user_count)