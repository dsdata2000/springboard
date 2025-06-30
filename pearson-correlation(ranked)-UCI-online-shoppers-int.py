import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("./DATA/online_shoppers_intention.csv")
print(df.info())

'''
['Administrative', 'Administrative_Duration', 'Informational',
       'Informational_Duration', 'ProductRelated', 'ProductRelated_Duration',
       'BounceRates', 'ExitRates', 'PageValues', 'SpecialDay', 'Month',
       'OperatingSystems', 'Browser', 'Region', 'TrafficType', 'VisitorType',
       'Weekend', 'Revenue']

'''


df = df[ df['Administrative_Duration']>=0]
df = df[ df['Informational_Duration']>=0 ] 
df = df[ df['ProductRelated_Duration']>=0] 


mon_idx = df['Month'].value_counts().index.tolist()

df['Month'].replace(to_replace=mon_idx,
            value=np.arange(1,len(mon_idx)+1),inplace=True)

vt_idx = df['VisitorType'].value_counts().index.tolist()
df['VisitorType'].replace(to_replace=vt_idx,
                          value=np.arange(1,len(vt_idx)+1), inplace=True)

we_idx = df['Weekend'].value_counts().index.tolist()

df['Weekend'].replace(to_replace=we_idx,
                      value=np.arange(1,len(we_idx)+1),inplace=True)

r_idx = df['Revenue'].value_counts().index.tolist()
df['Revenue'].replace(to_replace=r_idx,
                      value=np.arange(1,len(r_idx)+1), inplace=True)


df_corr = df.corr(method='pearson')
plt.figure(num=1,figsize=(6,6))
sns.heatmap(df_corr, annot=True, annot_kws={"size":8}, fmt='0.3f')
plt.title(" Attributes correlation: Online Shoppers Revenue dataset")
plt.show()


attr = df_corr.iloc[:,17].index.tolist()
c_val = df_corr.iloc[:,17].values.tolist()
c_val.remove(c_val[-1])

idx_d = np.argsort(c_val).tolist()
idx_a = idx_d

c_attr = []
corr_sort = []

for v in idx_a:
    c_attr.append(attr[v])
    corr_sort.append(c_val[v])

df_corr1 = pd.DataFrame({'attr':c_attr, 'correlation':corr_sort})
df_corr1 = df_corr1.set_index(df_corr1['attr'])

print(df_corr1)
plt.figure(num=2, figsize=(6,6))
df_corr1['correlation'].plot(kind='barh')
plt.xlabel("Pearson Correlation Coefficient")
plt.title('Correlation(ranked): Online Shoppers Intention dataset-UCI')
plt.show()








