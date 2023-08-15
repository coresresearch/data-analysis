import pandas as pd

path = 'C:/Users/Mels/Code/Data/Temptext.txt'

data = pd.read_csv(path, header = None, sep = "\t", index_col=0)
print(data)
data_dict = data.to_dict()
print(data_dict)
