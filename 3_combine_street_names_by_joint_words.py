import pandas as pd


def combine(street):
    return "_".join(street.split(" "))

def main():
    return

# Returns a list of street names of road_usages data which contain at least two words
def joint_street_names():
    unique_road_usages_streets = df_road_usages.nimi.unique()
    print(unique_road_usages_streets)

    return [street for street in unique_road_usages_streets if len(street.split(" ")) > 1]

if __name__ == '__main__':
    import sys

    accidents_load_path = "data/1_accidents.csv"
    road_usages_load_path = "data/3_road_usages.csv"

    accidents_save_path = "data/4_accidents.csv"
    road_usages_save_path = "data/4_road_usages.csv"

    df_accidents = pd.read_csv(accidents_load_path)
    df_road_usages = pd.read_csv(road_usages_load_path)

    print("Original accidents:")
    #print(df_accidents)
    print("\n")
    print("Original road usages:")
    #print(df_road_usages)

    j_sreets = joint_street_names()
    c_streets = map(combine, j_sreets)
    print(j_sreets)
    print(c_streets)

    main()

    # df_accidents.to_csv(accidents_save_path, index = False)
    # df_road_usages.to_csv(road_usages_save_path, index = False)

    print("New accidents:")
    #print(df_accidents)
    print("\n")
    print("New road usages:")
    #print(df_road_usages)
