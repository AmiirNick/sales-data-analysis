
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv("data/sales.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Create output directory
os.makedirs("outputs/charts", exist_ok=True)

# 1. Sales by Product
product_sales = df.groupby("Product")["Total_Sales"].sum().sort_values()

plt.figure(figsize=(10, 6))
product_sales.plot(kind="barh")
plt.title("Total Sales by Product")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig("outputs/charts/sales_by_product.png", dpi=300)
plt.close()

# 2. Sales by Category
category_sales = df.groupby("Category")["Total_Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 6))
category_sales.plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("outputs/charts/sales_by_category.png", dpi=300)
plt.close()

# 3. Monthly Sales Trend
monthly_sales = (
    df.groupby(df["Date"].dt.month)["Total_Sales"]
    .sum()
)

plt.figure(figsize=(10, 6))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(range(1, 13))
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/charts/monthly_sales.png", dpi=300)
plt.close()

# 4. Sales by Region
region_sales = df.groupby("Region")["Total_Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 6))
region_sales.plot(kind="bar")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("outputs/charts/sales_by_region.png", dpi=300)
plt.close()

print("All charts generated successfully!")
print("Charts saved in outputs/charts/")

