# LOAD DATA

import pandas as pd
df = pd.read_csv("lat_long_kota_kab.csv", index_col=0)


# DISTANCE CALCULATING FUNCTION

import haversine as hs
from haversine import Unit

def jarak(x, y):
    loc1 = (df.lat.iloc[x], df.long.iloc[x])
    loc2 = (df.lat.iloc[y], df.long.iloc[y])
    result = hs.haversine(loc1, loc2, unit=Unit.KILOMETERS)
    return result


# EXECUTION RESULT

df_list = []

for a in range (514):
    for i in range(514):
        temp_df = pd.DataFrame({'id_x': [df.id[a]],
                                'foreign_x': [df.foreign[a]],
                                'name_x': [df.name[a]],
                                'lat_x': [df.lat[a]],
                                'long_x': [df.long[a]],
                                'id_y': [df.id[i]],
                                'foreign_y': [df.foreign[i]],
                                'name_y': [df.name[i]],
                                'lat_y': [df.lat[i]],
                                'long_y': [df.long[i]],
                                'jarak': [jarak(a,i)]})
        df_list.append(temp_df)

# Concatenate all DataFrames in the list
final_df = pd.concat(df_list, ignore_index=True)

final_df.to_csv('regency.csv')