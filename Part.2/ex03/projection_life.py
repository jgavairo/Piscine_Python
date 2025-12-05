from load_csv import load
import pandas as pandas
import matplotlib.pyplot as plt


def projection_life(data: pandas.DataFrame, data2: pandas.DataFrame):
    """Projection the life expectancy for France.

    Args:
        data (pandas.DataFrame): The dataset to projection.
        data2 (pandas.DataFrame): The dataset to projection.
    """
    if data is None or data2 is None:
        print("Error: Could not load dataset")
        return None

    data = data["1900"]
    data2 = data2["1900"]

    plt.scatter(data2, data)
    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.xlabel("GDP per capita (USD)")
    plt.ylabel("Life expectancy (years)")
    plt.title("Life expectancy correlation with GDP per capita in 1900")
    plt.show()


def main():
    """Main function to projection the life expectancy for France.
    """
    try:
        data_life_expectancy = load("life_expectancy_years.csv")
        data_inflation = \
            load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        if data_life_expectancy is None or data_inflation is None:
            print("Error: Could not load dataset")
            return None
        projection_life(data_life_expectancy, data_inflation)
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    main()
