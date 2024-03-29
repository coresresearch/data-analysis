#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools
plt.style.use('default')
#%%
path = 'D:\projects\Data\ToProcess'
RefData = pd.read_excel(path + "/"+ "Summary_LCA.xlsx", sheet_name= None, header= None)

# %%
# This a function which plots a clustered bar chart
# key = "Lithium"
# cmap = plt.get_cmap('Greys')

# key = "Current Collectors"
# cmap = plt.get_cmap('Oranges')
# gridspec_kw={'height_ratios': [1, 2]}
# width = 0.85
# ncol=4
# ax1.yaxis.set_ticks(np.arange(100, max, 20))
# ax1.set_ylim(100, max)  # outliers only
# ax2.set_ylim(0, 14)

# key ='Binders'
# cmap = plt.get_cmap('Reds')
# gridspec_kw={'height_ratios': [1, 2]}
# width = 0.85
# ncol=6
# ax1.yaxis.set_ticks(np.arange(30000, max, 10000))
# ax1.set_ylim(30000, max)  # outliers only
# ax2.set_ylim(0, 70)

key = "Catalysts"
# cmap = plt.get_cmap('Blues')

# key ='Solvents'
# cmap = plt.get_cmap('Greens')
# gridspec_kw={'height_ratios': [1, 2]}
# width = 0.85
# ncol=5
# ax1.yaxis.set_ticks(np.arange(100, max, 20))
# ax1.set_ylim(100, max)  # outliers only
# ax2.set_ylim(0, 35)


# key = 'Salts'
# cmap = plt.get_cmap('Purples')
# gridspec_kw={'height_ratios': [1.4, 2]}
# width = 0.85
# ncol=5
# ax1.yaxis.set_ticks(np.arange(1000, max, 10000))
# ax1.set_ylim(1000, max)  # outliers only
# ax2.set_ylim(0, 70)

Clustered = RefData[key].rename(columns=RefData[key].iloc[0]).drop(RefData[key].index[0])
max = Clustered[Clustered.columns[1:]].max().max()
print(max)
legend = Clustered.columns[1:]
legend_add = len(legend) + 3

cmap = plt.get_cmap('Greys')
color_ind = np.linspace(0,1,legend_add)
color_ind = np.flip(color_ind)
colors = list()
for i in np.arange(legend_add):
    colors.append(cmap(color_ind[i]))

#%%

def flip(items, ncol):
    return itertools.chain(*[items[i::ncol] for i in range(ncol)])
#chage direction of the legend

fig2, (ax1,ax2) =  plt.subplots(2, 1, gridspec_kw={'height_ratios':  [1.4, 2]}, sharex=True)
Clustered.set_index(key).plot(ax = ax1, kind='bar', legend = False, width = 0.85, color = colors)
Clustered.set_index(key).plot(ax = ax2, kind='bar', legend= False, width = 0.85, color = colors)
ax1.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax1.tick_params(bottom =False)  # don't put tick labels at the top
handles, labels = ax2.get_legend_handles_labels()
fig2.legend(flip(handles, 5), flip(labels, 5), loc=9, ncol=5)
# fig2.legend(labels = Clustered.columns[1:], loc="upper center", ncol=5)
ax2.xaxis.tick_bottom()
ax1.yaxis.set_ticks(np.arange(1000, max, 50000))
ax1.set_ylim(1000, max)  # outliers only
ax2.set_ylim(0, 70)
d = .5  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)

ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)
plt.xlabel("Salts and Additives", fontsize=18)
fig2.supylabel('Relative Impact to PEG')

# cmap = plt.get_cmap('Purples')
# gridspec_kw={'height_ratios': [1.4, 2]}
# width = 0.85
# ncol=5
# ax1.yaxis.set_ticks(np.arange(1000, max, 10000))
# ax1.set_ylim(1000, max)  # outliers only
# ax2.set_ylim(0, 70)


plt.show()
#%%
fig2.savefig(key+ '.png', format='png', dpi=1200, bbox_inches = "tight")

#%%
# for just running Catalysts
ax_blerg = plt.subplot(111)
Clustered.set_index("Li").plot(ax = ax_blerg, kind='bar', legend = False, width = 0.85, color = colors)
handles, labels = ax_blerg.get_legend_handles_labels()
plt.legend(flip(handles, 4), flip(labels, 4), bbox_to_anchor=(0.5, 1.2), loc="upper center", ncol=4)
# plt.yscale("log")
plt.ylabel('Relative Impact to Lithium')
plt.xlabel(key, fontsize=18)
# plt.legend(bbox_to_anchor=(0.5, 1.2),loc="upper center", ncol=4)
plt.savefig(key+ '.png', format='png', dpi=1200, bbox_inches = "tight")

#%%
path = 'D:\projects\Data\ToProcess'
RefData_kg = pd.read_excel(path + "/"+ "LCA_Summary_kg.xlsx", sheet_name= None, header= 0)

total = []
upper = []
lower = []
dataframes = []

for key in RefData_kg.keys():
    total.append(RefData_kg[key]['Total'].tolist())
    upper.append( RefData_kg[key]['Upper'].tolist())
    lower.append(RefData_kg[key]['Lower'].tolist())
    dataframes.append(RefData_kg[key][RefData_kg[key].columns[:-3]])

titles_legend = list(RefData_kg['LCA2'].columns[1:-3])

# titles  = ['Production', 'Use', 'Replacement']
# key = ['PiYG','PRGn','coolwarm'] # for km graph
# key = ['bwr_r','RdBu','BrBG_r'] #for grid mixes

titles =['Lithium', 'Binder', 'Current Collector', 'Solvent', 'Catalyst', 'Salt', 'Other', 'Transport', 'Production']
key = ['Greys','Reds','Oranges','Greens', 'Blues', 'Purples',  'PuRd' ,  'pink_r',  'Wistia']

legend_add =len(RefData_kg.keys())
color_ind = np.linspace(0.3,0.8,legend_add)
color_ind = np.flip(color_ind)

legend_map2= plt.get_cmap('Greys')
second_legend = list()
for i in np.arange(legend_add):
    second_legend.append(legend_map2(color_ind[i]))
# batteries = ['China', 'USA', 'Norway', 'South Korea', 'South Africa']
batteries = ['Electrolyte Var.' ,'Cat. & Binder Var.', 'Carbon/binder-less', 'Anode Protection', 'Gold Cat.']
legend_zip2 = dict(zip(batteries,second_legend))

colorseed = [ [] for _ in range(legend_add) ]


for i in np.arange(legend_add):
    for number, color in enumerate(key):
        cmap = plt.get_cmap(color)
        colorseed[i].append(cmap(color_ind[i]))

legend_zip = dict(zip(titles_legend,colorseed[1]))

n_df = len(dataframes)
n_col = len(dataframes[0].columns) -1
n_ind = len(dataframes[0].index)
Fig_2 = plt.subplot(111)

for i in range(n_df):
    Fig_2.bar(0, 0, color=second_legend[i])


for numbers, keys in enumerate(dataframes): # for each data frame
    Fig_2 = keys.plot(kind="bar", linewidth=0, stacked=True, ax=Fig_2, legend=False, grid=False, color = colorseed[numbers], ylabel = "Relative impact (km$^{-1}$) to Carbon/Binderless with China's Grid")
    Fig_2.errorbar(dataframes[numbers].index + Fig_2.patches[0].get_x()+(0.5+numbers)*1 / float(n_df + 1),total[numbers], yerr = (lower[numbers],upper[numbers]), color="black", ls='none')

h,l = Fig_2.get_legend_handles_labels() # get the handles we want to modify

for i in range(0, n_df * n_col, n_col):
    for pa in h[i:i+n_col]:
        for rect in pa.patches: # for each index
            rect.set_x(rect.get_x() + 1 / float(n_df + 1) * i / float(n_col))
            rect.set_width(1 / float(n_df + 1))
plt.xticks(dataframes[numbers].index, list(dataframes[0]['Materials Extraction']),  color='black')
legend = Fig_2.legend(legend_zip2, loc = "upper center", ncol = 3,bbox_to_anchor=(0.5, 1.16))
ax = plt.gca().add_artist(legend)
plt.legend(h[0:3],l[0:3], loc="upper center", ncol =3,bbox_to_anchor=(0.5, 1.24))
plt.xlim(np.array(plt.xlim())+[0,1 / float(n_df + 1)])


plt.savefig('variation'+ '.png', format='png', dpi=1200, bbox_inches = "tight")

# %%


fig_ultimate, (ax3,ax4) =  plt.subplots(2, 1, gridspec_kw={'height_ratios':  [1, 2]}, sharex=True)
for i in range(n_df):
    ax3.bar(0, 0, color=second_legend[i])

for numbers, keys in enumerate(dataframes): # for each data frame
    ax4 = keys.plot(kind="bar", linewidth=0, stacked=True, ax=ax4, legend=False, grid=False, color = colorseed[numbers])
    ax4.errorbar(dataframes[numbers].index + ax4.patches[0].get_x()+(0.5+numbers)*1 / float(n_df + 1),total[numbers], yerr = (lower[numbers],upper[numbers]), color="black", ls='none')

h,l = ax4.get_legend_handles_labels() # get the handles we want to modify

for i in range(0, n_df * n_col, n_col):
    for pa in h[i:i+n_col]:
        for rect in pa.patches: # for each index
            rect.set_x(rect.get_x() + 1 / float(n_df + 1) * i / float(n_col))
            rect.set_width(1 / float(n_df + 1))

for numbers, keys in enumerate(dataframes): # for each data frame
    ax3 = keys.plot(kind="bar", linewidth=0, stacked=True, ax=ax3, legend=False, grid=False, color = colorseed[numbers])
    ax3.errorbar(dataframes[numbers].index + ax4.patches[0].get_x()+(0.5+numbers)*1 / float(n_df + 1),total[numbers], yerr = (lower[numbers],upper[numbers]), color="black", ls='none')

h,l = ax3.get_legend_handles_labels() # get the handles we want to modify

for i in range(0, n_df * n_col, n_col):
    for pa in h[i:i+n_col]:
        for rect in pa.patches: # for each index
            rect.set_x(rect.get_x() + 1 / float(n_df + 1) * i / float(n_col))
            rect.set_width(1 / float(n_df + 1))


ax3.spines['bottom'].set_visible(False)
ax4.spines['top'].set_visible(False)
ax3.tick_params(bottom =False)  # don't put tick labels at the top
ax4.xaxis.tick_bottom()
ax3.yaxis.set_ticks(np.arange(20, 140, 20))
ax3.set_ylim(20, 140)  # outliers only
ax4.set_ylim(0, 8)
d = .5  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax3.plot([0, 1], [0, 0], transform=ax3.transAxes, **kwargs, label='_nolegend_')

ax4.plot([0, 1], [1, 1], transform=ax4.transAxes, **kwargs, label='_nolegend_')
ax4.set_xlim(np.array(ax4.get_xlim())+[0,1 / float(n_df + 1)])
ax3.set_xlim(np.array(ax4.get_xlim())+[0,1 / float(n_df + 1)])

legend = ax4.legend(legend_zip, loc = "upper center", ncol = 4, bbox_to_anchor=(0.5,2.3 ))

legend2 = ax3.legend(legend_zip2, loc = "upper center", ncol =3, bbox_to_anchor=(0.5, 1.55))
fig_ultimate.supylabel('Relative Impact (kg$^{-1}$) to Carbon/binder-less')
plt.xticks(dataframes[numbers].index, list(dataframes[0]['Materials Extraction']))
plt.savefig('variation'+ '.png', format='png', dpi=1200, bbox_inches = "tight")

#%%

weight_data = pd.read_excel(path + "/"+ "weight.xlsx", sheet_name= 'Sheet1', header= 0)
fig_w, ax_w = plt.subplots()

# for numbers, keys in enumerate(dataframes): # for each data frame
#     ax_w= weight_data.plot(kind="bar", linewidth=0, stacked=True, ax=ax4, legend=False, grid=False, color = colorseed[numbers])
weight_data.plot(ax = ax_w, kind='bar', stacked = True, figsize = (6,3), color=colorseed[1], legend = False, ylabel = "Mass %", )

fig_w.legend(loc='upper center', ncol = 4, bbox_to_anchor=(0.5, 1.10))


key_bar = ['Greys','Reds','Oranges','Greens', 'Blues', 'Purples',  'PuRd']


legend_bar =5
colorseed_bar = []
color_ind = np.linspace(0.3,0.8,legend_bar)
color_ind = np.flip(color_ind)


for number, color in enumerate(key_bar):
    for i in np.arange(legend_bar):
        cmap = plt.get_cmap(color)
        colorseed_bar.append(cmap(color_ind[i]))
some = len(colorseed_bar)
# flat_list = [item for sublist in colorseed_bar for item in sublist]
# some = len(flat_list)



# batteries = ['China', 'USA', 'Norway', 'South Korea', 'South Africa']
batteries = ['Electrolyte Var.' ,'Cat. & Binder Var.', 'Carbon/binder-less', 'Anode Protection', 'Gold Cat.']


for x in np.arange(some) :
    ax_w.get_children()[x].set_color(colorseed_bar[x])

vals = ax_w.get_yticks()

ax_w.set_yticklabels(['{:,.0%}'.format(x) for x in vals])

plt.xticks(np.arange(legend_bar),list(weight_data['Component']),  rotation=45)



plt.savefig('weight'+ '.png', format='png', dpi=1200, bbox_inches = "tight")


#%%

#soundtrack:
# Queen Bee - BL, Oil
# Ethel Cain - Preacher's Daughter
# %%
