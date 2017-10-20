import pandas as pd

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


def flatten_list(to_flat):
    """
    Flattens 2D-list to 1d
    :param to_flat: List to flatten
    :return: 1D list
    """
    return [row for rows in to_flat for row in rows]


def sum_over_autot_of_rows_sharing_aika(grouped_roads):
    """
    Sums car-amounts of given rows. Also time is increased by one to match accident-data. It is intended that group has
    the same 'aika'.
    :param grouped_roads: Car-amounts to sum.
    :return: First row of the group, with summed 'autot'
    """
    roads = grouped_roads[1]

    cars = roads['autot'].sum()

    result = roads.iloc[0].copy() # TODO: what does this do?
    result['autot'] = cars
    result['aika'] += 1

    return result


def handle_roads_by_id_and_suunta(grouped_roads):
    """
    Divides 'aika' column by 100, and groups rows by 'aika', and proceeds to pass this value to sum 'autot'.
    :param piste_suunta_grouped: grouped-by - groups-tuple.
    :return: Two rows with summed 'auto':t, for each 'suunta'
    """
    roads = grouped_roads[1]

    roads['aika'] = roads['aika'].apply(lambda x: int(x / 100)) # set for example each 700, 715, 730, and 745 to 7, for summing over them

    result = map(sum_over_autot_of_rows_sharing_aika, group_by_column(roads, 'aika'))
    return result # TODO: add flattening here?


def handle_roads_by_id(grouped_roads):
    """
    Splits rows by 'suunta', direction, and proceeds to sum 'auto'-column, cars for each hour.
    :param piste_grouped: grouped-by - groups tuple. Should be already grouped by 'piste', measurement point
    :return: flatten result of rows, which have summed 'auto', car-amount for each hour
    """
    roads = grouped_roads[1]
    result = map(handle_roads_by_id_and_suunta, group_by_column(roads, 'suunta'))
    return flatten_list(result)


def main(road_usages_data_path):
    """
    Merges hours in 2_road_usages.csv
    :param road_usages_data_path: String, where file is loaded from.
    :return: New dataframe. If time-unit was between some hour, they were summed.
    """
    roads = pd.read_csv(road_usages_data_path)

    result = map(handle_roads_by_id, group_by_column(roads, 'piste')) # piste = unique ID that stands for given road. Could use also 'nimi' here.
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

    load_path = "data/3_road_usages.csv"
    save_path = "data/4_road_usages.csv"

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
