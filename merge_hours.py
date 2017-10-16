import pandas as pd


def flatten_list(to_flat):
    return [row for rows in to_flat for row in rows]


def handle_grouped_by_aika(group):
    rows = group[1]

    cars = rows['autot'].sum()

    result = rows.iloc[0].copy()
    result['autot'] = cars
    result['aika'] += 1

    return result


def handle_grouped_by_suunta(tuple):
    groups = tuple[1]

    normalized_aika = groups['aika'].apply(lambda x: x / 100)

    groups['aika'] = normalized_aika
    grouped_by_aika = group_by_column(groups, 'aika')

    result = map(handle_grouped_by_aika, grouped_by_aika)

    return result


def handle_grouped_by_piste(tuple):
    grouped_by_suunta = group_by_column(tuple[1], 'suunta')
    result = map(handle_grouped_by_suunta, grouped_by_suunta)

    flat_result = flatten_list(result)

    return flat_result


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
    return pd.read_csv(path)


def main(path='data/hki_road_usages.csv'):
    """
    Merges hours in original hki_road_usages.csv
    :return: New dataframe. If time-unit was between some hour, they were summed.
    """
    ru = road_usages(path)
    grouped_by_piste = group_by_column(ru, 'piste')

    result = map(handle_grouped_by_piste, grouped_by_piste)

    flat_result = flatten_list(result)

    result_df = pd.DataFrame(flat_result)

    return result_df


if __name__ == '__main__':
    """
    Optional parameters:
    sys.argv[1] = csv-file to be handeled. Default is data/hki_road_usages.csv
    sys.argv[2] = desired file name to be saved as
    """
    import sys
    pd.options.mode.chained_assignment = None  # default='warn'

    result = None

    try:
        result = main(sys.argv[1])
    except:
        result = main()

    try:
        result.to_csv(sys.argv[2])
    except:
        result.to_csv("data/hki_road_usages_v1.csv")

    print(result)
