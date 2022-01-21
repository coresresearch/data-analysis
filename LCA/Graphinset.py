#%%

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

#%%
x = ['Nuclear', 'Hydro', 'Gas', 'Oil', 'Coal', 'Biofuel']
energy = [5, 6, 15, 22, 24, 8]
X2 = x[:3]
energy2 = energy[:3]

x_pos = [i for i, _ in enumerate(x)]
x_pos2 = [i for i, _ in enumerate(X2)]
fig, ax = plt.subplots()
plt.bar(x_pos, energy, color=['green', 'green', 'blue'])
plt.xlabel("Energy Source", fontsize = 14, fontname= 'Times New Roman')
plt.ylabel("Energy Output (GJ)", fontsize = 14, fontname= 'Times New Roman')
plt.title("Energy output from various fuel sources")
plt.xticks(x_pos, x)

axins = inset_axes(ax, width="40%", height="40%", loc="upper right")
plt.bar(x_pos2, energy2, color=['green','blue'])
plt.xticks(x_pos2, X2)
for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_fontsize(12)
    tick.label1.set_fontname('Times New Roman')

for tick in ax.yaxis.get_major_ticks():
    tick.label1.set_fontsize(12)
    tick.label1.set_fontname('Times New Roman')

for tick in axins.xaxis.get_major_ticks():
    tick.label1.set_fontsize(12)
    tick.label1.set_fontname('Times New Roman')
for tick in axins.yaxis.get_major_ticks():
    tick.label1.set_fontsize(12)
    tick.label1.set_fontname('Times New Roman')

plt.show()

# %%
