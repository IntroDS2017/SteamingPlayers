import pandas as pd

# File hki_accidents.csv contains all traffic accidents in Helsinki area from 2011 to 2016.
# It has all the columns of the original dataset except Oslakpvm and Luovpvm.


def drop_column(col):
    if type(c) == int:
        df.drop(df.columns[c], axis = 1, inplace = True)

    else:
        df.drop(c, axis = 1, inplace = True)



df = pd.read_csv("data/hki_accidents.csv", encoding = 'utf-8')

print("Original columns:\n")
print(df.columns.values)

# Clearly unnecessary columns

# 0 = index, 33 = Saasel, 58 = Paallsel, 73 = Maankaytse, 76 = LisaKaisse, 90 = Paallksel
obvious_cols = [0, 33, 58, 73, 76, 90, "Tienpitsel", "Vakavuus", "ELY", "Elynimi", "Poliisipri", "Piirinimi", "Ontyypsel", "Onlksel", "Taajamasel",
                "Pintasel","Valsel", "Onnpaiksel", "Liikvalsel", "Maakunta", "Maakuntsel", "Kunta", "Kuntasel", "Noplajisel", "Mo_molsel",
                "Toimlksel", "Risteyssel", "Rautatsel", "Muuliitsel", "Tietyypsel", "Talvhoitsel", "Tienverkse", "Valoohjsel","Solmutyyps",
                "Liitlksel", "Toimpidsel", "Valomsel", "Poikleikse"]

for c in obvious_cols:
    drop_column(c)

print("")

# Find columns where each entry has the same value and delete them

for c in df.columns.values:
    value = df[c][0]

    if len(df.loc[df[c] != value]) == 0:
        print("Unnecessary column found: " + str(c))
        drop_column(c)

# Tienverkas is mostly unused and doesn't seem to provide any useful information

other_cols = ["Tienverkas"] # TODO: add more here

for c in other_cols:
    drop_column(c)

print("\nNew columns:\n")
print(df.columns.values)

df.to_csv("data/hki_accidents_cleaned.csv", index = False, encoding = 'utf-8')
