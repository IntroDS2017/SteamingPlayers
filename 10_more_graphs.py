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

    #print(accidents)

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
    
    #print(traffic)
   
    df_traffic = traffic.to_frame()
    df_traffic.reset_index(inplace=True)
    df_traffic.columns = ['Street', 'Year', 'Cars']
    
    #print(df_traffic)
    
    #A rough estimate of all traffic on a street during one year 
    #(divide by 1000 to make the plot prettier, but must fix it for the accident_ratioplot!)
    df_traffic['Cars'] = df_traffic['Cars'].apply(lambda x: x*365)
    
#    print('************************')
#    print(df_traffic)
    
    trafficplot = sns.factorplot(x='Street', y='Cars', kind ='bar', size=50, 
               data=df_traffic, hue='Year')

    trafficplot.set_xticklabels(rotation=90)

    trafficplot.savefig('data/figures/2_trafficplot.png')
    
    
    df_point = df[['nimi', 'piste']]
    
    #A new combined dataset for calculating Accidents/Traffic ratio
    df_combined = pd.merge(df_traffic, df_accidents, how = 'left', 
                           left_on=['Street', 'Year'], 
                           right_on=['Street', 'Year'])
    
    df_combined = pd.merge(df_combined, df_point, how = 'left', 
                           left_on=['Street'], 
                           right_on=['nimi'])
    
    
#    print('*************')
#    print(df_combined)
#    print('*************')
     
    df_combined['Accidents per Traffic']=df_combined.apply(lambda row: 
                  calculate_ratio(row.Accidents,row.Cars), axis=1)
    
    #A small dataset containing the accident-traffic ratio, street names and points
    df_combined.to_csv('data/8_accident_ratio.csv')
        
#    print('*************')
#    print(df_combined)
#    print('*************')
                  
    accident_ratioplot = sns.factorplot(x='Street', y='Accidents per Traffic', kind ='bar', size=50, 
               data=df_combined, hue='Year')

    accident_ratioplot.set_xticklabels(rotation=90)
    
    accident_ratioplot.savefig('data/figures/3_accident_ratioplot.png')
      
    
    

if __name__ == '__main__':
    main()
