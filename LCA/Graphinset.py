#%%

import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import pandas as pd
import os
import numpy as np
import matplotlib.ticker as mtick
#%%
path = 'D:\projects\Data\ToProcess'
RefData = pd.read_excel(path + "/"+ "Summary.xlsx", sheet_name= None, header= None)
plt.style.use('default')
plt.rc('font', size=12) #controls default text size

#%%
key = 'Salts'
#%% Bar chart with inset
x = RefData[key][0]
energy = RefData[key][1]
X2 = RefData[key][0][3:]
energy2 = RefData[key][1][3:]

x_pos = [i for i, _ in enumerate(x)]
x_pos2 = [i for i, _ in enumerate(X2)]

fig, ax = plt.subplots()
plt.bar(x_pos, energy, color=['blue'])

# for i in range(len(patterns)):
#     if i == 3:
#         ax.bar(i, height =energy[i], color='red', edgecolor='blue', hatch=patterns[i])
plt.xlabel(key, fontsize = 14, color = 'black')
plt.ylabel("GHG Emissions [$kg_{CO_2eq}$ $kg^{-1}_{material}$]", fontsize = 14, color='black')
#plt.title("Energy output from various fuel sources")
plt.xticks(x_pos, x)
ax.tick_params(axis="y",direction="in", colors='black')
plt.tick_params(bottom = False)
plt.yticks(color= 'black')
plt.xticks(rotation=45, color= 'black')

axins = inset_axes(ax, width="56%", height="76%", loc="upper right")

#plt.bar(x_pos2, energy2, color=['blue', 'blue', 'blue', 'red', 'red', 'red', 'red', 'red','red', 'red'], edgecolor=['blue', 'blue', 'blue', 'blue', 'red', 'red', 'red', 'red','red', 'red'], hatch ='\\')
plt.bar(x_pos2, energy2, color=['blue'])
plt.xticks(x_pos2, X2)
ax.tick_params(axis="y",direction="in", colors='black')
plt.tick_params(bottom = False)
plt.yticks(color= 'black')
plt.ylim(0,14)
plt.xticks(rotation=45, color= 'black')


plt.savefig('D:\projects\Data\Figures'+"/" + key + '.jpg', dpi = 600, transparent=True, bbox_inches="tight")
plt.show()


# %%
x = RefData[key][0]#[:-1]
energy = RefData[key][1]#[:-1]
x_pos = [i for i, _ in enumerate(x)]


fig, ax = plt.subplots()

plt.bar(x_pos, energy, color = ['blue'], width=0.4)
patterns = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')


plt.xlabel('Salts and Additives', fontsize = 14, color= 'black')
plt.ylabel("GHG Emissions [$kg_{CO_2eq}$ $kg^{-1}_{material}$]", fontsize = 14, color= 'black')
#plt.title("Energy output from various fuel sources")
plt.xticks(x_pos, x)
ax.tick_params(axis="y",direction="in", colors='black')
plt.tick_params(bottom = False)
plt.yticks(color= 'black')
plt.xticks(rotation=45, color= 'black')
plt.ylim(0, 75)
for i in range(len(x)):
    if i < 4:
        ax.bar(i, height =energy[i], color='blue', edgecolor='blue')
    if i == 4:
        ax.bar(i, height =energy[i], color='red', edgecolor='blue', hatch=patterns[3])
    if i > 4:
        ax.bar(i, height =energy[i], color='red', edgecolor='red')

plt.savefig('D:\projects\Data\Figures'+"/" + 'Salts and Additives'+ '.jpg', dpi = 300, bbox_inches="tight", facecolor='w')
# %%

path2 = 'D:\\user\\documents\\Work\\LCA'
Results = pd.read_excel(path2 + "\\"+ "graphs.xlsx", sheet_name= None, header= 0)
Weight= Results['Weight']
GHGemissions= Results['GHGemissions']
colors = {'Current Collectors':'#FFB061','Cathode':'#CCCCFF','Separator':'#99FFCC','Electrolyte':'#A3C8FF','Anode':'#E0E0E0'}

fig, (ax0, ax1) = plt.subplots(2,1, sharex= True)
Weight.plot(ax = ax0, kind='bar', stacked = True, figsize = (6,6), color=colors, legend = False, ylabel = "Mass %")
GHGemissions.plot(ax = ax1, kind='bar', stacked = True, figsize = (6,6), color=colors, legend = False, ylabel = "GHG Emissions %")
vals = ax0.get_yticks()
ax0.set_yticklabels(['{:,.0%}'.format(x) for x in vals])

vals = ax1.get_yticks()
ax1.set_yticklabels(['{:,.0%}'.format(x) for x in vals])
ax0.tick_params(axis="y",direction="in", colors='black')
ax0.yaxis.label.set_color('black')
ax0.yaxis.label.set_size(16)
ax1.tick_params(axis="y",direction="in", colors='black')
ax1.yaxis.label.set_color('black')
ax1.yaxis.label.set_size(16)
plt.xticks([0,1,2,3,4,5],list(Weight['Component']), color = "black")

legend = fig.legend(colors, loc = "upper center", ncol = 5)
plt.setp(legend.get_texts(), color='black')

plt.savefig('D:\projects\Data\Figures'+"/" +  'comparison.jpg', dpi = 600, bbox_inches="tight",  transparent=True, facecolor ='w')

# %%
path2 = 'D:\\user\\documents\\Work\\LCA'
Results = pd.read_excel(path2 + "\\"+ "graphs.xlsx", sheet_name= None, header= 0)
distance = Results['perkm']
distance = distance[distance.columns[0:4]]
distance_small = distance[distance.columns[0:4]]
distance_small['Replacement'][0]=0
upper = list(Results['perkm']['Upper'])
lower = list(Results['perkm']["Lower"])
Total = list(Results['perkm']["Total"])
Total1 = list(Results['perkm']["Total1"])

colors2 = {'Production':'#B3DE69','Use':'#FFDD2B','Replacement':'#F28E2B'}

fig2, ax3 = plt.subplots()
distance.plot(ax = ax3, kind="bar", stacked = True, legend = False,  ylabel = "GHG Emissions [$kg_{CO_2eq}$ $km^{-1}$]",color=colors2)
plt.xticks([0,1,2,3,4,5],list(distance['Author']),  color='black')
ax3.tick_params(axis="y",direction="in", colors='black')
ax3.yaxis.label.set_color('black')
ax3.errorbar(list(distance['Author']),Total, yerr = (lower,upper), color="black", ls='none')


axins = inset_axes(ax3, width="75%", height="75%", loc="upper right")
axins.tick_params(axis="y",direction="in", colors='black')
axins.yaxis.label.set_color('black')
axins.set_ylim(0,2.5)
axins.errorbar(list(distance['Author']),Total1, yerr = (lower,upper), color="black", ls='none')

distance_small.plot(ax = axins, kind="bar",stacked = True, legend = False, color=colors2)
legend = fig2.legend(colors2, loc = "upper center", ncol = 3)
plt.setp(legend.get_texts(), color='black')

plt.savefig('D:\projects\Data\Figures'+"/" + 'distance.jpg', dpi = 600, transparent=True, bbox_inches="tight")
#%%
path2 = 'D:\\user\\documents\\Work\\LCA'
Results = pd.read_excel(path2 + "\\"+ "graphs.xlsx", sheet_name= None, header= 0)
projection = Results['countryperkm']
plt.style.use('default')
colors2 = {'Production':'#B3DE69','Use':'#FFDD2B','Replacement':'#F28E2B'}
fig4, ax6 = plt.subplots()
projection.plot(ax = ax6, kind="bar", stacked = True, legend = False,  ylabel = "GHG Emissions [$kg_{CO_2eq}$ $km^{-1}$]",color=colors2)
plt.xticks([0,1,2,3,4],list(projection['Author']),  color='black')
legend = fig4.legend(colors2, loc = "upper center", ncol = 3)
plt.savefig('D:\projects\Data\Figures'+"/" + 'distance_proj.jpg', dpi = 600, transparent=True, bbox_inches="tight")
# %%

path2 = 'D:\\user\\documents\\Work\\LCA'
Results = pd.read_excel(path2 + "\\"+ "graphs.xlsx", sheet_name= None, header= 0)
mass = Results['perkwh']
mass = mass[mass.columns[0:4]]
mass2 = Results['perkwh'][['Mass Basis']]
upper1 = list(Results['perkwh']['Upper'])
lower1 = list(Results['perkwh']["Lower"])
type(mass)
colors3 = {'Materials':'#B3DE69','Transportation':'#FFDD2B','Production':'#F28E2B'}

fig3, ax4 = plt.subplots()
ax5 = ax4.twinx()
ax4 = mass.plot(kind="bar", stacked = True, legend = True,  ylabel = "GHG Emissions [$kg_{CO_2eq}$ $kWh^{-1}$]",color=colors3)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],list(mass['Chemistry']),  color='black', rotation=45)


ax5 = mass2.plot(kind ="line", ax= ax4, secondary_y=True, legend = True, linestyle = 'none', marker ='o', color = 'b')
ax5.set_ylabel("GHG Emissions [$kg_{CO_2eq}$ $kg^{-1}$]")
ax5.errorbar([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],mass2['Mass Basis'] , yerr = (lower1,upper1), color="black", ls='none')
ax5.set_ylim(0,120)
ax4.set_xticklabels(ax4.get_xticks(), rotation = 90)
ax4.yaxis.label.set_color('black')
ax5.yaxis.label.set_color('black')

ax4.tick_params(axis="y",direction="in", colors='black')
ax5.tick_params(axis="y",direction="in", colors='black')

plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],list(mass['Chemistry']),  color='black', rotation=45)
legend = fig3.legend(colors3, loc = "upper center", ncol = 3)
plt.setp(legend.get_texts(), color='black')
plt.savefig('D:\projects\Data\Figures'+"/" + 'scenario_mass.jpg', dpi = 300, transparent=True, bbox_inches="tight")

## Projections Figure
# path2 = 'D:\\user\\documents\\Work\\LCA'
# Results = pd.read_excel(path2 + "\\"+ "graphs.xlsx", sheet_name= None, header= 0)
# mass = Results['projectperkwh']
# mass = mass[mass.columns[0:4]]
# mass2 = Results['projectperkwh'][['Mass Basis']]
# # upper1 = list(Results['perkwh']['Upper'])
# # lower1 = list(Results['perkwh']["Lower"])

# colors3 = {'Materials':'#B3DE69','Transportation':'#FFDD2B','Production':'#F28E2B'}

# fig3, ax4 = plt.subplots()
# ax5 = ax4.twinx()
# ax4 = mass.plot(kind="bar", stacked = True, legend = True,  ylabel = "GHG Emissions [$kg_{CO_2eq}$ $kWh^{-1}$]",color=colors3)
# plt.xticks([0,1,2,3],list(mass['Chemistry']),  color='black', rotation=45)


# ax5 = mass2.plot(kind ="line", ax= ax4, secondary_y=True, legend = True, linestyle = 'none', marker ='o', color = 'b')
# ax5.set_ylabel("GHG Emissions [$kg_{CO_2eq}$ $kg^{-1}$]")
# # ax5.errorbar([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],mass2['Mass Basis'] , yerr = (lower1,upper1), color="black", ls='none')

# ax4.set_xticklabels(ax4.get_xticks(), rotation = 90)
# ax4.yaxis.label.set_color('black')
# ax5.yaxis.label.set_color('black')

# ax4.tick_params(axis="y",direction="in", colors='black')
# ax5.tick_params(axis="y",direction="in", colors='black')

# plt.xticks([0,1,2,3],list(mass['Chemistry']),  color='black', rotation=45)
# legend = fig3.legend(colors3, loc = "upper center", ncol = 3)
# plt.setp(legend.get_texts(), color='black')
# plt.savefig('D:\projects\Data\Figures'+"/" + 'scenario_mass.png', dpi = 300, transparent=True, bbox_inches="tight")

# %%
path2 = 'D:\\user\\documents\\Work\\LCA'
Results = pd.read_excel(path2 + "\\"+ "graphs.xlsx", sheet_name= None, header= 0)
mass = Results['Capacity']
plt.style.use('default')
groups = mass.groupby('Source')
upper2 = list(Results['Capacity']['Upper'])
lower2 = list(Results['Capacity']["Lower"])

colors4 = {'Electrolyte Var.':'#208EA3','Cat. & Binder Var.':'#37A862','Carbon/binder-less':'#E8384F','Anode Protection':'#EA4E9D','Gold Cat.':'#EECC16','BatPaC LCA§':'#4178BC'}

for name, group in groups:
    plt.plot(group.Capacity, group.GHGemissions, marker = 'o', linestyle = 'none', markersize = 12, label = name, color = colors4[name])

plt.errorbar(mass['Capacity'], mass['GHGemissions']-5, yerr = (lower2, upper2), color ="black", ls='none')
plt.legend()
plt.tick_params(axis ='both', color='black', direction ='in' , labelcolor ='black')
plt.xlabel("Capacity [Wh $kg^{-1}$]")
plt.ylabel("GHG Emissions [$kg_{CO_2eq}$ $kWh^{-1}$]")
plt.ylim(0,2750)
# plt.set_edgecolor('black')
# ax5 = massXu.plot.scatter('Capacity', 'GHGemissions' legend = True, linestyle = 'none', marker ='o', color = 'b')

plt.savefig('D:\projects\Data\Figures'+"/" + 'capaci.jpg', dpi = 300, transparent=True, bbox_inches="tight")

# %%
plt.style.available
# %%
