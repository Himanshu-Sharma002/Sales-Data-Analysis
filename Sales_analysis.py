import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("SampleSuperstore.csv")

print(df.head())
print(df.describe())

print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())

category_sales = df.groupby("Category")["Sales"].sum()
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

region_profit = df.groupby("Region")["Profit"].sum()
region_profit.plot(kind="line", marker='o')
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.show()

plt.scatter(df["Discount"], df["Profit"])
plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.show()
