from load_csv import load
import matplotlib.pyplot as plt


def main():
    country = "France"
    data = load("life_expectancy_years.csv").loc[country]
    plt.plot(data.index, data.values)
    plt.title(country + " Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.xticks(data.index[::40])
    try:
        plt.show()
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        exit()

if __name__ == "__main__":
    main()