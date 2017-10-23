import pandas as pd
import seaborn as sns

def calculate_ratio(accidents, traffic):
    if traffic == 0:
        return 0.0
    return 1.0*accidents/traffic


def main():
    """
    For testing different types of visualizations of the combined traffic and accidents
    dataset. 
    """

    df = pd.read_csv('data/7_combined_left_join.csv')

    
    #Data on the accidents per year on the streets of Helsinki
    accidents = df[['nimi', 'vuosi', 'Onnett_id']].groupby(['nimi', 'vuosi']).count()['Onnett_id']

    print(accidents)

    df_accidents = accidents.to_frame()
    df_accidents.reset_index(inplace=True)
    df_accidents.columns = ['Street', 'Year', 'Accidents']
    
    sns.set(font_scale = 2) #Increase the font size
    
    accidentplot = sns.factorplot(x='Street', y='Accidents', kind='bar', size=50, 
               data=df_accidents, hue='Year')
    accidentplot.set_xticklabels(rotation=90) 

    accidentplot.savefig('data/figures/1_accidentplot.png')
   
    #Data on the traffic (number of cars) per year on the streets of Helsinki
    traffic = df[['nimi', 'vuosi', 'autot']].groupby(['nimi', 'vuosi']).sum()['autot']
   
    traffic_df = traffic.to_frame()
    traffic_df.reset_index(inplace=True)
    traffic_df.columns = ['Street', 'Year', 'Cars']
    
    #A rough estimate of all traffic on a street during one year
    traffic_df['Autoja'] = traffic_df['Cars'].apply(lambda x: x*365)

    
    trafficplot = sns.factorplot(x='Street', y='Cars', kind ='bar', size=50, 
               data=traffic_df, hue='Year')

    trafficplot.set_xticklabels(rotation=90)

    trafficplot.savefig('data/figures/2_trafficplot.png')
    
    #A new combined dataset for calculating Accidents/Traffic ratio
    df_combined = pd.merge(traffic_df, df, how = 'left', 
                           left_on=['Street', 'Year'], 
                           right_on=['Street', 'Year'])
    
    
    df_combined['Accidents/Traffic']=df_combined.apply(lambda row: 
                  calculate_ratio(row.Onnettomuuksia,row.Autoja), axis=1)
        
    
    accident_ratioplot = sns.factorplot(x='Street', y='Accidents/Traffic', kind ='bar', size=50, 
               data=df_combined, hue='Year')

    accident_ratioplot.set_xticklabels(rotation=90)
    
    trafficplot.savefig('data/figures/3_accident_ratioplot.png')
      
    
    

if __name__ == '__main__':
    main()
