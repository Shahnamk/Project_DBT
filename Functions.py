import pandas as pd
import matplotlib.pyplot as plt


def load_and_choose_columns(filepath: str, sheet_name: str = 0, skiprows: int = 0) -> pd.DataFrame:
    """
    Load an Excel sheet

    Parameters
    ----------
    filepath : str
        Path to the Excel file.
    sheet_name : str or int, default 0
        Sheet name or index to read.
    skiprows : int, default 0
        Number of rows to skip before the header (useful if there's a title/subtitle above the data).

    Returns
    -------
    pd.DataFrame
        The loaded DataFrame, ready for plotting.
    """
    df = pd.read_excel(filepath, sheet_name=sheet_name, skiprows=skiprows)
    df = df.dropna(how="all")  # drop fully empty rows

    print("Available columns:")
    for i, col in enumerate(df.columns):
        print(f"  [{i}] {col}")

    return df


def plot_columns(df: pd.DataFrame, x_col: str, y_col: str, kind: str = "line") -> None:
    """
    Plot one column against another.

    Parameters
    ----------
    df : pd.DataFrame
        The data to plot.
    x_col : str
        Column name to use for the x-axis.
    y_col : str
        Column name to use for the y-axis.
    kind : str, default 'line'
        Chart type: 'line', 'bar', or 'scatter'.
    """
    data = df[[x_col, y_col]].dropna().sort_values(by=x_col)

    plt.figure(figsize=(10, 6))
    if kind == "line":
        plt.plot(data[x_col], data[y_col], marker="o")
    elif kind == "bar":
        plt.bar(data[x_col], data[y_col])
    elif kind == "scatter":
        plt.scatter(data[x_col], data[y_col])
    else:
        raise ValueError(f"Unsupported chart kind: {kind}")

    plt.title(f"{y_col} vs {x_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()