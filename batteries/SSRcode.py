
#%%
import pandas as pd
import os


path = 'D:\projects\Data\ToProcess' #change this to file directory
modelfile = 'Refdata1.csv'
comparison = 'Refdata.xlsx'

# CPCN04 = "50CP50CNT0.4"
# CP04 = "CP0.4"
# 50CP50CNT0.5
# CP0.5
# 50CP50CNT0.6
# CP0.6
#%%

Capacity_test = [0.1,0.2, 0.3]
Voltage_test = [0, 0, 0]


def interpolate(voltage1, voltage2, capacity1, capacity2, capacity3):
    voltage3 =  (voltage2 - voltage1)*(capacity3-capacity1)/(capacity2-capacity1) +voltage1
    return voltage3

def locater(dataset, i, refcapacity):
    lowerneighbour_ind = RefData[dataset][Data[dataset]['Capacity'] < CodeData['Capacity'][i]]['Capacity'].idxmax()
    higherneighbour_ind = RefData[dataset][Data[dataset]['Capacity'] > CodeData['Capacity'][i]]['Capacity'].idxmin()
    capacity1 = RefData[dataset]['Capacity'][lowerneighbour_ind]
    capacity2 = RefData[dataset]['Capacity'][higherneighbour_ind]
    capacity3 = refcapacity
    voltage1 = RefData[dataset]['Voltage'][lowerneighbour_ind]
    voltage2 = RefData[dataset]['Voltage'][higherneighbour_ind]
    v3 = (interpolate(voltage1, voltage2, capacity1, capacity2, capacity3))
    print(i)
    SSR = (CodeData['Capacity'][i] - v3)**2
    return SSR


RefData = pd.read_excel(path + "/"+ comparison, sheet_name= None)
CodeData = pd.read_csv(path + "/"+ modelfile)

for x, y in enumerate(CodeData['Capacity']):
    SumSR += locater("50CP50CNT0.4", x, y)
    print(SumSR)

#result = [locater("50CP50CNT0.4", x, refcapcity) for x, refcapcity in enumerate(CodeData['Capacity'])]
#print(result)

# print (Data['50CP50CNT0.4']['Capacity'][row])
# lowerneighbour_ind = Data2[Data2['Capacity'] < Temp]['Capacity'].idxmax()
# higherneighbour_ind = Data2[Data2['Capacity'] > Temp]['Capacity'].idxmin()
# v3 = interpolate(Data2['Capacity'][higherneighbour_ind], voltage2,Data2['Capacity'][lowerneighbour_ind], Data2['Capacity'][higherneighbour_ind], capacity3)
# SSR += (Voltage_test[i] - v3)**2



# %%
# Official Playlist
# Small World - Bump of Chicken