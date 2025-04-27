import pandas as pd
import random


# Generate 100 fake user signups
data = {
    "user_id": [i for i in range(1, 101)],
    "email": [f"user{i}@example.com" if random.random() > 0.05 else None for i in range(1, 101)],
    "age": [random.randint(15, 110) for _ in range(100)],
    "country": [random.choice(["USA", "Canada", "UK", "Australia", "Unknown"]) for _ in range(100)],
}

df = pd.DataFrame(data)
print(df)
df.to_csv("user_signup.csv",index=False)