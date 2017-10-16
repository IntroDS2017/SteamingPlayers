import pandas as pd

def modify_street(street):
    for i in range(len(old_names)):
        if street == old_names[i]:
            return new_names[i]
    return street

if __name__ == '__main__':

    load_path = "data/2_road_usages.csv"
    save_path = "data/3_road_usages.csv"

    df_road_usages = pd.read_csv(load_path)

    # TODO: remove rows with names "VALIMOT.+KIRKKOTIE", "MALMIK. + OJAM.", "PORVOONVÄYLÄ 1" and "PORVOONVÄYLÄ 2"
    # TODO: should we just drop rows with "VALIMOT.+KIRKKOTIE" and "MALMIK. + OJAM." instead? Those streets seem to be far from each other in map.
    old_names = ["V.PORVOONTIE", "VALIMOT.+KIRKKOTIE", "PORVOONVÄYLÄ 1", "PORVOONVÄYLÄ 2", "UUSI PORVOONTTIE", "KEHÄ III", "MALMIK.  + OJAM."]
    new_names = ["VANHA PORVOONTIE", "VALIMOTIE", "PORVOONVÄYLÄ", "PORVOONVÄYLÄ", "UUSI PORVOONTIE", "KEHÄ 3", "MALMINKATU"]

    print("\nOriginal unique road names count: " + str(len(df_road_usages.nimi.unique())))
    print("Original unique road names:")
    print(df_road_usages.nimi.unique())

    # Changes PORVOONVÄYLÄ 1 & 2 to PORVOONVÄYLÄ. PORVOONVÄYLÄ also itself already existed to begin with.

    df_road_usages['nimi'] = df_road_usages['nimi'].map(modify_street)

    df_road_usages.to_csv(save_path, index = False)


    print("\nNew unique road names count: " + str(len(df_road_usages.nimi.unique())))
    print("New unique road names:")
    print(df_road_usages.nimi.unique())
