#%% 
import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt
import os
#edit these to process your data.
path = 'C:/Users/Mels/Downloads/drive-download-20210924T155724Z-001/ToProcess' #change this to file directory
key = 'Absorbance'
filenames = os.listdir(path)
legend = ['0 M','0.5 M', '0.75 M', '1 M', '1.25 M', '1.5 M', '2 M', '3.5 M', '5 M']
peaks = [740, 786, 1053, 1180, 1230, 1327, 1451, 2880]

n_exp = 9
cmap = plt.get_cmap('copper')
color_ind = np.linspace(0,1,n_exp)
colors = list()
for i in np.arange(n_exp):
    colors.append(cmap(color_ind[i]))

for filename in filenames:
    os.rename(os.path.join(path, filename), os.path.join(path, filename.replace(' ', '-')))
#%%
i = 0
def graph(file):
    Data = pd.read_table(file, sep=',', engine='python', header=None)
    Data = Data.drop(2, axis=1)
    Data['graph_x'] =Data.iloc[2:, 0].astype(float)
    Data['graph_y'] =Data.iloc[2:, 1].astype(float)
    
    
    plt.figure(0)
    plt.plot(Data['graph_x'] ,Data['graph_y'],  linewidth = 2., label =legend[i],  color = colors[i]) 
    Data = Data.fillna(0.0)
    # print(Data['graph_x'].apply(type))
    #test = Data.set_index('graph_x').sub(740.0).abs().idxmin()
    
    intensity = []
    for peak in peaks:
        lowerneighbour_ind = Data[Data['graph_x'] < peak]['graph_x'].idxmax()
        higherneighbour_ind = Data[Data['graph_x'] > peak]['graph_x'].idxmin()
        average = (Data['graph_y'][lowerneighbour_ind] + Data['graph_y'][higherneighbour_ind])/2
        intensity.append(average)
    intensity = np.array(intensity)
    return intensity
 
exp_intensity = np.empty([0,len(peaks)])

for file in os.listdir(path):
    if file.find(key) > -1: #change this so the file is reconized
        intensity = graph(path + "/"+ file)
        exp_intensity = np.append(exp_intensity, np.array([intensity]), axis = 0); exp_intensity
        i = i+1

plt.legend()
plt.xlabel('Cycle', fontsize=14, fontname = 'Times New Roman')
plt.ylabel('Capacity (mAh/g-carbon)', fontsize=12, fontname = 'Times New Roman')

ax = plt.gca()
for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_fontsize(12)
    tick.label1.set_fontname('Times New Roman')

for tick in ax.yaxis.get_major_ticks():
    tick.label1.set_fontsize(12)
    tick.label1.set_fontname('Times New Roman')
       
        

# %%
