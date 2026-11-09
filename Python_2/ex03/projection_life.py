from load_csv import load
import matplotlib.pyplot as plt


def main():
    '''
    shows a graph comparing the GDP to the life expectancy
    specifically in the year 1900
    '''
    file = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    gdp = load(file)["1900"]
    expect = load("life_expectancy_years.csv")["1900"]
    plt.scatter(gdp, expect)
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Excpectancy")
    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.yticks(range(20, 56, 5))
    try:
        plt.show()
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        exit()


if __name__ == "__main__":
    main()
