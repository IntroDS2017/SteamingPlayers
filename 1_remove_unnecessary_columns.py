import pandas as pd

# File 0_accidents.csv contains all traffic accidents in Helsinki area from 2011 to 2016.
# It has all the columns of the original dataset except Oslakpvm and Luovpvm.

def drop_column(c):
    if type(c) == int:
        df_accidents.drop(df_accidents.columns[c], axis = 1, inplace = True)

    else:
        df_accidents.drop(c, axis = 1, inplace = True)

def process_df():
    # Clearly unnecessary columns

    # 0 = index
    obvious_cols = [0, "Tienpitsel", "Vakavuus", "Poliisipri", "Piirinimi", "Ontyypsel", "Onlksel", "Taajamasel", "Pintasel",
                    "Valsel", "Sääsel", "Onnpaiksel", "Liikvalsel", "Maakunta", "Maakuntsel", "Kunta", "Kuntasel", "Noplajisel",
                    "Mo_molsel", "Toimlksel", "Päällsel", "Risteyssel", "Rautatsel", "Muuliitsel", "Tietyypsel", "Talvhoitsel",
                    "Tienverkse", "Maankäytse", "Valoohjsel", "Lisäkaisse", "Solmutyyps", "Liitlksel", "Toimpidsel", "Valomsel",
                    "Poikleikse", "Päällksel"]

    for c in obvious_cols:
        drop_column(c)

    print("")

    # Find columns where each entry has the same value and delete them

    for c in df_accidents.columns.values:
        value = df_accidents[c][0]

        if len(df_accidents.loc[df_accidents[c] != value]) == 0:
            print("Unnecessary column removed: " + str(c))
            drop_column(c)

    # Tienverkas is mostly unused and doesn't seem to provide any useful information

    other_cols = ["Tienverkas", "Maankäyttö", "Talvhoitlk", "Nakos150",
                  "Nakos300", "Nakos460", "Runkotie", "Raskos"] # TODO: add more here

    for c in other_cols:
        drop_column(c)


if __name__ == '__main__':
    import sys

    load_path = "data/0_accidents.csv"
    save_path = "data/1_accidents.csv"

    try:
        load_path = sys.argv[1]
        save_path = sys.argv[2]
    except:
        None

    print("load path: " + load_path)
    print("save path: " + save_path)

    df_accidents = pd.read_csv(load_path)

    print("Original columns:\n")
    print(df_accidents.columns.values)

    process_df()

    df_accidents.to_csv(save_path, index = False)

    print("\nNew columns:\n")
    print(df_accidents.columns.values)
