import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
import pandas as pd


def main():
    print("1: Present the plot\n2: Close the program\n")

    user_choice = input("Enter here: ")

    if user_choice == '1':
        car_plot()
    elif user_choice == '2':
        exit_program()
    else:
        print("Invalid choice. Please try again.")
        main()


def exit_program():
    print("\nExiting Program....")


def currency_fmt(x, pos):
    return "${:,.0f}".format(x)


def car_plot():
    print("Plot is currently being presented")

    car = pd.read_csv('car_sales.csv')

    plt.figure(figsize=(12, 6))

    car_sales = np.array([col for col in car.columns if col != 'Month'])

    for Sales in car_sales:
        plt.plot(np.arange(0, len(car)), car[Sales], marker='.', label=Sales)

    car['Year'] = [x.split("-")[0] for x in car.Month]  # Extract the year from the Month column

    plt.xticks(np.arange(0, len(car), 12), car['Year'].unique(), rotation=0)

    plt.title('Car Sales Throughout 1960 - 1968 (US Dollars)')

    plt.xlabel('Year')
    plt.ylabel('Car Sales')

    plt.gca().yaxis.set_major_formatter(FuncFormatter(currency_fmt))

    plt.legend(loc="upper left")  # add this line to place the legend at the top left

    plt.savefig('Gas_price_figure.png', dpi=300)

    plt.show()


if __name__ == "__main__":
    main()
