#%%
import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt
import os

# %%
path = 'C:/Users/Mels/Code/BatCan/outputsinputs'

def graph(file):
    Data = pd.read_csv(file, header= None)
    Data = Data.transpose()
    Data ['time (hr)'] = Data[0]/3600
    Data ['Current (mA/cm2)'] = Data[1]*0.1
    Data ['Capacity'] = Data ['time (hr)'] * Data ['Current (mA/cm2)']
    for cell in Data['Current (mA/cm2)']:
        if cell > 0:
            Current = str(cell) 
            break

    plt.figure(0) #fix this so we can take out that?
    p, = plt.plot(Data ['Capacity'], Data [22], \
            linewidth = 4., label = Current +'mAh/cm2')
    plt.xlabel('Capacity (mAh/cm2)', fontsize=14, fontname = 'Times New Roman')
    plt.ylabel('Potential (V)', fontsize=14, fontname = 'Times New Roman')
    plt.xticks(fontsize=14, fontname = 'Times New Roman') 
    plt.yticks(fontsize=14, fontname = 'Times New Roman') 
    plt.legend()

for file in os.listdir(path):
    graph(path + "/"+ file)
    print('Found')
# %%
