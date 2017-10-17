#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd


def main(roadpath='data/4_road_usages.csv', accidentpath='data/6_accidents.csv'):
    """
    Combine the road usage data with the accident data based on the street address,
    hour and year.
    """

    df_road_usages = pd.read_csv(roadpath)
    df_accidents = pd.read_csv(accidentpath)

    df_combined = pd.merge(df_road_usages, df_accidents, how = 'left', 
                           left_on=['nimi', 'aika', 'vuosi'], 
                           right_on=['Katuosoite', 'Tunti', 'Vuosi'])

    #print(combineddf.columns)

    #print(combineddf)

    df_combined.to_csv('data/7_combined.csv')
    

if __name__ == '__main__':
    main()



