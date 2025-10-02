import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("data/retail_sales.csv")

print("Preview of dataset:")
print(df.head())

# Debug: show column names
print("Columns in dataset:", df.columns.tolist())

# Use the last column (TotalSales) to avoid KeyError
category_sales = df.groupby("Category")[df.columns[-1]].sum().sort_values(ascending=False)

print("\nSales by Category:\n", category_sales)

# Plot
plt.figure(figsize=(6,4))
sns.barplot(x=category_sales.index, y=category_sales.values)
plt.title("Total Sales by Category")
plt.ylabel("Sales")
plt.savefig("reports/figures/sales_by_category.png")
plt.show()

