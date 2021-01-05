import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt



objects = ('01/03', '02/03', '03/03', '04/03', '05/03', '06/03')
data1 = [23,85, 72, 43, 52]
data2 = [42, 35, 21, 16, 9]
y_pos = np.arange(len(objects))
plt.xticks(y_pos, objects, fontsize=22)
width =0.3
plt.bar(np.arange(len(data1))-width/2, data1, width=width)
plt.bar(np.arange(len(data2))+ width/2, data2, width=width)
plt.title('Energias Reativas', fontsize=22)
plt.xlabel('Datas',fontsize=22)
plt.ylabel('Valores de Demanda',fontsize=22)
plt.legend(labels=['Energia reativa fora de ponta', 'Energia reativa ponta'], loc='upper center',
  bbox_to_anchor=(0.5, -0.09), shadow=True, prop=dict(size=22))
plt.show()