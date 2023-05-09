#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('default')
plt.rcParams.update({'font.size': 17})
#%%
path = 'D:\projects\Data\ToProcess'
ThermoProps = pd.read_excel(path + "/"+ "Thermo_props.xlsx", sheet_name= None, header= 0)
# %%

keys=list(ThermoProps.keys())

plt.figure(figsize=(7, 16))

solvents = ['PC:DME+LiPF₆','TEGDME+LiTFSI','TEGDME+LiClO₄','DME+LiTFSI','DMSO+LiTFSI']
color_pal = ['#f61717','#1e8fd4','#9ad0f1','#30B700','#8e58e7']
shape = ['C','M','U']
shape_pal = ['black','none', 'none']
colors = dict(zip(solvents,color_pal))
shapes = dict(zip(shape,shape_pal))



for n, key in enumerate(keys):
    ax = plt.subplot(4, 1, n + 1)
    color_set = []
    shape_set = []

    columns = ThermoProps[key].columns
    for row in ThermoProps[key]['Solvent']:
        color_set.append(colors[row])

    for row in ThermoProps[key]['Calculated']:
        shape_set.append(shapes[row])

    abridged = ThermoProps[key][['Molarity (M)',columns[1]]]
    abridged.plot.scatter( 'Molarity (M)',columns[1], ax=ax, c = color_set, s = 120, edgecolor=shape_set)
    if n == 0 or n==1:
        ax.set_yscale('log')
        if n==0:
            ax.set_ylim(1.E-13,1.E-8)
        # ax.sharey(ax)
    else:
        ax.set_yscale('linear')
        # ax.sharey(ax)
        pass
for number, color in enumerate(color_pal):
        ax.scatter([0],[-1], color=color, label =solvents[number] )
ax.scatter([0],[-100], color='white', label ='Calculated', edgecolor='black' )
ax.set_ylim(0,10)
plt.legend(ncol = 3, fontsize =14, bbox_to_anchor =(1.1,4.1))
plt.subplots_adjust(wspace=0.3, hspace=0.3)
plt.savefig('Properties'+ '.png', format='png', dpi=900, bbox_inches = "tight")
# ax.plot(ThermoProps[keys[0]]['Molarity (M)'],ThermoProps[keys[0]][columns[1]], marker = 'o', linestyle = 'none', markersize=10, color = 'red')
# plt.yscale("log")
# for key in ThermoProps.keys():
#     ax.plot(ThermoProps[key]['Molarity (M)'],ThermoProps[2])

# %%
