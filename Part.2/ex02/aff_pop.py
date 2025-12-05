from load_csv import load
import pandas as pandas
import matplotlib.pyplot as plt


def convert_to_int(values: str) -> float:
    """Convert a string to an integer.

    Args:
        values (str): The string to convert.

    Returns:
        float: The float value.
    """
    if isinstance(values, str):
        if values.endswith("k"):
            return float(values[:-1]) * 1000
        if values.endswith("M"):
            return float(values[:-1]) * 1000000
        if values.endswith("B"):
            return float(values[:-1]) * 1000000000
        return float(values)
    return None


def aff_pop(data: pandas.DataFrame):
    """Display the population total between \
        1800 and 2050 for France and Switzerland.

    Args:
        data (pandas.DataFrame): The dataset to display.
    """
    if data is None:
        print("Error: Could not load dataset")
        return None

    france_data = data[data["country"] == "France"]
    if france_data.empty:
        print("Error: France not found in dataset")
        return None

    switzerland_data = data[data["country"] == "Switzerland"]
    if switzerland_data.empty:
        print("Error: Switzerland not found in dataset")
        return None

    try:
        all_years = france_data.columns[1:].astype(int)
        mask = all_years <= 2050
        years = all_years[mask]
        fr_values = france_data.iloc[0, 1:].values[mask]
        fr_values = [convert_to_int(values) for values in fr_values]
        sw_values = switzerland_data.iloc[0, 1:].values[mask]
        sw_values = [convert_to_int(values) for values in sw_values]

        fr_values = [v / 1_000_000 for v in fr_values]
        sw_values = [v / 1_000_000 for v in sw_values]

        plt.plot(years, fr_values, color="blue", label="France")
        plt.plot(years, sw_values, color="red", label="Switzerland")
        plt.title("Population projection to 2050")
        plt.xlabel("Year")
        plt.ylabel("Population (in millions)")
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    """Main function to display the population\
         total between 1800 and 2050 for France and Switzerland.
    """
    try:
        data = load("population_total.csv")
        if data is None:
            print("Error: Could not load dataset")
            return None
        aff_pop(data)
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    main()
