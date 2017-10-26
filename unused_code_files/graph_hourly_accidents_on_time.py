import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#def unique_roads(combined_df):
#    cols = ['ru-index','piste','nimi','x_gk25','y_gk25','aika','vuosi','ha','pa','ka','ra','la','mp','rv','autot']
#    combined_road_usages = combined_df.as_matrix(columns = cols)

#    _, unique_road_indexes = np.unique(combined_road_usages[:, 0], return_index = True)
#    return combined_road_usages[unique_road_indexes]

#def unique_accidents(combined_df):
#    cols = ['a-index','Onnett_id','Vuosi','Kk','Kuolleet','Loukkaant','Vakavuusko','Tunti','Ontyyppi','Onluokka','Osallkm','Nopraj','Kvl','Raskaskvl','Tietyö']
#    accidents = combined_df.as_matrix(columns = cols)

def form_road_accidents(road_index):
    rows = combined_road_usages[:, 0 == road_index]
    print(len(rows))



df = pd.read_csv('data/7_combined_left_join.csv')
nd_array = df.as_matrix(columns = None)

_, unique_road_indexes = np.unique(combined_road_usages[:, 0], return_index = True)

unique_roads = combined_road_usages[unique_road_indexes]

road_accidents = map(form_road_accidents, unique_roads)


print(unique_roads)
print(len(unique_roads))
