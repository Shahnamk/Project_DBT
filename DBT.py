import pandas as pd

expenses = pd.read_excel(r"C:\Users\Joe\Downloads\expense_tracker.xlsx", sheet_name="Expenses", skiprows=3)
print(expenses.head())

print(expenses.columns.tolist())

category_totals = expenses.groupby("Category")["Amount"].sum()
print(category_totals)

