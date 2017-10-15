import pandas as pd

# File hki_accidents.csv contains all traffic accidents in Helsinki area from 2011 to 2016.
# It has all the columns of the original dataset except Oslakpvm and Luovpvm.


def drop_column(col):
    if type(c) == int:
        df.drop(df.columns[c], axis = 1, inplace = True)

    else:
        df.drop(c, axis = 1, inplace = True)



df = pd.read_csv("data/hki_accidents.csv", encoding = 'utf-8')
print(df.columns.values)

# Clearly unnecessary columns

# 0 = index, 33 = Saasel, 58 = Paallsel, 73 = Maankaytse, 76 = LisaKaisse, 90 = Paallksel
obvious_cols = [0, 33, 58, 73, 76, 90, "Tienpitsel", "Vakavuus", "ELY", "Elynimi", "Poliisipri", "Piirinimi", "Ontyypsel", "Onlksel", "Taajamasel",
                "Pintasel","Valsel", "Onnpaiksel", "Liikvalsel", "Maakunta", "Maakuntsel", "Kunta", "Kuntasel", "Noplajisel", "Mo_molsel",
                "Toimlksel", "Risteyssel", "Rautatsel", "Muuliitsel", "Tietyypsel", "Talvhoitsel", "Tienverkse", "Valoohjsel","Solmutyyps",
                "Liitlksel", "Toimpidsel", "Valomsel", "Poikleikse"]

for c in obvious_cols:
    drop_column(c)


# Other not clearly obvious columns that should be dropped

# Tienverkas mostly unused and doesn't seem to provide any useful information.
# Valoohjaus == -1 for each entry.
other_cols = ["Tienverkas", "Valoohjaus"]

for c in other_cols:
    drop_column(c)

print "\n"
print(df.columns.values)

df.to_csv("data/hki_accidents_cleaned.csv", index = False, encoding = 'utf-8')