import pandas as pd

def flatten_list(to_flat):
    """
    Flattens 2D-list to 1d
    :param to_flat: List to flatten
    :return: 1D list
    """
    return [row for rows in to_flat for row in rows]


def sum_over_autot_of_rows_sharing_aika(grouped_roads):
    """
    Sums car-amounts of given rows.
    :param grouped_roads: Roads that are supposed to share (piste/nimi, year, and suunta).
    :return: First road of the roads, with summed 'autot'
    """
    roads = grouped_roads[1]

    cars = roads['autot'].sum()

    result = roads.iloc[0].copy() # copies the first row as the result field
    result['autot'] = cars
    return result


def handle_roads_by_id_vuosi_and_suunta(grouped_roads):
    roads = grouped_roads[1]
    return map(sum_over_autot_of_rows_sharing_aika, roads.groupby('aika'))


def handle_roads_by_id_and_vuosi(grouped_roads):
    roads = grouped_roads[1]
    result = map(handle_roads_by_id_vuosi_and_suunta, roads.groupby('vuosi'))
    return flatten_list(result)


def handle_roads_by_id(grouped_roads):
    # grouped_rows[0] = list of "groupping value" (in this case 'piste' as previously grouped with that value)
    # grouped_rows[1] = "grouped rows (= road_usages_rows)"

    roads = grouped_roads[1]
    result = map(handle_roads_by_id_and_vuosi, roads.groupby('suunta'))
    return flatten_list(result)


def main(road_usages_data_path):
    """
    Merges hours in 2_road_usages.csv
    :param road_usages_data_path: String, where file is loaded from.
    :return: New dataframe. If time-unit was between some hour, they were summed.
    """
    roads = pd.read_csv(road_usages_data_path)
    roads['aika'] = roads['aika'].apply(lambda x: int(x / 100) + 1) # set for example each 700, 715, 730, and 745 to 8, for summing over them

    result = map(handle_roads_by_id, roads.groupby('piste')) # piste = unique ID that stands for given road. Could use also 'nimi' here.
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
