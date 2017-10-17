#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Select from accident data the rows with those street names that are in traffic data

import pandas as pd

df_accidents = pd.read_csv('data/5_accidents.csv')

df_road_usages = pd.read_csv('data/4_road_usages.csv')

roads = list(df_road_usages.nimi.unique())

#print(roads)

#print(len(df_accidents))

df_selected_accidents = df_accidents[df_accidents.Katuosoite.isin(roads)]

#print(len(df_selected_accidents))

df_selected_accidents.to_csv('data/6_accidents.csv')

