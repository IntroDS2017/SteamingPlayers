import pandas as pd
import math

def drop_column(c):
    if type(c) == int:
        df.drop(df.columns[c], axis = 1, inplace = True)

    else:
        df.drop(c, axis = 1, inplace = True)


def float_to_binary(id):
    if not math.isnan(id):
        return 1
    return 0


def main():
    print("Original columns:\n")
    print(df.columns.values)

    df['Onnettomuus'] = df['Onnett_id'].map(float_to_binary)
    drop_column("Onnett_id")

    df.to_csv(save_path, index = False)

    print("\nNew columns:\n")
    print(df.columns.values)


if __name__ == '__main__':
    load_path = "data/7_combined.csv"
    save_path = "data/8_combined.csv"

    df = pd.read_csv(load_path)
    main()
