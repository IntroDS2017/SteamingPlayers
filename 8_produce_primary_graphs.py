import sys
import pandas as pd
import seaborn as sns

def calculate_ratio(accidents, traffic):
    if traffic == 0:
        return 0.0
    return 1.0 * accidents / traffic


def get_car_counts_by_road_indexes(df):
    prev_ru_index = -1
    cars = []

    # Returns data for a new column where car count is the original count for first occured ru_index entry, and 0 otherwise.
    # This will avoid summing over the car count of the same road again when calculating traffic.

    traffic_data = df[['ru-index', 'nimi', 'vuosi', 'autot']]

    for i in range(len(traffic_data)):
        row = traffic_data.values[i]

        if prev_ru_index != row[0]:
            prev_ru_index = row[0]
            cars.append(row[3])
        else:
            cars.append(0)

    return cars


# Data on the accidents per year on the streets of Helsinki
def procude_yearly_accidents_plot(df):
    accidents = df[['nimi', 'vuosi', 'Onnett_id']].groupby(['nimi', 'vuosi']).count()['Onnett_id']

    df_accidents = accidents.to_frame()
    df_accidents.reset_index(inplace=True)
    df_accidents.columns = ['Street', 'Year', 'Accidents']

    sns.set(font_scale = 2) #Increase the font size

    accidentplot = sns.factorplot(x='Street', y='Accidents', kind='bar', size=50, data=df_accidents, hue='Year')
    accidentplot.set_xticklabels(rotation=90)

    accidentplot.savefig('data/figures/1_accidentplot.png')

    return df_accidents


# Data on the traffic (number of cars) per year on the streets of Helsinki
def procude_yearly_traffic_plot(df):
    df['uusi_autot'] = get_car_counts_by_road_indexes(df)
    traffic = df.groupby(['nimi', 'vuosi']).sum()['uusi_autot']

    # Alkuperäijnen ongelma:
    # EHRENSTRÖMINTIE v. 2014 oli alussa 2917 (sum()['autot']. Nyt: 2533 (joka siis nykyinen, oikea lukuarvo)
    # 2917 = 2533 + 2 * 192 (ja ru-indexillä 6713 3 riviä, joiden 'autot' siis 192)

    df_traffic = traffic.to_frame()
    df_traffic.reset_index(inplace=True)
    df_traffic.columns = ['Street', 'Year', 'Cars']

    # A rough estimate of all traffic on a street during one year

    df_traffic['Cars'] = df_traffic['Cars'].apply(lambda x: x*365)

    trafficplot = sns.factorplot(x='Street', y='Cars', kind='bar', size=50, data=df_traffic, hue='Year')

    trafficplot.set_xticklabels(rotation=90)
    trafficplot.savefig('data/figures/2_trafficplot.png')

    return df_traffic


def produce_accidents_per_traffic_ratio_plot(df, df_accidents, df_traffic):
    df_point = df[['nimi', 'piste']]

    # A new combined dataset for calculating Accidents/Traffic ratio
    df_ratio = pd.merge(df_traffic, df_accidents, how = 'left', left_on=['Street', 'Year'], right_on=['Street', 'Year'])

    df_ratio = pd.merge(df_ratio, df_point, how = 'left', left_on=['Street'], right_on=['nimi'])

    df_ratio['Accidents per Traffic' ] = df_ratio.apply(lambda row: calculate_ratio(row.Accidents, row.Cars), axis=1)

    accident_ratioplot = sns.factorplot(x='Street', y='Accidents per Traffic', kind ='bar', size=50, data=df_ratio, hue='Year')

    accident_ratioplot.set_xticklabels(rotation=90)
    accident_ratioplot.savefig('data/figures/3_accident_ratioplot.png')

    return df_ratio


def main():
    """
    For producing different types of graphs using the combined traffic and accidents dataset.
    """

    data_path = 'data/7_combined_left_join.csv'

    try:
        data_path = sys.argv[1]
    except:
        None

    df = pd.read_csv(data_path)

    print("Producing yearly accidents plot..")
    df_accidents = procude_yearly_accidents_plot(df.copy())

    print("Producing yearly traffic plot..")
    df_traffic = procude_yearly_traffic_plot(df.copy())

    print("Producing accidents per traffic ratio plot..")
    df_traffic_accident_ratio = produce_accidents_per_traffic_ratio_plot(df.copy(), df_accidents, df_traffic)

    df_traffic_accident_ratio.to_csv('data/8_traffic_accidents_ratio.csv')


if __name__ == '__main__':
    main()
