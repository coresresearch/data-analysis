#%%
import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt
import os
# %%
path = 'C:/Users/Mels/Code/Labdata/HNG_out'
r_min = 1e-10 # m // minimum particle radius to consider
r_max = 0.3e-7 # m // maximum particle radius to consider
n_bins = 200 # Number of histogram bins for the radii discretization
radii = np.linspace(r_min, r_max, n_bins)

def graph(file):
    Data = pd.read_csv(file, header= None)
    name = "M"
    plt.figure(0) #fix this so we can take out that?
    p, = plt.plot(radii, Data [Data.columns[-1]], \
            linewidth = 4., label = name)
    plt.xlabel('radius (m)', fontsize=14, fontname = 'Times New Roman')
    plt.ylabel('Nuclei (kmol/m2))', fontsize=14, fontname = 'Times New Roman')
    plt.xticks(fontsize=14, fontname = 'Times New Roman') 
    plt.yticks(fontsize=14, fontname = 'Times New Roman') 
    plt.legend()
    plt.xlim([0, 0.6E-8])

for file in os.listdir(path):
    graph(path + "/"+ file)
    print('Found')
# %%
