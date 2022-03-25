import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ticker = 'SPY'
df = pd.read_excel(ticker+'.xlsx', index_col='Date')
rets = df['Close'].pct_change()

buckets = [-.99, -.03, -.025, -.02, -.015, -.01, -.005, 0, .005, .01, .015, .02, .025, .03, .99]
probabilities = []
median_ret = []
sample_size = []
for i in range(len(buckets)-1):
    lower = buckets[i]
    upper = buckets[i+1]

    rets_slice = rets[(rets.shift() > lower) & (rets.shift() <= upper)]

    prob = rets_slice[rets_slice > 0].count() / rets_slice.count()
    probabilities.append(prob)

    median_ret.append(rets_slice.median())

    sample_size.append(rets_slice.count())

results = pd.DataFrame({'Probabilities':probabilities, 'Median Return':median_ret, 'Sample Size':sample_size}, index=buckets[1:])
results.index.name = 'Buckets'
results.index *= 100
results[['Probabilities', 'Median Return']] *= 100
print(results)

ax = results['Median Return'].plot.bar()
ax.set_title(ticker)
ax.set_xlabel('Previous Day Return Bucket')
ax.set_ylabel('Next Day Median Return (%)')

plt.show()