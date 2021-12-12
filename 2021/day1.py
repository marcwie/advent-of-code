import numpy as np
import pandas as pd

def run():
    data = np.loadtxt('data/day1/input')
    print('Part1 Solution:', (np.diff(data) > 0).sum())

    df = pd.DataFrame(data)
    print('Part2 Solution:', (df.rolling(window=3).sum().dropna().diff() > 0).sum().values[0])
   

if __name__ == '__main__':
    run()
