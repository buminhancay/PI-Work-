import pandas as pd
import numpy as np
import glob 

file_path = 'C:/Users/Bumin/Desktop/projects/first/pi_works/exhibitA-input.csv'

data = pd.read_csv(file_path, delimiter='\t' ,header=[0, 1, 2, 3])

play_id = []
play_id = data.values[:,0]
song_id = []
song_id = data.values[:,1]
client_id = []
client_id = data.values[:,2]
play_ts = []
play_ts = data.values[:,3]

distinc_num = []
for i in range(998):
    distinct_346 = 0
    yeni_arr = []
    for j in range(len(client_id)):
        if client_id[j] == i+1:
            yeni_arr.append(song_id[j])

    yeni_arr_unique = list(set(yeni_arr))
    distinc_num.append(len(yeni_arr_unique))
    #if len(yeni_arr_unique) == 25:
     #   distinct_346 = distinct_346 + 1
    del yeni_arr
    del yeni_arr_unique

#print(max(distinc_num))
#print(min(distinc_num))

print(distinc_num)            
