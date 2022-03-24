# Comparing returns when above the exponential moving avg (EMA) versus below the EMA, looping over many lookback windows.
# Findings: Over the sample period, returns on average are higher when above the EMA than below it, for nearly all lookback windows except for very short windows.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt

ticker = 'spy'

filename = ticker+'.xlsx'
df = pd.read_excel(filename, index_col='Date')
df = df.dropna(how='all')
#df.index = pd.to_datetime(df.index)

df['Returns'] = df['Close'].pct_change()
years = (df.index[-1] - df.index[0]).days / 365

# calc average returns for various moving averages
results = []
for window in range(5, 505, 5):
    above_val = (1 + df.loc[df['Close'].shift(1) > df['Close'].ewm(span=window).mean().shift(1), 'Returns']).cumprod().iloc[-1]
    below_val = (1 + df.loc[df['Close'].shift(1) <= df['Close'].ewm(span=window).mean().shift(1), 'Returns']).cumprod().iloc[-1]
    above_cagr = above_val ** (1 / years) - 1
    below_cagr = below_val ** (1 / years) - 1
    results.append([window, above_cagr, below_cagr])

# convert results to a dataframe and output to Excel
results_df = pd.DataFrame(results, columns = ['window', 'above_cagr', 'below_cagr']) 
#results_df.to_excel('ema_output.xlsx')

# Plot data
ax1 = results_df.plot(kind='scatter', x='window', y='above_cagr', color='b', label="above MA")
ax2 = results_df.plot(kind='scatter', x='window', y='below_cagr', color='r', label="below MA", ax=ax1)
plt.axhline(y=0, xmin=0, xmax=1, color='k')
start_date = dt.strftime(df.index[0], '%Y-%m-%d')
end_date = dt.strftime(df.index[-1], '%Y-%m-%d')
plt.title(ticker+' '+start_date+' to '+end_date)
plt.ylabel('CAGR')
plt.xlabel('moving average window')
plt.legend()
plt.show()

# Calc performance metrics
window = 5
results = dict()

# Average Returns
results['avg'] = df['Returns'].mean()
results['above_avg'] = df.loc[df['Close'].shift(1) > df['Close'].ewm(span=window).mean().shift(1), 'Returns'].mean()
results['below_avg'] = df.loc[df['Close'].shift(1) <= df['Close'].ewm(span=window).mean().shift(1), 'Returns'].mean()

# Standard deviations
results['std'] = df['Returns'].std()
results['above_std'] = df.loc[df['Close'].shift(1) > df['Close'].ewm(span=window).mean().shift(1), 'Returns'].std()
results['below_std'] = df.loc[df['Close'].shift(1) <= df['Close'].ewm(span=window).mean().shift(1), 'Returns'].std()

# Negative standard deviations
results['downside_std'] = df.loc[df['Returns'] < 0, 'Returns'].std()
results['above_downside_std'] = df.loc[(df['Close'].shift(1) > df['Close'].ewm(span=window).mean().shift(1)) & (df['Returns'] < 0), 'Returns'].std()
results['below_downside_std'] = df.loc[(df['Close'].shift(1) <= df['Close'].ewm(span=window).mean().shift(1)) & (df['Returns'] < 0), 'Returns'].std()

# Sharpe ratio
results['sharpe'] = results['avg'] / results['std']
results['above_sharpe'] = results['above_avg'] / results['above_std']
results['below_sharpe'] = results['below_avg'] / results['below_std']

# Sortino ratio
results['sortino'] = results['avg'] / results['downside_std']
results['above_sortino'] = results['above_avg'] / results['above_downside_std']
results['below_sortino'] = results['below_avg'] / results['below_downside_std']

results_df = pd.DataFrame([results])
print(results_df)