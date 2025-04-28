import pandas as pd
import random
data = {
    "transaction_id": [i for i in range(1, 201)],
    "amount_usd": [round(random.uniform(-20, 500), 2) for _ in range(200)],
    "payment_method": [random.choice(["Credit Card", "Paypal", "Bitcoin", "Unknown"]) for _ in range(200)],
    "date": [f"2024-04-{random.randint(1, 27)}" if random.random() > 0.02 else None for _ in range(200)],
}
df_sales = pd.DataFrame(data)
df_sales.to_csv("sales_transactions.csv", index=False)
