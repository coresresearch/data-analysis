# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 13:13:26 2021

@author: Joelle Scott
"""

import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt
import os

path = 'C:/Users/Mels/Code/Data'

def graph(file): 
    data = pd.read_csv(path + "/" + file,  header=1, sep = '\t')
    data = data.reset_index()
        #data["delta"+column] = data[column] - data[column][1]
    thickness = [col for col in data.columns if 'h [nm]' in col]
    mass = [col for col in data.columns if 'ng' in col]
        
    plt.figure(0)
    for i, N in enumerate(mass):
        plt.plot(data['Time [s]'], data[N])
        plt.ylabel('Mass (ng/$cm^2$)')
        plt.xlabel('Time (s)')
        plt.show()
    
    plt.figure(1)
    for i, N in enumerate(thickness):
        plt.plot(data['Time [s]'], data[N])
        plt.ylabel('Thickness (nm)')
        plt.xlabel('Time (s)')
        plt.show()
        
for file in os.listdir(path):
    if file.find('thicknessdata')>-1:
        graph(file)
        
        
        
        
        
        