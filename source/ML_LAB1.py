import pandas as pd
import numpy as np


def main():
    df = pd.read_csv("titanic3.csv", on_bad_lines='skip')
    print(df.head())


if __name__ == "__main__":
    main()
