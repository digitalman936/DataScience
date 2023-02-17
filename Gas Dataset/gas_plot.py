import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

gas = pd.read_csv('gas_prices.csv')

print("This is a graph containing gas prices from 1990 - 2008 in US Dollars.\n")

countries = np.array([col for col in gas.columns if col != 'Year'])

plt.figure(figsize=(12, 6))

plt.title('Gas Prices throughout 1990 - 2008 (US Dollars)')

for country in countries:
    plt.plot(gas.Year, gas[country], marker='.', label=country)

for country in gas:
    if country != 'Year':
        print(country)

plt.xticks(gas.Year[::1])

plt.xlabel('Year')
plt.ylabel('US Dollars')

plt.legend(loc="upper left")  # add this line to place the legend at the top left

plt.savefig('Gas_price_figure.png', dpi=300)

plt.show()
