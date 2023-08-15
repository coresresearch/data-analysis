#%%
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
plt.style.use('default')
plt.rcParams.update({'font.size': 22})

#%%
color = ['#FF7276','#77DD77','#8BD3E6','#EFBE7D']
path = 'D:/projects/Data/charge_discharge_curve'
fig, ax = plt.subplots(figsize=[10, 6])
for color_counter, file in enumerate(os.listdir(path)):
    Data = pd.read_csv(path+'/'+file, header=None)
    final = len(Data.columns)
    spacing = np.arange(0,final,2)
    for i in spacing:
        if i ==spacing[-1]:
            linewidth=3
            linestyle = 'dashed'
            cap = 'experimental mean'
        else:
            linewidth = 2
            linestyle = 'dotted'
            cap = 'experimental'
        ax.plot(Data[i],Data[i+1], color=color[color_counter], linewidth=linewidth, linestyle = linestyle, label = cap)


path1 = 'D:\projects\Data\model'
current_legend= ['0.1 mA cm-2','0.2 mA cm-2','0.5 mA cm-2','1 mA cm-2']

color2 = ['#00873E','#4D4DFF','#ED8B00','#FF033E']
for color_counter, file in enumerate(os.listdir(path1)):
    Data2 = pd.read_csv(path1+'/'+file, header=0)
    ax.plot(Data2['capacity'],Data2['phi_ed'], color=color2[color_counter], linewidth=4, label = current_legend[color_counter])

ax.plot([0,1],[-1,-1], color='black', linewidth=4,linestyle = 'dashed', label ='experimental mean')
ax.plot([0,1],[-1,-1], color='black', linewidth=4,linestyle = 'dotted', label ='experimental')
h, l = ax.get_legend_handles_labels()
ax.set_ylim([2.2, 3.0])
plt.xlabel('Capacity [mAh cm2]')
plt.ylabel('Voltage [V]')
plt.legend(h[-6:],l[-6:], ncol = 3, fontsize =14, bbox_to_anchor =(0.5,1.20), loc="upper center")

plt.savefig('Validation'+ '.png', format='png', dpi=1200, bbox_inches = "tight")


# %%
