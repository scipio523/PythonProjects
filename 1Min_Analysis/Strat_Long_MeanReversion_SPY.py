# Program testing a mean reversion trading strategy. Buy when price exceeds a 2 standard deviation threshold.
# Configurable lookback period, stop loss, and profit target.

import pandas as pd 
import numpy as np
import math
import matplotlib.pyplot as plt

filename = 'SPY 1Min.xlsx'
df = pd.read_excel(filename, index_col='Dates')
df = df[-10000:] # for testing

# initialize variables
lookback = 120 # minutes
reward_risk = 3
timeout = 0
timeout_threshold = 0 # minutes to wait after being stopped out
trade_count = 0
capital = 1000
pos = 0
df['Capital'] = 0
df['Signal'] = np.nan

# Loop through the dataframe
for i in range(lookback, len(df.index)):
    if i % 10000 == 0:
        print(f'iteration: {i}')

    timeout = max(0, timeout-1)

    avg = df.loc[df.index[i-lookback]:df.index[i], 'Close'].mean()
    std = df.loc[df.index[i-lookback]:df.index[i], 'Close'].std()    
    px = df.loc[df.index[i], 'Close']

    #buy signal
    if pos == 0 and timeout == 0 and px < (avg - std*2):
        pos = 1
        entry_px = px
        stop = px - std
        target = px + (px - stop) * reward_risk
        shs = math.floor(capital / px)
        df.loc[df.index[i], 'Signal'] = px
        trade_count += 1

    #profit target
    if pos == 1 and px >= target:
        pos = 0
        pnl = shs * (target - entry_px)
        capital += pnl

    #stop loss
    if pos == 1 and px <= stop:
        pos = 0
        pnl = shs * (stop - entry_px)
        capital += pnl
        timeout = timeout_threshold

    df.loc[df.index[i], 'Capital'] = capital

print(f'Ending Capital: {capital}')
print(f'Return: {capital / 1000 -1}')
print(f'Trade Count: {trade_count}')

fig, axes = plt.subplots(nrows=2, ncols=1)
df['Close'].plot(ax=axes[0], title='Close')
df['Signal'].plot(ax=axes[0], marker='^')
df['Capital'][lookback:].plot(ax=axes[1], title='Capital')
fig.subplots_adjust(hspace=0.8)
plt.show()