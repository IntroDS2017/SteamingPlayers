import pandas as pd
import numpy as np

def flatten_list(to_flat):
    """
    Flattens 2D-list to 1d
    :param to_flat: List to flatten
    :return: 1D list
    """
    return [row for rows in to_flat for row in rows]


def sum_over_car_counts_of_rows_sharing_aika(grouped_roads):
    """
    Sums car-amounts of given rows.
    :param grouped_roads: Roads that are supposed to share (piste/nimi, year, and suunta).
    :return: First road of the roads, with summed 'autot'
    """
    roads = grouped_roads[1]

    result = roads.iloc[0].copy() # copies the first row as the result field

    for col in ['ha', 'pa', 'ka', 'ra', 'la', 'mp', 'rv', 'autot']:
        result[col] = roads[col].sum()

    return result


def handle_roads_by_id_and_vuosi(grouped_roads):
    roads = grouped_roads[1]
    return map(sum_over_car_counts_of_rows_sharing_aika, roads.groupby('aika'))


def handle_roads_by_id(grouped_roads):
    # grouped_rows[0] = list of "groupping value" (in this case 'piste' as previously grouped with that value)
    # grouped_rows[1] = "grouped rows (= road_usages_rows)"

    roads = grouped_roads[1]
    result = map(handle_roads_by_id_and_vuosi, roads.groupby('vuosi'))
    return flatten_list(result)


def main(road_usages_data_path):
    """
    Merges hours in 2_road_usages.csv
    :param road_usages_data_path: String, where file is loaded from.
    :return: New dataframe. If time-unit was between some hour, they were summed. Sums also over both 'suunta's!
    """
    roads = pd.read_csv(road_usages_data_path)
    roads['aika'] = roads['aika'].apply(lambda x: int(x / 100) + 1) # set for example each 700, 715, 730, and 745 to 8, for summing over them

    result = map(handle_roads_by_id, roads.groupby('piste')) # piste = unique ID that stands for given road. Could use also 'nimi' here.
    flat_result = flatten_list(result)

    return pd.DataFrame(flat_result)


if __name__ == '__main__':
    pd.options.mode.chained_assignment = None  # default='warn'

    load_path = "data/3_road_usages.csv"
    save_path = "data/4_road_usages.csv"

    df = main(load_path)
    df = df.drop('suunta', 1)

    indexes = np.arange(len(df))

    df['road-usage-index'] = indexes
    df.to_csv(save_path, index = False) # do not write index column in the file

    print(df)
