import pandas as pd
import math

def drop_column(c):
    if type(c) == int:
        df.drop(df.columns[c], axis = 1, inplace = True)

    else:
        df.drop(c, axis = 1, inplace = True)


def float_to_binary(id):
    if not math.isnan(id):
        return 1
    return 0

def remove_unnecessrary_columns_df():

    index_cols = [0, 15]
    other_cols = ["Tienpit", "Tie", "Aosa", "Aet", "Ajr", "Vuosi", "Päivä", "Tunti", "Vkpv", "Taajmerk",
            "Pinta", "Valoisuus", "Sää", "Onnpaikka", "Liikvalot", "Liittyvtie", "Noplaji", "Nopsuunvas", "Nopsuunoik",
            "Taajama", "Mo_mol", "Toimluokka", "Tienlev", "X", "Y", "Päällyste", "Lämpötila", "Risteys", "Katuosoite",
            "Tietyyppi", "Lisäkaisty", "Solmutyyp", "Liitluok", "Lähliittie", "Suuntlkm", "Toimenpide", "Valaisomis",
            "Poikkileik", "Päällyslev", "Päällystlk"]

    for c in index_cols:
        drop_column(c)

    for c in other_cols:
        drop_column(c)

    df['Onnettomuus'] = df['Onnett_id'].map(float_to_binary)
    drop_column("Onnett_id")


if __name__ == '__main__':
    load_path = "data/7_combined.csv"
    save_path = "data/8_combined.csv"

    df = pd.read_csv(load_path)

    print("Original columns:\n")
    print(df.columns.values)

    remove_unnecessrary_columns_df()

    df.to_csv(save_path, index = False)

    print("\nNew columns:\n")
    print(df.columns.values)
