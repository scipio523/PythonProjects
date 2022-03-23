# Find probability of loss over large sample of poker hands based on assumed win rate using monte carlo

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

trials = 1000
hands_list = [1, 100, 200, 300, 400]
prob_results = {}

for hands in hands_list:
    results = []
    for t in range(trials):
        money = 100
        for h in range(hands):
            ret = np.random.choice([.01, -.01], p=[0.55, 0.45])
            money = money * (1 + ret)
        results.append(money)
    results = pd.Series(results)
    prob_loss = results.loc[results < 100].count() / results.count()
    prob_results[hands] = prob_loss

df = pd.DataFrame(prob_results.items(), columns=['Hands', 'Prob of Loss'])
df.set_index('Hands', inplace=True)
df.plot()
plt.show()