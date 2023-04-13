import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
index = np.arange(9)
#from google.colab import files
#uploaded = files.upload()

file = 'c:\imsi.xlsx'

df = pd.read_excel(file, sheet_name = 0, usecols='A:E',  skiprows=1, skipfooter=1)
plt.figure(figsize=(10, 5))


x_data =df.loc[:, 'subject']

#subject --string 일때는 value없음 -> 숫자일때 cell.value.tolist()  --키,value
y1_data=df['Accuracy']
y2_data=df['Kappa']
y3_data=df['Precision']
y4_data=df['Recall']
index=index+1
plt.bar(index, y1_data, color='red', width=0.1, label='Accuracy')
plt.bar(index+0.2, y2_data, color='green', width=0.1, label='Kappa')
plt.bar(index+0.4, y3_data, color='blue', width=0.1, label='Precision')
plt.bar(index+0.6, y4_data, color='olive', width=0.1, label='Recall')
plt.ylim([0.8, 1.0])
plt.xticks(index+0.3, x_data)
plt.legend(loc='upper right')

#plt.show()
plt.savefig('imsi.jpg', format='jpg', dpi=300, bbox_inches='tight')
