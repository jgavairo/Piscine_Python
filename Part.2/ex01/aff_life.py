from load_csv import load
import pandas as pandas
import matplotlib.pyplot as plt


def aff_life(data: pandas.DataFrame):
    """Display the life expectancy projections for France.

    Args:
        data (pandas.DataFrame): The dataset to display.
    """
    if data is None:
        print("Error: Could not load dataset")
        return None

    filtered_data = data[data["country"] == "France"]

    if filtered_data.empty:
        print("Error: France not found in dataset")
        return None

    years = filtered_data.columns[1:].astype(int)
    values = filtered_data.iloc[0, 1:].values

    plt.plot(years, values)
    plt.title("France Life Expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


def main():
    """Main function to display the life expectancy projections for France.
    """
    try:
        data = load("life_expectancy_years.csv")
        aff_life(data)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
