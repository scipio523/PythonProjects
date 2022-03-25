import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = 'raise'

def analyze_rets(rets, show):
    # assumes returns are daily returns
    cagr = (1 + rets).prod() ** (252 / len(rets)) - 1
    cumret = (1 + rets).cumprod()
    
    sharpe = np.sqrt(252) * rets.mean() / rets.std()

    drawdown = cumret / cumret.cummax() - 1
    maxDD = drawdown.min() 
    
    drawdown_tally = np.sign(drawdown) * -1
    drawdown_dur = pd.Series(0, index=drawdown_tally.index)
    for i in range(len(drawdown_tally)):
        if drawdown_tally.iloc[i] == 0:
            drawdown_dur[i] = 0
        else:
            drawdown_dur[i] = drawdown_dur[i-1] + 1
    maxDDD = drawdown_dur.max()

    calmar = cagr / -min(-0.01, maxDD)  # make min drawdown 1% to avoid divide by zero warnings

    pct_up_days = rets[rets > 0].count() / rets.count()
    avg_up_day = rets[rets > 0].mean()
    avg_down_day = rets[rets < 0].mean()
    avg_up_day_over_avg_down_day = avg_up_day / -avg_down_day

    # Plot equity curve
    if show == 'Yes':
        print(f'--- Daily Returns Analysis ---')
        print(f'Start Date: {rets.index[0]}')
        print(f'End Date: {rets.index[-1]}')
        print(f'Sample Size (Days): {len(rets)}')
        print(f'CAGR: {cagr*100:.2f}%')
        print(f'Sharpe: {sharpe:.2f}')
        print(f'Calmar: {calmar:.2f}')
        print(f'Max DD: {maxDD*100:.2f}%')
        print(f'Max DDD (Days): {maxDDD:.0f}')
        print(f'% Up Days: {pct_up_days*100:.2f}%')
        print(f'Avg Up Day: {avg_up_day*100:.2f}%')
        print(f'Avg Down Day: {avg_down_day*100:.2f}%')
        print(f'Avg Up Day / Avg Down Day: {avg_up_day_over_avg_down_day:.2f}')
        cumret.plot(title='Equity Curve')
        plt.show()

    return cagr, sharpe, calmar, maxDD, maxDDD, pct_up_days, avg_up_day, avg_down_day, avg_up_day_over_avg_down_day