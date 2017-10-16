import pandas as pd


#def handle_by_suunta(df_tuple):
#    print(df_tuple[1].head())
#    return df_tuple[1]


def merge_by_hour(df_tuple):
    grouped_by_suunta = group_by_column(df_tuple[1], 'suunta')

    for row in grouped_by_suunta:
        print(row[1])

    return df_tuple[1]


def group_by_column(df, c_name):
    """
    Groups rows by column.
    :param df: Dataframe to be grouped
    :param c_name: Column to be grouped by.
    :return: Tuple, first contains by which value dataframe has been grouped by with. Second contains dataframe with
    rows which correspond the tuple's first value.
    """
    return df.groupby(c_name)


def road_usages(path='data/hki_road_usages.csv'):
    return pd.read_csv(path, encoding='utf-8')


def main():
    """
    Merges hours in original hki_road_usages.csv
    :return:
    """
    ru = road_usages('data/hki_road_usages.csv')
    grouped_by_piste = group_by_column(ru, 'piste')

    result = pd.concat(map(merge_by_hour, grouped_by_piste))


if __name__ == '__main__':
    main()
