import pandas as pd
import seaborn as sns


def main():
    """
    For testing different types of visualizations of the combined traffic and accidents
    dataset. 
    """

    df = pd.read_csv('data/9_combined.csv')

    df_accidents = df.loc[df['Onnettomuus'] == 1]

    #Data on the accidents per year on the streets of Helsinki
    accidents = df_accidents[['nimi', 'vuosi', 'Onnettomuus']].groupby(['nimi', 'vuosi']).count()['Onnettomuus']

    print(accidents)

    df_accidents = accidents.to_frame()
    df_accidents.reset_index(inplace=True)
    df_accidents.columns = ['Katuosoite', 'Vuosi', 'Onnettomuuksia']
    
    sns.set(font_scale = 2) #Increase the font size
    
    accidentplot = sns.factorplot(x='Katuosoite', y='Onnettomuuksia', kind='bar', size=50, 
               data=df_accidents, hue='Vuosi')
    accidentplot.set_xticklabels(rotation=90) 

    accidentplot.savefig('data/figures/1_accidentplot.png')
   
    #Data on the traffic (number of cars) per year on the streets of Helsinki
    traffic = df[['nimi', 'vuosi', 'autot']].groupby(['nimi', 'vuosi']).sum()['autot']
   
    traffic_df = traffic.to_frame()
    traffic_df.reset_index(inplace=True)
    traffic_df.columns = ['Katu', 'Vuosi', 'Autoja']

    
    trafficplot = sns.factorplot(x='Katu', y='Autoja', kind ='bar', size=50, 
               data=traffic_df, hue='Vuosi')

    trafficplot.set_xticklabels(rotation=90)

    trafficplot.savefig('data/figures/2_trafficplot.png')
    
    

if __name__ == '__main__':
    main()
