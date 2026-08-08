import matplotlib
matplotlib.use('module://backend_interagg')
import matplotlib.pyplot as plt
import pdfplumber
import pandas as pd
import re


expenses = pd.read_excel(r"C:\Users\Joe\Downloads\expense_tracker.xlsx", sheet_name="Expenses", skiprows=3)
print(expenses.head())

print(expenses.columns.tolist())

category_totals = expenses.groupby("Category")["Amount"].sum()
print(category_totals)

expenses["Date"] = pd.to_datetime(expenses["Date"])

expenses["Month"] = expenses["Date"].dt.to_period("M")

summary = expenses.groupby(["Category", "Month"])["Amount"].sum()
print(summary)

idx = expenses.groupby(["Category", "Month"])["Amount"].idxmax()
highest_details = expenses.loc[idx, ["Category", "Month", "Date", "Description", "Amount"]]
print(highest_details)

pivot = expenses.pivot_table(
    index="Category",
    columns="Month",
    values="Amount",
    aggfunc="sum",
    fill_value=0
)

pivot.plot(kind="bar", figsize=(10, 6))
plt.title("Spend by Category and Month")
plt.xlabel("Category")
plt.ylabel("Total Spend ($)")
plt.legend(title="Month")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

daily = expenses.groupby("Date")["Amount"].sum().sort_index()

plt.figure(figsize=(10, 6))
plt.plot(daily.index, daily.values, marker="o")
plt.title("Daily Spend Over Time")
plt.xlabel("Date")
plt.ylabel("Total Spend ($)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


cumulative = daily.cumsum()

plt.figure(figsize=(10, 6))
plt.plot(cumulative.index, cumulative.values, marker="o", color="darkred")
plt.title("Cumulative Spend Over Time")
plt.xlabel("Date")
plt.ylabel("Cumulative Spend ($)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
