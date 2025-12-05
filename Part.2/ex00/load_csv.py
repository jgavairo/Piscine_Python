import pandas as pandas


def load(path: str) -> pandas.DataFrame:
    """Load a CSV file into a pandas DataFrame.

Args:
    path (str): The path to the CSV file.

Returns:
    Dataset: A pandas DataFrame.
"""
    if not isinstance(path, str):
        print("Path must be a string")
        return None

    if not path.endswith(".csv"):
        print("Path must end with .csv")
        return None

    try:
        data = pandas.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except Exception:
        return None


def main():
    try:
        print(load("life_expectancy_years.csv"))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
