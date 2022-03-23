import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.append('C:/Users/dasei/Box/PythonProjects/util')
from util import analyze_rets

def run_strategy():
    # Calc z-score of ratio between price and moving avg of price. Go long when z-score low and vice versa.

    data = pd.read_excel('SPY_1min.xlsx', index_col='Date', parse_dates=True)

    #data = data[:'2021-01-31'] # train set
    #data = data['2021-01-31':] # test set

    cost_per_trade = 0.0001  # 1bp
    lookbacks = [50, 100, 150, 200, 300, 400, 500, 600, 800]  # bars (minutes)
    entry_thresholds = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]

    results = pd.DataFrame(columns=['lookback', 'entry_threshold', 'sharpe'])

    for lookback in lookbacks:
        print(f'lookback: {lookback}')
        for entry_threshold in entry_thresholds:
            exit_threshold = entry_threshold * 0.5
    
            price = data['Close']
            z_score = (price - price.rolling(lookback).mean()) / price.rolling(lookback).std()

            longEntry =  z_score < -entry_threshold
            longExit = z_score > -exit_threshold

            shortEntry = z_score > entry_threshold
            shortExit = z_score < exit_threshold

            unitsLong = pd.Series(index=z_score.index, dtype='float64')
            unitsLong[longEntry] = 1
            unitsLong[longExit] = 0
            unitsLong[0] = 0
            unitsLong.fillna(method='ffill', inplace=True)

            unitsShort = pd.Series(index=z_score.index, dtype='float64')
            unitsShort[shortEntry] = -1
            unitsShort[shortExit] = 0
            unitsShort[0] = 0
            unitsShort.fillna(method='ffill', inplace=True)

            pos = unitsLong + unitsShort
            #pos[(pos.index.strftime('%H:%M:%S') == '15:59:00')] = 0 # close positions at end of trading day (3:59pm)
            
            pnl = pos.shift() * price.pct_change()
            rets = pnl / np.abs(pos.shift())
            rets.fillna(0, inplace=True)
            
            # calc trade count
            diffs = np.abs(pos.diff()).fillna(0)
            diffs[diffs != 0] = 1
            trade_count = diffs.resample('1D').sum()
            total_trades = trade_count.sum()

            # aggregate returns by day, deduct trade costs
            daily_rets = rets.resample('1D').sum()
            daily_rets = daily_rets - (trade_count * cost_per_trade)

            cagr, sharpe, calmar, maxDD, maxDDD, pct_up_days, avg_up_day, avg_down_day, avg_up_day_over_avg_down_day = analyze_rets(daily_rets, show='No')

            results.loc[len(results)] = [lookback, entry_threshold, sharpe]
    
    results = results.pivot(index='lookback', columns='entry_threshold', values='sharpe')
    sns.heatmap(results, annot=True)
    plt.show()

run_strategy()