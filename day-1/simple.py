import pandas as pd
import numpy as np
import os

FILEPATH = os.path.join(os.path.dirname(__file__), "input.csv")


def abs_diff(a, b):
    return np.abs(a - b)


if __name__ == "__main__":
    df = pd.read_csv(FILEPATH)
    inputs = df.sort_values(by="left")["left"].values
    outputs = df.sort_values(by="right")["right"].values
    vabs = np.vectorize(abs_diff)
    results = vabs(inputs, outputs)
    print(sum(results))
