import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

font = {'family' : 'normal',
        'weight' : '500',
        'size'   : 16}

plt.rc('font', **font)

objects = ('01/03', '02/03', '03/03', '04/03', '05/03', '06/03')
months = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho')
data1 = [23,85, 72, 43, 52]
data2 = [42, 35, 21, 16, 9]
clrs = ['grey']
y_pos = np.arange(len(objects))
b_range = len(data1)
plt.xticks(y_pos, months, fontsize=22)
width =0.3
bar=plt.bar(np.arange(len(data1)), data1, width=width, color=clrs)
plt.ylabel('Valores de consumo', fontsize=22)
plt.title('Consumo Mensal', fontsize=22)
bar[b_range-1].set_color('#3D7070')
plt.legend(labels=['Meses Anteriores', 'Mês Atual'], loc='upper center',
  bbox_to_anchor=(0.5, -0.09), shadow=True, prop=dict(size=22))
plt.show()

