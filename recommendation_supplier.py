# DATA PREPROCESSING

import pandas as pd

df = pd.read_excel('komoditas.xlsx', 'Feb_1', index_col=0)

recommended_regency = df[df.rekomendasi=="YES"]
recommended_regency = pd.DataFrame({'id': recommended_regency.id, 
                                    'foreign': recommended_regency.foreign, 
                                    'name': recommended_regency.name, 
                                    'lat': recommended_regency.lat, 
                                    'long': recommended_regency.long,
                                    'neraca': recommended_regency.neraca})
recommended_regency = recommended_regency.reset_index()

deficit_regency = df[df.status=="DEFISIT"]
deficit_regency = pd.DataFrame({'id': deficit_regency.id, 
                                    'foreign': deficit_regency.foreign, 
                                    'name': deficit_regency.name, 
                                    'lat': deficit_regency.lat, 
                                    'long': deficit_regency.long,
                                    'neraca': deficit_regency.neraca})
deficit_regency = deficit_regency.reset_index()


# DISTANCE CALCULATING

import haversine as hs
from haversine import Unit

df_list = []

def jarak(x, y):
    loc1 = (deficit_regency.lat.iloc[x], deficit_regency.long.iloc[x])
    loc2 = (recommended_regency.lat.iloc[y], recommended_regency.long.iloc[y])
    result = hs.haversine(loc1, loc2, unit=Unit.KILOMETERS)
    return result

for a in range (len(deficit_regency)):
    for i in range (len(recommended_regency)):
        temp_df = pd.DataFrame({'daerah_defisit' : [deficit_regency.name[a]], 'neraca_defisit' : [deficit_regency.neraca[a]],
                                'daerah_rekomendasi' : [recommended_regency.name[i]], 'neraca_surplus' : [recommended_regency.neraca[i]],
                                'jarak': [jarak(a,i)]})
        df_list.append(temp_df)


hasil = pd.concat(df_list, ignore_index=True)
hasil.sort_values(by='jarak')
hasil