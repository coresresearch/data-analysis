
#%%
import pandas as pd
import os




path = 'D:\projects\Data\ToProcess' #change this to file directory
path2 = 'D:\projects\BatCan\outputs'
modelfile = 'output.csv'
comparison = 'Refdata.xlsx'
#%%

def interpolate(voltage1, voltage2, capacity1, capacity2, capacity3):
    voltage3 =  (voltage2 - voltage1)*(capacity3-capacity1)/(capacity2-capacity1) +voltage1
    return voltage3

def locater(dataset, i, refcapacity):
    lowerneighbour_ind = RefData[dataset][RefData[dataset]['Capacity'] < CodeData['capacity'][i]]['Capacity'].idxmax()
    higherneighbour_ind = RefData[dataset][RefData[dataset]['Capacity'] > CodeData['capacity'][i]]['Capacity'].idxmin()
    capacity1 = RefData[dataset]['Capacity'][lowerneighbour_ind]
    capacity2 = RefData[dataset]['Capacity'][higherneighbour_ind]
    capacity3 = refcapacity
    voltage1 = RefData[dataset]['Voltage'][lowerneighbour_ind]
    voltage2 = RefData[dataset]['Voltage'][higherneighbour_ind]
    v3 = (interpolate(voltage1, voltage2, capacity1, capacity2, capacity3))
    SSR = (CodeData['capacity'][i] - v3)**2
    return SSR

def SSRmain(folder_name, dataset):
    SumSR = 0
    CodeData = pd.read_csv(path2+"/" + folder_name + "/" + "output.csv")
    cyclestart = CodeData[CodeData['cycle'] > 0]['cycle'].idxmin() + 1
    chargestart = CodeData[CodeData['cycle'] > 1]['cycle'].idxmin()
    for x, y in enumerate(CodeData['capacity'][cyclestart:chargestart]):
        SumSR += locater(dataset, x, y)

RefData = pd.read_excel(path + "/"+ comparison, sheet_name= None)

#%%

ID_key = {"CPCN04": "50CP50CNT0.4", "CP04":"CP0.4", "CPCN05":"50CP50CNT0.5", "CP05": "CP0.5", "CPCN06":"50CP50CNT0.6", "CP06":"CP0.6"}
SSRarray = []


for folder_name in os.listdir(path2):
    if "20220114" in folder_name:
        string = folder_name
        array = string.split("_")
        dataset = ID_key[array[1]]
        SSR_file = SSRmain(folder_name, dataset)
        SSRarray.append(SSR_file)

print(SSRarray)


#result = [locater("50CP50CNT0.4", x, refcapcity) for x, refcapcity in enumerate(CodeData['Capacity'])]
#print(result)

# print (Data['50CP50CNT0.4']['Capacity'][row])
# lowerneighbour_ind = Data2[Data2['Capacity'] < Temp]['Capacity'].idxmax()
# higherneighbour_ind = Data2[Data2['Capacity'] > Temp]['Capacity'].idxmin()
# v3 = interpolate(Data2['Capacity'][higherneighbour_ind], voltage2,Data2['Capacity'][lowerneighbour_ind], Data2['Capacity'][higherneighbour_ind], capacity3)
# SSR += (Voltage_test[i] - v3)**2



# %%
# Official Playlist
# Small World - Bump of Chicken