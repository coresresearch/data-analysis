#%%
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import numpy as np

plt.style.use('default')
plt.rcParams.update({'font.size': 18})


#%%
path = 'D:/projects/Data/Batcan/summary.csv'
bulkdata = pd.read_csv(path, header = 0)
bulkdata.columns
bulkdata['density'] = 1.0869 +934.1*bulkdata["Thickness"]*(1-bulkdata["Porosity"])+2216**bulkdata["Thickness"]*(bulkdata["Porosity"])
bulkdata['GHG Emissions [kg CO2 m-2]'] = 65.77324472 + 27192.25698*bulkdata["Thickness"]*(1-bulkdata["Porosity"])+149407.4639*bulkdata["Thickness"]*(bulkdata["Porosity"])
bulkdata["Thickness"] =bulkdata["Thickness"]*1000000 #convert from m
bulkdata['En_Den'] = bulkdata['Energy Density']/bulkdata['density']
bulkdata['GHG Emissions [kg CO2 kWh-2]'] = bulkdata['GHG Emissions [kg CO2 m-2]']/bulkdata['Energy Density']*1000
bulkdata['Pow Den'] = bulkdata['Power Density']/bulkdata['density']
# ed_max = bulkdata['En Den'].max() #Wh/m2
# ed_min = bulkdata['En Den'].min()
# pd_max = bulkdata['Pow Den'].max() #W/m2
# pd_min = bulkdata['Pow Den'].min()

bulkdata.loc[bulkdata['Current'] == '0p5_liu', 'Current'] = '0.5 mA cm⁻²'
bulkdata.loc[bulkdata['Current'] == '0p2_liu', 'Current'] = '0.2 mA cm⁻²'
bulkdata.loc[bulkdata['Current'] == '1_liu', 'Current'] = '1 mA cm⁻²'
bulkdata.loc[bulkdata['Current'] == '0p1_liu', 'Current'] = '0.1 mA cm⁻²'

bulkdata = bulkdata.rename(columns={'Porosity': 'Porosity [-]','Thickness':'Thickness (μm)'})
array = bulkdata['Current'].unique()
array.sort()
#ToDo:
#Make subplots
#Change title
#change labels
#Share-x and share-y
#Change current
pointer = np.arange(0.20,0.84,0.05)[::-1].round(2)
fig, axes = plt.subplots(2, 2, figsize=(20,14))
plt.subplots_adjust(wspace=0, hspace=0.1)
fig2, axes2 = plt.subplots(2, 2, figsize=(20,14))
plt.subplots_adjust(wspace=0, hspace=0.1)
fig3, axes3 = plt.subplots(2, 2, figsize=(20,14))
plt.subplots_adjust(wspace=0, hspace=0.1)
# fig4, axes4 = plt.subplots(2, 2, figsize=(20,14))
# plt.subplots_adjust(wspace=0, hspace=0.1)

plt.plot(bulkdata['En_Den'], bulkdata["GHG Emissions [kg CO2 kWh-2]"], marker ='o', linestyle = 'none')



for n, current in enumerate(array):
    if n<2:
        a = 0
    else:
        a = 1
    if n % 2 == 0:
        b=0 # Even
    else:
        b=1 # Odd
    data = bulkdata[bulkdata.Current == current]
    # plt.figure()
    # plt.plot(data['En_Den'], data["GHG Emissions [kg CO2 kWh-2]"], marker ='o', linestyle = 'none')
    # plt.ylabel('Energy Density [Wh kg⁻¹]')
    # plt.xlabel('GHG Emissions [ kg CO2 kWh⁻¹]')
    # plt.savefig(str(current)+'.png', format='png', dpi=900, bbox_inches = "tight")
    # plt.yscale('log')
    ed_max = data['En_Den'].max() #Wh/m2
    Point = bulkdata[bulkdata.En_Den == ed_max]

    ed_min = data['En_Den'].min()
    pd_max = data['Pow Den'].max() #W/m2
    pd_min = data['Pow Den'].min()
    g_min = data["GHG Emissions [kg CO2 kWh-2]"].min()
    # c_max = data["Capacity"].max()
    # Point_2 = bulkdata[bulkdata.Capacity == c_max]
    print(Point)
    energy_density = data.pivot('Porosity [-]','Thickness (μm)', 'En_Den')
    power_density = data.pivot('Porosity [-]', 'Thickness (μm)', "Pow Den")
    # capacity = data.pivot('Porosity [-]', 'Thickness (μm)', "Capacity")
    GHG= data.pivot('Porosity [-]', 'Thickness (μm)', "GHG Emissions [kg CO2 kWh-2]")
    sns.heatmap(energy_density, ax=axes[a,b]).set_title(current + ': Max Energy Density =' + str(round(ed_max)) + ' Wh kg⁻¹') #, vmin=ed_min, vmax=ed_max
    sns.heatmap(power_density, ax=axes2[a,b]).set_title(current + ': Max Power Density =' + str(round(pd_max,1)) + ' W kg⁻¹') #, vmin=pd_min, vmax=pd_max
    # sns.heatmap(capacity, ax=axes4[a,b]).set_title(current + ': Max Capacity =' + str(round(c_max,1)) + ' mAh g⁻¹') #, vmin=pd_min, vmax=pd_max
    sns.heatmap(GHG, ax=axes3[a,b], cmap="crest").set_title(current + ': Min GHG =' + str(round(g_min)) + ' kg CO2 kWh⁻¹') #, vmin=pd_min, vmax=pd_max

axes[0,0].set(xticklabels=[])
axes[0,1].set(xticklabels=[])
axes[0,0].set(yticklabels=pointer)
axes[1,0].set(yticklabels=pointer)
axes[0,0].set(xlabel=None)
axes[0,1].set(xlabel=None)
axes[0,0].tick_params(bottom=False)
axes[0,1].tick_params(bottom=False)

axes[1,1].set(yticklabels=[])
axes[0,1].set(yticklabels=[])
axes2[0,0].set(yticklabels=pointer)
axes2[1,0].set(yticklabels=pointer)
axes[0,1].tick_params(left=False)
axes[1,1].tick_params(left=False)
axes[0,1].set(ylabel=None)
axes[1,1].set(ylabel=None)

# fig.savefig('heatmap_ed'+ '.png', format='png', dpi=900, bbox_inches = "tight")
axes2[0,0].set(xticklabels=[])
axes2[0,1].set(xticklabels=[])
axes2[0,0].set(yticklabels=pointer)
axes2[1,0].set(yticklabels=pointer)
axes2[0,0].set(xlabel=None)
axes2[0,1].set(xlabel=None)
axes2[0,0].tick_params(bottom=False)
axes2[0,1].tick_params(bottom=False)

axes2[1,1].set(yticklabels=[])
axes2[0,1].set(yticklabels=[])
axes2[0,1].tick_params(left=False)
axes2[1,1].tick_params(left=False)
axes2[0,1].set(ylabel=None)
axes2[1,1].set(ylabel=None)

# fig2.savefig('heatmap_pd'+ '.png', format='png', dpi=900, bbox_inches = "tight")

axes3[0,0].set(xticklabels=[])
axes3[0,1].set(xticklabels=[])
axes3[0,0].set(yticklabels=pointer)
axes3[1,0].set(yticklabels=pointer)
axes3[0,0].set(xlabel=None)
axes3[0,1].set(xlabel=None)
axes3[0,0].tick_params(bottom=False)
axes3[0,1].tick_params(bottom=False)

axes3[1,1].set(yticklabels=[])
axes3[0,1].set(yticklabels=[])
axes3[0,1].tick_params(left=False)
axes3[1,1].tick_params(left=False)
axes3[0,1].set(ylabel=None)
axes3[1,1].set(ylabel=None)

# fig3.savefig('heatmap_ghg'+ '.png', format='png', dpi=900, bbox_inches = "tight")
# axes4[0,0].set(xticklabels=[])
# axes4[0,1].set(xticklabels=[])
# axes4[0,0].set(yticklabels=pointer)
# axes4[1,0].set(yticklabels=pointer)
# axes4[0,0].set(xlabel=None)
# axes4[0,1].set(xlabel=None)
# axes4[0,0].tick_params(bottom=False)
# axes4[0,1].tick_params(bottom=False)

# axes4[1,1].set(yticklabels=[])
# axes4[0,1].set(yticklabels=[])
# axes4[0,1].tick_params(left=False)
# axes4[1,1].tick_params(left=False)
# axes4[0,1].set(ylabel=None)
# axes4[1,1].set(ylabel=None)


# for items in axes:
#     print(items)
#     items[0].set(xticklabels=[])  # remove the tick labels
#     items[0].tick_params(bottom=False)


# %%
