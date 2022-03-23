# Idea: is there a "rubber band" effect whereby a stock may experience a mean reversion effect if it becomes too overextended?

# We will define "EMA Gap" as the percentage difference between price and the EMA. 
# Gap_Above is when price is above EMA. Gap_Below is when price is below EMA.
# We will regress the Forward returns against the EMA Gap. Note that we are taking into account the size of the EMA Gap here.

# Findings:
# For SPY (S&P 500) - Gap_Above is associated with negative forward performance (perhaps the stock got overextended). 
# Gap_Below is associated with positive forward performance (perhaps the stock got overextended to the downside).
# This confirms the intuition that when the stock market is overextended, there is a mean reversion effect.

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns

ticker = 'spy'

filename = ticker+'.xlsx'
df = pd.read_excel(filename, index_col='Date')
df = df.dropna(how='all')

df['Returns'] = df['Close'].pct_change()
window = 20

df['EMA'] = df['Close'].ewm(span=window, min_periods=window).mean()
df['Gap'] = abs(df['Close'].shift(1) / df['EMA'].shift(1) - 1)
df['Gap_Above'] = df['Gap'].loc[df['Close'].shift(1) > df['EMA'].shift(1)]
df['Gap_Below'] = df['Gap'].loc[df['Close'].shift(1) <= df['EMA'].shift(1)]

# Regression - above EMA
Y = df['Returns'].loc[df['Gap_Above'].notnull()]  # long returns
X = df['Gap_Above'].dropna()
X = sm.add_constant(X)
lm = sm.OLS(Y, X)
results = lm.fit()
print(results.summary())

# Regression - below EMA
Y = df['Returns'].loc[df['Gap_Below'].notnull()]  # short returns
X = df['Gap_Below'].dropna()
X = sm.add_constant(X)
lm = sm.OLS(Y, X)
results = lm.fit()
print(results.summary())

# Scatter Plot
fig, (ax1, ax2) = plt.subplots(ncols=2)
sns.regplot(df['Gap_Above'], df['Returns'], ax=ax1)
sns.regplot(df['Gap_Below'], df['Returns'], ax=ax2)
fig.suptitle(ticker)
plt.show()