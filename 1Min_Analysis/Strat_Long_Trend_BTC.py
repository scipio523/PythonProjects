# Program testing a trend following trading strategy. Buy when price exceeds a moving average; vice versa for sells.
# Configurable lookback period, stop loss, and profit target.

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

filename = 'Bitcoin 1Min.xlsx'
df = pd.read_excel(filename, index_col='Dates')
df = df[-10000:] # for testing

# initialize variables
lookback = 7800 # minutes
trade_count = 0
capital = 1000
pos = 0
df['Capital'] = capital
df['Buy Signal'] = np.nan
df['Sell Signal'] = np.nan

# Loop through the dataframe
for i in range(lookback, len(df.index)):
    if i % 10000 == 0:
        print(f'iteration: {i}')

    avg = df.loc[df.index[i-lookback]:df.index[i], 'Close'].mean()
    px = df.loc[df.index[i], 'Close']

    #buy signal
    if pos == 0 and px >= avg:
        pos = 1
        entry_px = px
        shs = capital / px
        df.loc[df.index[i], 'Buy Signal'] = px
        trade_count += 1

    #sell signal
    if pos == 1 and px < avg:
        pos = 0
        pnl = shs * (px - entry_px)
        capital += pnl
        df.loc[df.index[i], 'Sell Signal'] = px

    df.loc[df.index[i], 'Capital'] = capital

print(f'Trade Count: {trade_count}')
print(f'Ending Capital: {capital}')
print(f'Return: {capital / 1000 - 1}')

buy_hold_ret = df.loc[df.index[-1], 'Close'] / df.loc[df.index[0], 'Close'] - 1
print(f'Buy & Hold Return: {buy_hold_ret}')

df['Strat_Returns'] = df['Capital'].pct_change()
stdev = df['Strat_Returns'].std()
print(f'Stdev: {stdev}')

df['Returns'] = df['Close'].pct_change()
buy_hold_std = df['Returns'].std()
print(f'Buy & Hold Stdev: {buy_hold_std}')

stdev_down = df['Strat_Returns'].loc[df['Strat_Returns'] < 0].std()
print(f'Downside Stdev: {stdev_down}')

buy_hold_std_down = df['Returns'].loc[df['Returns'] < 0].std()
print(f'Downside Buy & Hold Stdev: {buy_hold_std_down}')

fig, axes = plt.subplots(nrows=2, ncols=1)
df['Close'].plot(ax=axes[0], title='Close')
df['Buy Signal'].plot(ax=axes[0], marker='^')
df['Sell Signal'].plot(ax=axes[0], marker='v')
df['Capital'][lookback:].plot(ax=axes[1], title='Capital')
fig.subplots_adjust(hspace=0.8)
plt.show()