import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
index = np.arange(9)

file = 'c:\egg_result1.xlsx'

df = pd.read_excel(file, sheet_name = 0, usecols='A:C',  skipfooter=1)
plt.figure(figsize=(8, 5))


x_data =df.loc[:, 'subject']


y1_data=df['1s']
y2_data=df['1s_OVLP']

index=index+1
plt.bar(index, y1_data, color='blue', width=0.2, label='1s')
plt.bar(index+0.3, y2_data, color='red', width=0.2, label='1s_OVLP')

plt.ylim([0.8, 1.0])
plt.xticks(index+0.15, x_data)
plt.ylabel('Kappa value')
plt.legend(loc='upper right')

#plt.show()
plt.savefig('fig1.jpg', format='jpg', dpi=300, bbox_inches='tight')
