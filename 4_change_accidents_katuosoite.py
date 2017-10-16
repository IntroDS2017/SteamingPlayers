import pandas as pd

# Changes address into one of the unique road names in road_usages, or makes it empty if no comparison can be made.
def modify_katuosoite(address):
    for road_name in road_usages_names:
        if road_name in address:
            if (road_name != address.strip()):
                print("Address " + address + " changed into " + road_name)
            return road_name
    return "NOT_FOUND: " + address # TODO: hack to maintain the address information if still needed further on.


def main():
    print(df_accidents.Katuosoite.unique())
    print(len(df_accidents.Katuosoite.unique()))

    df_accidents['Katuosoite'] = df_accidents['Katuosoite'].map(modify_katuosoite)
    print(df_accidents.Katuosoite.unique())
    print(len(df_accidents.Katuosoite.unique()))

    df_accidents.to_csv("data/5_accidents.csv", index = False)


if __name__ == '__main__':

    accidents_load_path = "data/1_accidents.csv"
    road_usages_load_path = "data/4_road_usages.csv"

    df_accidents = pd.read_csv(accidents_load_path)
    df_road_usages = pd.read_csv(road_usages_load_path)

    accidents_save_path = "data/5_accidents.csv"

    road_usages_names = df_road_usages.nimi.unique()
    main()
