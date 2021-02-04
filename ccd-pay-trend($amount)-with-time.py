import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("./DATA/default_of_credit_card_clients.csv")
#print(df.columns)
del df[df.columns[0]]


df.columns = ['id', 'bal', 'gen', 'edu', 'mary', 'age',
              'p1', 'p2', 'p3', 'p4', 'p5', 'p6',
              '$b1', '$b2', '$b3', '$b4', '$b5', '$b6',
              '$p1', '$p2', '$p3', '$p4', '$p5', '$p6',
              'DPNM']

print(df.columns)

'''
print(df[['$b1', '$b2', '$b3', '$b4', '$b5', '$b6',
          '$p1', '$p2', '$p3', '$p4', '$p5', '$p6'] ].head())
'''


bpc = ['b$p1', 'b$p2', 'b$p3', 'b$p4', 'b$p5', 'b$p6']


print(df[ ['$b1', '$b2', '$b3', '$p1', '$p2', '$p3'] ].head())

bc = ['$b1', '$b2', '$b3', '$b4', '$b5', '$b6']
pc = [ '$p1', '$p2', '$p3', '$p4', '$p5', '$p6' ]


pbcb = [] # pay-bill comp with binary 

i = 0
for col in pc:
    i = i + 1
    print(col, '\t', bc[i-1])
    for n in range(len(df)):
        if( df[col].iloc[n]>=df[bc[i-1]].iloc[n] ):
            pbcb.append(1)
        else:
            pbcb.append(0)

#print(np.shape(pbcb), pbcb[0:20])

pbcb_r = np.array(pbcb).reshape(6, len(df))
print(pbcb_r[:, 0:20])

ncol = ['$bpc1', '$bpc2', '$bpc3', '$bpc4', '$bpc5', '$bpc6']

i = 0
for col in ncol:
    df[col] = pbcb_r[i,:]
    i += 1

print(df[ncol].head())

'''  SHOW THE CONTRAST OF CREDIT RESPONSE WITH TIME for bal>500K and bal<500K
IN ONE bar plot '''

print(" df['bal'].min() = ", df['bal'].min(), " df['bal'].max() = ", df['bal'].max() )


df25K = df[  (df['bal']<=25000)  ]
df100K = df[ (df['bal']>25000) & (df['bal']<=100000) ]
df500K = df[ (df['bal']>100000) & (df['bal']<=500000) ]
df1000K = df[ (df['bal'])>500000 ]

dfs = [df25K, df100K, df500K, df1000K]

plt.figure(figsize=(14,7))
leg = ['10_25K-> Usually improve month to month',
       '25_100K-> Improve with a linear trend',
       '100_500K -> Usually improve with a positive trend',
       '500_1000K -> Fluctuate at a later time']
j = 0
for itms in dfs:
    df1 = itms[ncol]
    m_to_m_ND = np.zeros(6)
    i = 0
    for col in ncol:
        #print(itms[col].value_counts()[1]*100.0/itms[col].value_counts().sum())
        #print(itms[col].value_counts())
        r = itms[col].value_counts()[1]/itms[col].value_counts().sum()
        m_to_m_ND[i] = r
        i += 1
    plt.plot(np.arange(1,7,1), m_to_m_ND, alpha=0.3, label=leg[j] )
    plt.legend()
    j += 1

plt.title(' Time trend: Clients who paid full bill or more than that ')
plt.xticks([1,2,3,4,5,6], ('APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP'))
plt.show()

''' MACHINE LEARNING   '''

col_ml = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6',
          '$bpc1', '$bpc2', '$bpc3', '$bpc4', '$bpc5', '$bpc6']
from sklearn.model_selection import train_test_split
x_tr, x_t, y_tr, y_t = train_test_split(df[col_ml], df['DPNM'], test_size=0.3)

from sklearn.metrics import roc_auc_score, classification_report
from sklearn import ensemble
from sklearn.ensemble import GradientBoostingClassifier


clf = ensemble.GradientBoostingClassifier()
clf.fit(x_tr, y_tr)
y_p = clf.predict(x_t)
roc = roc_auc_score(y_t, y_p)
print("ROC Score : ", roc)  # 0.66
print("Classification Report : \n\n", classification_report(y_t,y_p))

































