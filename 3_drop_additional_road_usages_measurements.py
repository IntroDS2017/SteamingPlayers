import pandas as pd


def main():
    load_path = "data/2_road_usages.csv"
    save_path = "data/3_road_usages.csv"

    df = pd.read_csv(load_path)

    street_names = df.nimi.unique()
    points_to_drop = []

    for street in street_names:
        points = df[df['nimi'] == street].piste.unique()

        if len(points) > 1:
            print(street + " has the following measurement points: " + str(points))

            for i in range(1, len(points)):
                points_to_drop.append(points[i])

    print("\nDropping rows at measurement points " + str(points_to_drop))

    df = df[-df['piste'].isin(points_to_drop)]
    df.to_csv(save_path, index=False)


if __name__ == '__main__':
    main()
