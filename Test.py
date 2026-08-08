import pandas as pd
from Functions import load_and_choose_columns

def test_load_expenses_has_expected_columns():
    df = load_and_choose_columns(
        r"C:\Users\Joe\Downloads\expense_tracker.xlsx",
        sheet_name="Expenses",
        skiprows=3
    )
    expected_cols = {"Date", "Category", "Description", "Amount", "Payment Method"}
    assert expected_cols.issubset(set(df.columns))

def test_load_expenses_has_no_empty_rows():
    df = load_and_choose_columns(
        r"C:\Users\Joe\Downloads\expense_tracker.xlsx",
        sheet_name="Expenses",
        skiprows=3
    )
    assert df["Date"].isna().sum() == 0

def test_amount_column_is_numeric():
    df = load_and_choose_columns(
        r"C:\Users\Joe\Downloads\expense_tracker.xlsx",
        sheet_name="Expenses",
        skiprows=3
    )
    assert pd.api.types.is_numeric_dtype(df["Amount"])