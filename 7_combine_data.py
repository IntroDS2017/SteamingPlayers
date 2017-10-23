import pandas as pd
import sys

def main():
    """
    Combine the road usage data with the accident data based on the street address,
    hour and year.
    """

    try:
        method = sys.argv[1]
    except:
        method = "inner"

    if not method in ['inner', 'outer', 'left', 'right']:
        raise ValueError("Invalid joining method " + str(method))

    df_road_usages = pd.read_csv('data/4_road_usages.csv')
    df_accidents = pd.read_csv('data/6_accidents.csv')

    df_combined = pd.merge(df_road_usages, df_accidents, how = method,
                           left_on=['nimi', 'aika', 'vuosi'],
                           right_on=['Katuosoite', 'Tunti', 'Vuosi'])

    df_combined.to_csv('data/7_combined_' + method + "_join.csv", index = False)

if __name__ == '__main__':
    main()
