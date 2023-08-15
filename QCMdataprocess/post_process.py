
#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.signal import savgol_filter

# %%
# Applys filter to F and D plots
df = pd.read_csv('Au_235_00030_nCV_06_6_2023.csv')

Error = df[df == "Failed"].stack().index.tolist()

for value in Error:
    df[value[1]][value[0]] =df[value[1]][value[0]-1]
df = df.apply(pd.to_numeric)
for column in df.columns[1:-1]:
    df[column] = filtered_discharge=savgol_filter(df[column], 31, 1)
    df.plot(x='Time [s]', y=column)

#%%
Timeslice = [787, 3894]
Baseline = df[:Timeslice[0]]
CV = df[Timeslice[0]:Timeslice[1]]
Discharge = df[Timeslice[1]:]

#%%
#get data out of
echem_df = pd.read_csv('20230606_open_au.DTA', header= None)
echem_df.dropna(inplace = True)
echem_df = echem_df[0].str.split("\t", expand = True)
split = echem_df[echem_df[0].str.contains("CURVE")].index.tolist()
split.append(echem_df.index[-1])
zeros =echem_df[echem_df == "0"].stack().index.tolist()
name =echem_df[echem_df[0].str.contains("CURVE")][0].tolist()


df_dict = dict()
for i,j in enumerate(split):
    if i == 0:
        pass
    elif name[i-1] =='OCVCURVE':
        temp_df = echem_df[split[i-1]+3:j-34]
        time_delta =float(temp_df[2].iloc[-1])
    else:
        df_dict[name[i-1]] = echem_df[split[i-1]+3:j]
        df_dict[name[i-1]] = df_dict[name[i-1]].drop([0,9], axis=1)
        df_dict[name[i-1]] = df_dict[name[i-1]].apply(pd.to_numeric)
        df_dict[name[i-1]].insert(0, 'Source', name[i-1])
        df_dict[name[i-1]][2]= df_dict[name[i-1]][2]
keys = list(df_dict.keys())



total = pd.concat(df_dict.values(), ignore_index=True)
#%%
fig, ax = plt.subplots()
total.plot(ax = ax, x=3, y=4)
ax.set_xlim(0.5,1.5)
ax.set_ylim(-2E-5,.5E-5)

#%%
#get time

#shift

CV['Time [s]'] = CV['Time [s]']-  df['Time [s]'][Timeslice[0]] - time_delta

Adjusted = CV[CV['Time [s]'] > 0]
pos_freq = [x for x in CV['Time [s]'] if x >= 0]

Voltage = np.interp(pos_freq, total[2], total[3])

plt.plot(Voltage,Adjusted['f3 [Hz]'])

# %%
