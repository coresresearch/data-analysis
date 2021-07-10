import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt
import os

path = 'C:/Users/Mels/Code/Data'

def graph(file):
    data = pd.read_csv(path +"/" + file, header= 0, sep = "\t")
    for column in data.columns[1:]:
        data["delta "+column] = data[column] - data[column][1]
    frequency = [col for col in data.columns if 'delta f' in col]
    dissipation = [col for col in data.columns if 'delta D' in col]
    plt.figure(0)
    for i, N in enumerate(frequency):
        plt.plot(data['Time_1 [s]'], data[N])
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (s)')
    plt.figure(1)
    for i, N in enumerate(dissipation ):
        plt.plot(data['Time_1 [s]'], data[N])
        plt.ylabel('Dissipation (ppm)')
    plt.xlabel('Time (s)')
    plt.show()
    data.to_csv(path +'/test.csv')


for file in os.listdir(path):
    if file.find('20210615') > -1:
        graph(file)