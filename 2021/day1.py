import numpy as np
import pandas as pd


def solve_part1(data):
    return (np.diff(data) > 0).sum()


def solve_part2(data):
    df = pd.DataFrame(data)
    return (df.rolling(window=3).sum().dropna().diff() > 0).sum().values[0]


def run():
    data = np.loadtxt('data/day1/test')
    solution = solve_part1(data)
    assert solution == 7

    data = np.loadtxt('data/day1/input')
    solution = solve_part1(data)
    print('Part1 Solution:', solution)

    data = np.loadtxt('data/day1/test')
    solution = solve_part2(data)
    assert solution == 5

    data = np.loadtxt('data/day1/input')
    solution = solve_part2(data)
    print('Part2 Solution:', solution)


if __name__ == '__main__':
    run()
