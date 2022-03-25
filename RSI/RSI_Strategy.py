import pandas as pd
import sys
from util import analyze_rets

def RSI(prices, window):
    # Calculate the up and down moves
    delta = prices.diff().dropna()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0

    # Calculate the EWMA
    roll_up = up.ewm(com=window-1, min_periods=window).mean()
    roll_down = down.ewm(com=window-1, min_periods=window).mean()

    # Calculate the RSI
    RS = abs(roll_up / roll_down)
    RSI = 100 - (100 / (1 + RS))

    return RSI

def RSI_Strategy(ticker, filename):
    # Load Data
    df = pd.read_excel(filename, index_col='Date')
    df = df.dropna(how='all')
    df['Returns'] = df['Close'].pct_change()

    # Create RSI
    rsi_window = 14
    df['RSI'] = RSI(df['Close'], rsi_window)

    # Create RSI Strategy. RSI signal is shifted 1 day backward to prevent lookahead bias.
    # Default Signal=1 (long 100%). If RSI>=80, reduce exposure to 0%. If RSI <=30, increase exposure to 200%.
    df['Signals'] = 1
    df.loc[df['RSI'] >= 80, 'Signals'] = 0
    df.loc[df['RSI'] <= 30, 'Signals'] = 2
    df['Signals'].fillna(method='ffill', inplace=True)

    #df['Strategy Returns'] = 0
    df.loc[:, 'Strategy Returns'] = df['Signals'].shift() * df['Returns']

    # RSI Strategy Returns
    print('RSI Strategy:')
    cagr, sharpe, calmar, maxDD, maxDDD, pct_up_days, avg_up_day, avg_down_day, avg_up_day_over_avg_down_day = analyze_rets(df['Strategy Returns'], show='Yes')

    print('\n')

    # Buy & Hold Returns
    print('Buy & Hold:')
    cagr, sharpe, calmar, maxDD, maxDDD, pct_up_days, avg_up_day, avg_down_day, avg_up_day_over_avg_down_day = analyze_rets(df['Returns'], show='Yes')

ticker = 'SPY'
filename = ticker+'.xlsx'

RSI_Strategy(ticker, filename)