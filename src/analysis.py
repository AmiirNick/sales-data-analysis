
import pandas as pd

# Load dataset
df = pd.read_csv("data/sales.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Basic information
print("\n========== DATASET OVERVIEW ==========")
print("Number of orders:", len(df))
print("Number of products:", df["Product"].nunique())
print("Number of categories:", df["Category"].nunique())
print("Number of regions:", df["Region"].nunique())

# Data quality check
print("\n========== DATA QUALITY ==========")
print("Missing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

# Sales statistics
print("\n========== SALES SUMMARY ==========")
print("Total revenue:", round(df["Total_Sales"].sum(), 2))
print("Average order value:", round(df["Total_Sales"].mean(), 2))
print("Total items sold:", df["Quantity"].sum())

# Best-selling products by revenue
print("\n========== TOP 5 PRODUCTS ==========")
top_products = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
print(top_products)

# Sales by category
print("\n========== SALES BY CATEGORY ==========")
category_sales = (
    df.groupby("Category")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)
print(category_sales)

# Sales by region
print("\n========== SALES BY REGION ==========")
region_sales = (
    df.groupby("Region")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)
print(region_sales)

# Monthly sales
print("\n========== MONTHLY SALES ==========")
monthly_sales = (
    df.groupby(df["Date"].dt.month)["Total_Sales"]
    .sum()
)
print(monthly_sales)

