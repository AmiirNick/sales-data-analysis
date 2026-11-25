
import pandas as pd
import os

# Load dataset
df = pd.read_csv("data/sales.csv")
df["Date"] = pd.to_datetime(df["Date"])

os.makedirs("outputs", exist_ok=True)

# Calculate key metrics
total_revenue = df["Total_Sales"].sum()
average_order_value = df["Total_Sales"].mean()
total_orders = len(df)
total_items = df["Quantity"].sum()

# Product analysis
product_sales = df.groupby("Product")["Total_Sales"].sum()
top_product = product_sales.idxmax()
top_product_revenue = product_sales.max()

# Category analysis
category_sales = df.groupby("Category")["Total_Sales"].sum()
top_category = category_sales.idxmax()
top_category_revenue = category_sales.max()

# Regional analysis
region_sales = df.groupby("Region")["Total_Sales"].sum()
top_region = region_sales.idxmax()

# Monthly analysis
monthly_sales = df.groupby(df["Date"].dt.month)["Total_Sales"].sum()
best_month = monthly_sales.idxmax()

# Calculate percentages
top_product_share = (top_product_revenue / total_revenue) * 100
top_category_share = (top_category_revenue / total_revenue) * 100

# Generate insights
insights = [
    "========== BUSINESS INSIGHTS ==========",
    f"Total Revenue: {total_revenue:,.2f}",
    f"Total Orders: {total_orders}",
    f"Average Order Value: {average_order_value:,.2f}",
    f"Total Items Sold: {total_items}",
    "",
    f"Top Product: {top_product}",
    f"Product Revenue: {top_product_revenue:,.2f}",
    f"Product Revenue Share: {top_product_share:.2f}%",
    "",
    f"Top Category: {top_category}",
    f"Category Revenue: {top_category_revenue:,.2f}",
    f"Category Revenue Share: {top_category_share:.2f}%",
    "",
    f"Top Region: {top_region}",
    f"Best Sales Month: {best_month}",
    "",
    "Note: This project uses synthetic data."
]

report = "\n".join(insights)

print(report)

# Save report
with open("outputs/business_insights.txt", "w") as file:
    file.write(report)

# Export summary tables
product_sales.sort_values(ascending=False).to_csv(
    "outputs/product_sales.csv"
)

category_sales.sort_values(ascending=False).to_csv(
    "outputs/category_sales.csv"
)

region_sales.sort_values(ascending=False).to_csv(
    "outputs/region_sales.csv"
)

monthly_sales.to_csv("outputs/monthly_sales.csv")

print("\nReports exported successfully!")

