import pandas as pd


def flatten_list(to_flat):
    """
    Flattens 2D-list to 1d
    :param to_flat: List to flatten
    :return: 1D list
    """
    return [row for rows in to_flat for row in rows]


def handle_grouped_by_aika(group):
    """
    Sums car-amounts of given rows. Also time is increased by one to match accident-data. It is intended that group has
    the same 'aika'.
    :param group: Car-amounts to sum.
    :return: First row of the group, with summed 'autot'
    """
    rows = group[1]

    cars = rows['autot'].sum()

    result = rows.iloc[0].copy()
    result['autot'] = cars
    result['aika'] += 1

    return result


def handle_grouped_by_suunta(df_tuple):
    """
    Divides 'aika' column by 100, and groups rows by 'aika', and proceeds to pass this value to sum 'autot'.
    :param df_tuple: grouped-by - groups-tuple.
    :return: Two rows with summed 'auto':t, for each 'suunta'
    """
    groups = df_tuple[1]

    groups['aika'] = groups['aika'].apply(lambda x: x / 100) # normalize aika
    grouped_by_aika = group_by_column(groups, 'aika')

    return map(handle_grouped_by_aika, grouped_by_aika)


def handle_grouped_by_piste(df_tuple):
    """
    Splits rows by 'suunta', direction, and proceeds to sum 'auto'-column, cars for each hour.
    :param df_tuple: grouped-by - groups tuple. Should be already grouped by 'piste', measurement point
    :return: flatten result of rows, which have summed 'auto', car-amount for each hour
    """
    grouped_by_suunta = group_by_column(df_tuple[1], 'suunta')
    result = map(handle_grouped_by_suunta, grouped_by_suunta)

    return flatten_list(result)


# TODO: could be removed
def group_by_column(df, c_name):
    """
    Groups rows by column.
    :param df: Dataframe to be grouped
    :param c_name: Column to be grouped by.
    :return: Tuple, first contains by which value dataframe has been grouped by with. Second contains dataframe with
    rows which correspond the tuple's first value.
    """
    return df.groupby(c_name)


def main(road_usages_data_path):
    """
    Merges hours in 2_road_usages.csv
    :param road_usages_data_path: String, where file is loaded from.
    :return: New dataframe. If time-unit was between some hour, they were summed.
    """
    road_usages = pd.read_csv(road_usages_data_path)
    grouped_by_piste = group_by_column(road_usages, 'piste')

    result = map(handle_grouped_by_piste, grouped_by_piste)
    flat_result = flatten_list(result)

    return pd.DataFrame(flat_result)


if __name__ == '__main__':
    """
    Optional parameters:
    sys.argv[1] = csv-file to be handeled. Default is data/3_road_usages.csv
    sys.argv[2] = desired file name to be saved as
    """
    import sys
    pd.options.mode.chained_assignment = None  # default='warn'

    load_path = "data/2_road_usages.csv"
    save_path = "data/3_road_usages.csv"

    try:
        load_path = sys.argv[1]
        save_path = sys.argv[2]
    except:
        None

    print("load path: " + load_path)
    print("save path: " + save_path)

    result = main(load_path)
    result.to_csv(save_path, index = False) # do not write index column in the file

    print(result)
