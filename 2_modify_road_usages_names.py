import pandas as pd


def modify_street(street):
    for i in range(len(old_names)):
        if street == old_names[i]:
            return new_names[i]
    return street


def drop_rows_by_road_names(road_names, df):
    return df[-df['nimi'].isin(road_names)]


if __name__ == '__main__':

    load_path = "data/2_road_usages.csv"
    save_path = "data/3_road_usages.csv"

    df_road_usages = pd.read_csv(load_path)

    old_names = ["V.PORVOONTIE", "UUSI PORVOONTTIE", "KEHÄ III"]
    new_names = ["VANHA PORVOONTIE", "UUSI PORVOONTIE", "KEHÄ 3"]

    print("\nOriginal unique road names count: " + str(len(df_road_usages.nimi.unique())))
    print("Original unique road names:")
    print(df_road_usages.nimi.unique())

    # Removing unclear road-names.
    roads_to_drop = ["VALIMOT.+KIRKKOTIE", "MALMIK.  + OJAM.", "PORVOONVÄYLÄ 1", "PORVOONVÄYLÄ 2"]
    df_road_usages = drop_rows_by_road_names(roads_to_drop, df_road_usages)

    # Renaming road names to match the other data-set
    df_road_usages['nimi'] = df_road_usages['nimi'].map(modify_street)

    df_road_usages.to_csv(save_path, index=False)


    print("\nNew unique road names count: " + str(len(df_road_usages.nimi.unique())))
    print("New unique road names:")
    print(df_road_usages.nimi.unique())
