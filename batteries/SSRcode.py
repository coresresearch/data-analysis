
#%%
import pandas as pd
import os


path = 'C:\Users\Mels\Code\Data\ToProcess' #change this to file directory
modelfile = 'file'
comparison = 'file'
#%%
capacity1 =5
capacity2 = 4
voltage1 = 2.92
voltage2 =2.93
capacity3 = 4.5



def interpolate(voltage1, voltage2, capacity1, capacity2, capacity3):
    voltage3 =  (voltage2 - voltage1)*(capacity3-capacity1)/(capacity2-capacity1) +voltage1
    return voltage3

def graph(file):
    Data = pd.read_table(path + "/"+ modelfile, sep=',', engine='python')
    Data2 = pd.read_table(path + "/"+ comparison, sep=',', engine='python')
    for row in Data['Capacity']:
        print (Data['Capacity'][row])
    # lowerneighbour_ind = Data2[Data2['Capacity'] < Temp]['Capacity'].idxmax()
    # higherneighbour_ind = Data2[Data2['Capacity'] > Temp]['Capacity'].idxmin()
    # v3 = interpolate(Data2['Capacity'][higherneighbour_ind], voltage2,Data2['Capacity'][lowerneighbour_ind], Data2['Capacity'][higherneighbour_ind], capacity3)




# %%
