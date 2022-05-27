
#%%
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#%%
path = "D:\projects\Steven\BatCan\outputs"
key = "eps_product" #reference datalike could be ClO4-[elyt], eps_product,
# %%
def graph_concentrations(pathes, title):
    Data =  pd.read_csv(pathes, header = 0, mangle_dupe_cols= True)
    n = len(Data.filter(like = key).columns)
    cmap = plt.get_cmap('cool')
    color_ind = np.linspace(0,1,n)
    colors = list()
    for i in np.arange(n):
        colors.append(cmap(color_ind[i]))
    Data.filter(like = key).plot.line(legend = False, title = title, color = colors) #
    plt.style.use('default')
    plt.xlabel('time (s)')
    plt.ylabel('CLO4- Concentration (M)')
    plt.tick_params(direction= 'in')

#%%
for folder in os.listdir(path):
    for subfolder in os.listdir(path +"/" +folder):
        if subfolder.find(".csv") > -1:
            graph_concentrations(path +"/" +folder + "/" +subfolder, subfolder)
        else:
            with os.scandir(path +"/" +folder) as it:
                for entry in it:
                    if entry.is_dir():
                        for file in os.scandir(path +"/" +folder +"/"+ entry.name):
                            if file.name.find(".csv") > -1:
                                graph_concentrations(path +"/" +folder +"/"+ entry.name+"/"+file.name, subfolder)

# %%
