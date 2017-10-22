import pandas as pd


def main():
    load_path = "data/2_road_usages.csv"
    save_path = "data/3_road_usages.csv"

    df = pd.read_csv(load_path)

    street_names = df.nimi.unique()

    for street in street_names:
        points = df[df['nimi'] == street].piste.unique()

        if len(points) > 1:
            print(street + " has the following measurement points: " + str(points))

            for i in range(1, len(points)):
                print("Dropping rows at measurement point " + points[i])
                df.drop(df['piste'] == points[i])

    df.to_csv(save_path, index=False)


if __name__ == '__main__':
    main()
