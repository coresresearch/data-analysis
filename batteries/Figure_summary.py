#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
plt.style.use('default')
plt.rcParams.update({'font.size': 18})
#%%

path = 'D:/projects/Data/ToProcess/Sensitivity.xlsx'
Sensitivity = pd.read_excel(path, sheet_name= None, header= 0)
keys = Sensitivity.keys()
#%%



plt.figure(figsize=(20, 16))
for n, key in enumerate(keys):
    ax1 = plt.subplot(3, 2, n + 1)
    columns = Sensitivity[key].columns
    ax1.set_ylim(Sensitivity[key][columns[1]].min()-0.05,Sensitivity[key][columns[1]].max()+0.05)

    if Sensitivity[key][columns[0]].min() <0.0003:
        ax1.set_xscale('log')
    ax1.plot(Sensitivity[key][columns[0]], Sensitivity[key][columns[1]], c='#648FFF', linestyle='-.', linewidth=5,label =columns[1], markersize =20, marker = 's')
    ax2 = ax1.twinx()
    ax2.plot(Sensitivity[key][columns[0]], Sensitivity[key][columns[2]], marker = 'o',linestyle='--', linewidth=5, c='#DC267F', label =columns[2], markersize =20)
    ax2.plot(Sensitivity[key][columns[0]], Sensitivity[key][columns[3]], marker = 'v', c='#FE6100',linestyle='-.', linewidth=5, label =columns[3], markersize =20)
    ax1.set_ylabel("Porosity [-]")
    ax2.set_ylabel("Δ%")
    ax1.set_xlabel(columns[0])
    ax2.yaxis.set_major_formatter(mtick.PercentFormatter())
    if n==2:
        ax1.set_xlim(1.E-10,5E-8)
        # ax2.set_ylim(-200,900)
    if n==3:
        ax2.set_ylim(-100,350)

h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
plt.subplots_adjust(wspace=0.40, hspace=0.25)
ax1.legend(h1+h2, l1+l2, ncol = 3, bbox_to_anchor =(0.4,2.5))

plt.savefig('Results'+ '.png', format='png', dpi=300, bbox_inches = "tight")

# %%

# fig, ax1 = plt.subplots()
# ax1.set_xscale('log')

# ax1.scatter(Sensitivity['Li_Diff'][columns[0]], Sensitivity['Li_Diff'][columns[1]], c='#648FFF', label =columns[1])
# ax2 = ax1.twinx()
# ax2.scatter(Sensitivity['Li_Diff'][columns[0]], Sensitivity['Li_Diff'][columns[2]], marker = 's', c='#DC267F', label =columns[2])
# ax2.scatter(Sensitivity['Li_Diff'][columns[0]], Sensitivity['Li_Diff'][columns[3]], marker = 'v', c='#FE6100', label =columns[3])
# ax1.set_ylabel("Porosity [-]")
# ax2.set_ylabel("Δ%")
# ax1.set_xlabel(columns[0])
# ax2.yaxis.set_major_formatter(mtick.PercentFormatter())
# fig.legend(ncol = 3)
