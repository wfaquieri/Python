#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import pandas as pd
import numpy as np

df = pd.read_excel (r'path\Database_1.xlsx') 
df['x_1'] = df['pond_base'] / df['r_1']
df['s_1'] = np.nansum(df['x_1'])
df['pond_1'] = (df['x_1'] / df['s_1'])*100
df['indice_1'] = df['indice_base'] / df['relativo_base']

N = 61
for i in range(2, N):
    j = i - 1
    df['var_' + str(j)] =  (df['r_' + str(j)] - 1)*100
    df['influencia_' + str(j)] = (df['pond_' + str(j)] * df['var_' + str(j)])/100
    df['x_' + str(i)] = df['pond_' + str(j)] / df['r_' + str(i)]
    df['s_' + str(i)] = np.nansum(df['x_' + str(i)])
    df['pond_' + str(i)] = (df['x_' + str(i)] / df['s_' + str(i)])*100
    df['indice_' + str(i)] = df['indice_' + str(j)] / df['r_' + str(j)]
print(df)

for i in range(1, N):
    d = {'pond_base': df['pond_base'], 'indice_base': df['indice_base'], 'variacao_base': df['variacao_base'], 'relativo_base': df['relativo_base'], 
     'influencia_base': df['influencia_base'], 'pond_' + str(i): df['pond_' + str(i)], 'indice_' + str(i): df['indice_' + str(i)],
    'var_' + str(i): df['var_' + str(i)], 'influencia_' + str(i): df['influencia_' + str(i)]}
        
print(d)


df.to_excel(r'C:\Users\winicius.faquieri\Desktop\Winicius\ISSVS\Python\output_2.xlsx')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




