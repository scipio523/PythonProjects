# Create a 3-D plot looking at relationships between various market variables and forward equity returns.
# Findings: generally speaking, larger drawdowns, high VIX, and higher credit spreads are associated with higher forward equity returns.
# This aligns with the common wisdom "buy when there is blood in the streets."

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read in data from Excel file
df = pd.ExcelFile('Data.xlsx').parse('Sheet1')

d = [] # drawdown
v = [] # vix
s = [] # HY credit spread
r = [] # avg return

# Create arrays for chart
for this_d in np.arange(-0.50, 0.00, 0.02): 
    for this_v in np.arange(0, 60, 2):
        for this_s in np.arange(0, 2.60, 0.10):
            d.append(this_d)
            v.append(this_v)
            s.append(this_s)
            r.append(df['MSCI ACWI'].where((df['VIX'] > this_v) & (df['Credit Spread'] < this_s) & (df['Index Drawdown'] < this_d)).mean())
s = [i * 100 for i in s] # format as %

# Make plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
im = ax.scatter(d, v, r, c=s, cmap=plt.magma())
ax.set_xlabel('ACWI Drawdown from Peak')
ax.set_ylabel('Spot VIX')
ax.set_zlabel('Avg 1-yr Forward Return')
vals = ax.get_xticks()
ax.set_xticklabels(['{:,.0%}'.format(x) for x in vals]) # format as %
vals = ax.get_zticks()
ax.set_zticklabels(['{:,.0%}'.format(z) for z in vals]) # format as %
fig.colorbar(im, ax=ax, pad=0.1, format='%.0f%%', label='HY Spread % Change During Preceding Year') # format as %
plt.show()