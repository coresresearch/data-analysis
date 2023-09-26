# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 10:10:36 2023

@author: mpopeil
"""
#import functions

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sk
import scipy as sp

#load data into dataframes

files=['L2_Ta.csv']
for data in files:  
    df = pd.read_csv(data)
    
    #edit range for which cycles you want to look at
    
    for i in range(3,4):
        charge = df[(df['Cycle']==i) & (df['Step']==4)]
        discharge = df[(df['Cycle']==i) & (df['Step']==7)]
        
        # We will sample the charge and discharge profiles, at regularly-spaced #  intervals. Begin by calculating the average voltage step size.
        step_charge = (max(charge['Voltage'])-min(charge['Voltage']))/len(charge['Voltage'])
        step_discharge = (max(discharge['Voltage'])-min(discharge['Voltage']))/len(discharge['Voltage'])
        
        x_charge = np.arange(min(charge['Voltage']),max(charge['Voltage']),
                            step_charge)
        x_discharge = np.arange(min(discharge['Voltage']),
                            max(discharge['Voltage']),step_discharge)
        
        xc = charge['Voltage']
        xd = np.flip(discharge['Voltage'])
        
        fc = charge['Capacity (mAHr)']
        fd = np.flip(discharge['Capacity (mAHr)'])
        
        interpolation_charge = np.interp(x_charge, xc, fc)
        interpolation_discharge=np.interp(x_discharge, xd, fd)
        
        #smooth data
        filtered_charge = sp.signal.savgol_filter(interpolation_charge, 9, 1)
        filtered_discharge = sp.signal.savgol_filter(interpolation_discharge, 
                                                     9, 1)
        
        #doing differentials for dq/dv
        dV_charge = np.diff(x_charge)
        dq_charge = np.diff(filtered_charge)
        dq_dV_charge=dq_charge / dV_charge
        V_charge = x_charge[:-1]
        dV_discharge = np.diff(x_discharge)
        dq_discharge = np.diff(filtered_discharge)
        dq_dV_discharge = dq_discharge/dV_discharge
        V_discharge = x_discharge[:-1]
        
        #Plot charge/discharge curve dq/dv
        plt.figure(1)
        plt.plot(V_charge, dq_dV_charge, 'r')
        plt.plot(V_discharge, dq_dV_discharge, 'r', label=data)
        plt.legend(loc ="upper left")
         
    #Determine the capacity(area under the curve)
    #integrate or area function
    # Compute the area using the composite trapezoidal rule.
    y = dq_dV_discharge
    area = np.trapz(y, dx = step_discharge)
    print("trapz area =", area)
    
    # Compute the area using the composite Simpson's rule.
    area = sp.integrate.simpson(y, dx = step_discharge)
    print("simpson area =", area)