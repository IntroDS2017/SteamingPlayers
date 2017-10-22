import pandas as pd


if __name__ == '__main__':

    load_path = "data/8_combined.csv"
    save_path = "data/9_combined.csv"

    df = pd.read_csv(load_path)

    street_names = df.nimi.unique()
    street_names_points = []

    for name in street_names:
        points = df[df['nimi'] == name].piste.unique()

        if len(points) > 1:
            print(name + " has the following measurement points: " + str(points))

            for i in range(1, len(points)):
                print("Dropping rows at measurement point " + points[i])
                df.drop(df['piste'] == points[i])

    df.to_csv(save_path, index=False)
