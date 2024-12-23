import pandas as pd
import numpy as np
import os

FILEPATH = os.path.join(os.path.dirname(__file__), "input.csv")


def abs_diff(a, b):
    return np.abs(a - b)


def part1(left: pd.Series, right: pd.Series):
    vabs = np.vectorize(abs_diff)
    results = vabs(left, right)
    return sum(results)


def part2(left: pd.Series, right: pd.Series):
    def get_counts(value, counts):
        try:
            return counts[value]
        except:
            return 0

    value_counts = right.value_counts()
    multpliers = left.apply(lambda n: get_counts(n, value_counts))
    score = (left * multpliers).sum()
    return score


if __name__ == "__main__":
    df = pd.read_csv(FILEPATH)
    left = df.sort_values(by="left")["left"]
    right = df.sort_values(by="right")["right"]
    print("Part 1 score: ", part1(left, right))
    print("Part 2 score: ", part2(left, right))
