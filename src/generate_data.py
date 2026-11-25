
import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

products = {
    "Laptop": ("Electronics", 800, 1500),
    "Mouse": ("Electronics", 15, 50),
    "Keyboard": ("Electronics", 30, 120),
    "Headphones": ("Electronics", 40, 200),
    "Chair": ("Furniture", 100, 400),
    "Desk": ("Furniture", 150, 600),
    "Notebook": ("Stationery", 2, 8),
    "Pen": ("Stationery", 1, 5),
    "Backpack": ("Accessories", 25, 100),
    "Watch": ("Accessories", 50, 300),
}

regions = ["North", "South", "East", "West"]

orders = []
start_date = datetime(2025, 1, 1)

for i in range(1, 501):
    product = random.choice(list(products.keys()))
    category, min_price, max_price = products[product]

    quantity = random.randint(1, 5)
    unit_price = round(random.uniform(min_price, max_price), 2)
    total_sales = round(quantity * unit_price, 2)

    order_date = start_date + timedelta(
        days=random.randint(0, 364)
    )

    orders.append({
        "Order_ID": f"ORD-{i:04d}",
        "Date": order_date.strftime("%Y-%m-%d"),
        "Product": product,
        "Category": category,
        "Quantity": quantity,
        "Unit_Price": unit_price,
        "Total_Sales": total_sales,
        "Region": random.choice(regions)
    })

df = pd.DataFrame(orders)

df.to_csv("data/sales.csv", index=False)

print("Dataset created successfully!")
print(f"Total orders: {len(df)}")
print(df.head())

