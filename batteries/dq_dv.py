# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 10:10:36 2023

@author: mpopeil
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sk
import sklearn.datasets
from pandas import DataFrame
from scipy.interpolate import Akima1DInterpolator
import scipy

from scipy import signal
from scipy.signal import savgol_filter
from scipy import interpolate
from scipy.integrate import simpson
from numpy import trapz

#load data into dataframes
files=['L2_Ta.csv']
for data in files:
    
    df = pd.read_csv(data)
# charge1=df[(df['Cycle']==1) & (df['Step']==4)]
# discharge1=df[(df['Cycle']==1) & (df['Step']==7)]
# charge2=df[(df['Cycle']==2) & (df['Step']==4)]
# discharge2=df[(df['Cycle']==2) & (df['Step']==7)]
# charge3=df[(df['Cycle']==3) & (df['Step']==4)]
# discharge3=df[(df['Cycle']==3) & (df['Step']==7)]

# cycles=[charge1,discharge1, charge2, discharge2, charge3, discharge3]

    for i in range(3,4):
        charge=df[(df['Cycle']==i) & (df['Step']==4)]
        discharge=df[(df['Cycle']==i) & (df['Step']==7)]
        # plt.figure(1)
        # plt.scatter(charge['Voltage'], charge['Capacity (mAHr)'])
        # plt.scatter(discharge['Voltage'], discharge['Capacity (mAHr)'])
        #"clean" data
        step=(max(charge['Voltage'])-min(charge['Voltage']))/len(charge['Voltage'])
        x=np.arange(min(charge['Voltage']),max(charge['Voltage']),step)
        xp=charge['Voltage']
        xd=discharge['Voltage']
        fp=charge['Capacity (mAHr)']
        interpolation=np.interp(x, xp, fp)
        #smooth data
        filtered=savgol_filter(interpolation, 9, 1)
        #filtered_discharge=savgol_filter(discharge['Capacity (mAHr)'], 9, 1)
        dV=np.diff(x)
        dq=np.diff(filtered)
        dq_dV=dq/dV
        V=x[:-1]
        #discharge
        #discharge=df[(df['Cycle']==2) & (df['Step']==7)]
        step_discharge=(max(discharge['Voltage'])-min(discharge['Voltage']))/len(discharge['Voltage'])
        x_discharge=np.arange(min(discharge['Voltage']),max(discharge['Voltage']),step_discharge)
        xd=discharge['Voltage']
        fd=discharge['Capacity (mAHr)']
        f = interpolate.interp1d(xd, fd, assume_sorted = False)
        ynew = f(x_discharge) 
        # plt.figure(1)
        # plt.plot(xd, fd, 'o', x_discharge, ynew, '-')
        # plt.plot(xp, fp, 'o', x,interpolation, '-')
        filtered_discharge=savgol_filter(ynew, 9, 1)
        dV_discharge=np.diff(x_discharge)
        dq_discharge=np.diff(filtered_discharge)
        dq_dV_discharge=dq_discharge/dV_discharge
        V2=x_discharge[:-1]
        plt.figure(2)
        plt.plot(V,dq_dV,'r')
        plt.plot(V2,dq_dV_discharge,'r', label=data)
        plt.legend(loc="upper left")
         
    #Determine the capacity(area under the curve)
    #first fit data to a function
    
    
    
    
    #integrate or area function
    # Compute the area using the composite trapezoidal rule.
    y=dq_dV_discharge
    area = trapz(y, dx=step_discharge)
    print("trapz area =", area)
    
    # Compute the area using the composite Simpson's rule.
    area = simpson(y, dx=step_discharge)
    print("simpson area =", area)