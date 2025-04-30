import pandas as pd
import random
import numpy as np

data = {
    "product_id": [i for i in range(1, 51)],
    "product_name": [f"Product {i}" if random.random() > 0.1 else None for i in range(1, 51)],
    "price": [round(random.uniform(0, 15000), 2) for _ in range(50)],
    "stock_qty": [random.randint(-5, 100) for _ in range(50)],
}
df_products = pd.DataFrame(data)
df_products.to_csv("product_catalog.csv", index=False)
