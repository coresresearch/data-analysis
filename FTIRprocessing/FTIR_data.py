#%% 
import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt
import os
from scipy.signal import find_peaks
from operator import truediv
from datetime import datetime 
#edit these to process your data.
path = 'C:/Users/Mels/Downloads/12_13_21/12_13_21/Toprocess' #change this to file directory
key = 'csv'
filenames = os.listdir(path)

datatype = "composition"  # options are "time" or "composition"

if datatype == "time":
    legend = []
elif datatype == "composition":
    #legend = ['0 M','0.5 M', '0.75 M', '1 M', '1.25 M', '1.5 M', '2 M', '3.5 M', '5 M']
    #legend2 = [0, 0.5, 0.75, 1, 1.25, 1.5, 2, 3.5, 5]
    legend = ['0 M','0.25 M','0.5 M','0.75 M', '1 M']
    legend2 = [0, 0.5, 0.75, 1, 1.25]
peaks = [850, 1099,1199, 1350, 1453, 2158, 2870]


n_exp =5
cmap = plt.get_cmap('rainbow')
color_ind = np.linspace(0,1,n_exp)
colors = list()
for i in np.arange(n_exp):
    colors.append(cmap(color_ind[i]))

for filename in filenames:
    os.rename(os.path.join(path, filename), os.path.join(path, filename.replace(' ', '-')))
#%%
i = 0
time_steps =[]
def graph(file):
    Data = pd.read_table(file, sep=',', engine='python', header=None)
    time = Data.iloc[0][1].split(' ')
    time = time[4]
    time = datetime.strptime(time, "%H:%M:%S")
    Data = Data.drop(2, axis=1)
    Data['graph_x'] =Data.iloc[2:, 0].astype(float)
    Data['graph_y'] =Data.iloc[2:, 1].astype(float)
    
    if datatype == "time":
        plt.figure(0)
        plt.plot(Data['graph_x'] ,Data['graph_y'],  linewidth = 1.5, label = time, color = colors[i])
    elif datatype ==  "composition":
        plt.figure(0)
        plt.plot(Data['graph_x'] ,Data['graph_y'],  linewidth = 1., label =legend[i],  color = colors[i]) 
    Data = Data.fillna(0.0)
    # print(Data['graph_x'].apply(type))
    found_peaks, _ = find_peaks(Data['graph_y'])

    intensity = []
    for peak in peaks:
        Data['locator'] =(Data['graph_x'][found_peaks]-peak).abs()
        Data = Data.fillna(5000)
        peak_index = Data.iloc[(Data['locator']).argsort()[:1]]
        peak_index_2 = peak_index.index.tolist()
        value = Data['graph_y'][peak_index_2[0]]
        intensity.append(value)
    intensity = np.array(intensity)
    
    return intensity, time
 
exp_intensity = np.empty([0,len(peaks)])

for file in os.listdir(path):
    if file.find(key) > -1: #change this so the file is reconized
        intensity, time = graph(path + "/"+ file)
        time_steps.append(time)
        exp_intensity = np.append(exp_intensity, np.array([intensity]), axis = 0); exp_intensity
        i = i+1

plt.legend(loc = "upper left", ncol=3)
plt.xlabel('Wavelength [cm-1]', fontsize=14, fontname = 'Times New Roman')
#plt.ylim([0.00, 0.5])
#plt.xlim([700, 1200])
plt.ylabel('Absorbance', fontsize=12, fontname = 'Times New Roman')

ax = plt.gca()
for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_fontsize(12)
    tick.label1.set_fontname('Times New Roman')

for tick in ax.yaxis.get_major_ticks():
    tick.label1.set_fontsize(12)
    tick.label1.set_fontname('Times New Roman')

#%%
test = [(time_steps[d] - time_steps[0]).total_seconds() for d in range(len(time_steps))]
#puts all the intensity for 
Peak_dic ={}
for peak_loc, peak_value in enumerate(peaks):
    Peak_dic['peak_'+str(peak_value)] = []
    for time_loc in range(len(time_steps)):
        Peak_dic['peak_'+str(peak_value)].append(exp_intensity[time_loc][peak_loc])

print(Peak_dic)


#%%
# ratio_1230_1451 = list(map(truediv, Peak_dic['peak_1230'],Peak_dic['peak_1451']))
# ratio_1327_1451 = list(map(truediv, Peak_dic['peak_1327'],Peak_dic['peak_1451']))
# ratio_1351_1451 = list(map(truediv, Peak_dic['peak_1351'],Peak_dic['peak_1451']))


plt.figure(1)
plt.scatter(time_steps,Peak_dic['peak_2870'],  linewidth = 2., label =time,  color = 'r')
# plt.scatter(legend2 ,ratio_1327_1451,  linewidth = 2., label =time,  color = 'g')
# plt.scatter(legend2  ,ratio_1351_1451,  linewidth = 2., label =time,  color = 'b')

# %%
plt.figure(2)
plt.scatter(test,Peak_dic['peak_2870'],  linewidth = 2.,  color = 'r')
plt.xlabel('time [s]', fontsize=14, fontname = 'Times New Roman')
plt.ylabel('Absorbance', fontsize=12, fontname = 'Times New Roman')
#plt.ylim([0.690, 0.700])
ax = plt.gca()
for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_fontsize(12)
    tick.label1.set_fontname('Times New Roman')

for tick in ax.yaxis.get_major_ticks():
    tick.label1.set_fontsize(12)
    tick.label1.set_fontname('Times New Roman')


# %%
