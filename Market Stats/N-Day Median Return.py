import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ticker = 'SPY'
df = pd.read_excel(ticker+'.xlsx', index_col='Date')

rets = df['Close'].pct_change()
future_rets = rets.shift(-1)
up_down = np.sign(rets)

median_ret = []
sample_size = []
day_cumsum = pd.Series(0, index=up_down.index, dtype='float64')

for i in range(1, len(up_down)):
    if up_down[i-1] == up_down[i]:
        day_cumsum[i] = day_cumsum[i-1] + up_down[i]
    else:
        day_cumsum[i] = up_down[i]

results = pd.DataFrame(columns=['days up/down', 'median return'])
for bucket in day_cumsum.unique():
    median = future_rets[day_cumsum == bucket].median()
    results.loc[len(results)] = [bucket, median]

results.set_index('days up/down', inplace=True)
results.sort_index(inplace=True)
results['median return'] *= 100

ax = results['median return'].plot.bar()
ax.set_title(ticker)
ax.set_xlabel('# Days Up/Down in a Row')
ax.set_ylabel('Next Day Median Return (%)')

plt.show()