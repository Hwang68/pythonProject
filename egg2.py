import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
index = np.arange(9)

file = 'c:\egg_result1.xlsx'

df = pd.read_excel(file, sheet_name=1, usecols='A:D', skiprows=1, skipfooter=1)
plt.figure(figsize=(10, 5))


x_data =df.loc[:, 'subject']


y1_data=df['CNN-LSTM']
y2_data=df['HDNN-TL']
y3_data=df['1s_OVLP']

index=index+1
plt.bar(index, y1_data, color='olive', width=0.15, label='CNN-LSTM')
plt.bar(index+0.2, y2_data, color='blue', width=0.15, label='HDNN-TL')
plt.bar(index+0.4, y3_data, color='red', width=0.15, label='1s_OVLP')

plt.ylim([0.5, 1.0])
plt.xticks(index+0.2, x_data)
plt.ylabel('Kappa value')
plt.legend(loc=(0.84, 0.3))
#plt.legend(loc='best')

#plt.show()
plt.savefig('fig2.jpg', format='jpg', dpi=300, bbox_inches='tight')
