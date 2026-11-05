from load_csv import load
import matplotlib.pyplot as plt


def convert(num: str) -> float:
    '''
    extract the last charcter of a population value
    and returns the according float value
    '''
    suffixes = {'k': 1000, 'M': 1000000, 'B': 1000000000}
    last = num[-1]
    if (last in suffixes):
        return float(num[:-1]) * suffixes[last]
    return float(num)


def main():
    '''
    shows a graph comparing the population total of France
    and another country.
    '''
    country = "Madagascar"
    data = load("population_total.csv")
    data_f = data.loc["France", "1800":"2050"].map(convert)
    data_c = data.loc[country, "1800":"2050"].map(convert)
    positions = range(20000000, 80000000, 20000000)
    plt.plot(data_f.index, data_f.values, label="France")
    plt.plot(data_c.index, data_c.values, label=country)
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.xticks(data_f.index[::40])
    plt.yticks(positions, [f"{p // 1000000}M" for p in positions])
    try:
        plt.legend(loc="lower right")
        plt.show()
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        exit()


if __name__ == "__main__":
    main()
