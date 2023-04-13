import pandas as pd
import numpy as np


import matplotlib.pyplot as plt
import seaborn as sns 


import warnings
warnings.filterwarnings("ignore")


df = pd.read_csv("./DATA/default_of_credit_card_clients.csv")
#print(df.columns)

del df[df.columns[0]]

#print(df.columns)

df.rename(columns={ 'ID':'id', 'LIMIT_BAL':'bal',
                    'SEX':'gen', 'EDUCATION':'edu',
                    'MARRIAGE':'mary', 'AGE':'age',
                    'PAY_1':'p1', 'PAY_2':'p2',
                    'PAY_3':'p3','PAY_4':'p4',
                    'PAY_5':'p5','PAY_6':'p6',
                    'BILL_AMT1':'$b1', 'BILL_AMT2':'$b2',
                    'BILL_AMT3':'$b3', 'BILL_AMT4':'$b4',
                    'BILL_AMT5':'$b5', 'BILL_AMT6':'$b6',
                    'PAY_AMT1':'$p1','PAY_AMT2':'$p2',
                    'PAY_AMT3':'$p3', 'PAY_AMT4':'$p4',
                    'PAY_AMT5':'$p5', 'PAY_AMT6':'$p6'
                    }, inplace=True)

print(df.columns)

'''  WE WILL CHECK how various bal classification   '''

print(df['bal'].max(), df['bal'].min(), 'bal varies from 10 K to 1 M' )

'''  SHOW THE CONTRAST OF CREDIT RESPONSE WITH TIME for bal>500K and bal<500K
IN ONE bar plot '''

df25K = df[  (df['bal']<=25000)  ]
df100K = df[ (df['bal']>25000) & (df['bal']<=100000) ]
df500K = df[ (df['bal']>100000) & (df['bal']<=500000) ]
df1000K = df[ (df['bal'])>500000 ]

print(len(df1000K)*100/30000.0)
print(len(df25K)+len(df100K)+len(df500K)+len(df1000K))


dfs = [df25K, df100K, df500K, df1000K]
M = [ 'p1', 'p2', 'p3', 'p4', 'p5', 'p6' ]
Mb = [ 'bp1', 'bp2', 'bp3', 'bp4', 'bp5', 'bp6' ]


for itms in dfs:
    df1 = itms[ M ]
    i = 0
    for col in Mb:
        itms[col]=itms[M[i]].apply(lambda x: 1 if(x<=0) else 0)
        i = i + 1


plt.figure(figsize=(10,5))
leg = ['10-25K', '25-100K', '100-500K', '500-1000K']


M_TO_M_ND = []

j = 0
for itms in dfs:
    df1 = itms[M]
    m_to_m_ND = np.zeros(6)
    i = 0
    for col in Mb:
        #print(itms[col].value_counts()[1]*100.0/itms[col].value_counts().sum())
        r = itms[col].value_counts()[1]/itms[col].value_counts().sum()
        m_to_m_ND[i] = r
        M_TO_M_ND.append(r)
        i += 1
    plt.plot(np.arange(1,7,1), m_to_m_ND, alpha=0.3, label=leg[j], marker='s')
    plt.legend()
    plt.autoscale(tight=False, enable=True)
    plt.grid(True)
    j += 1

plt.title(' Month to month pay record for various credit limit group ')
plt.xticks([1,2,3,4,5,6], ('APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP'))
plt.show()
        
'''  MACHINE LEARNING  '''



from sklearn.model_selection import train_test_split
x_tr, x_t, y_tr, y_t = train_test_split(df[ ['p1', 'p2', 'p3', 'p4', 'p5', 'p6'] ],
                                        df['DPNM'], test_size=0.3)


from sklearn.metrics import roc_auc_score, classification_report
from sklearn import ensemble
from sklearn.ensemble import GradientBoostingClassifier

clf = ensemble.GradientBoostingClassifier()
clf.fit(x_tr, y_tr)
y_p = clf.predict(x_t)
roc = roc_auc_score(y_t, y_p)
print("ROC Score : ", roc)
print(" Classification Report : \n\n", classification_report(y_t, y_p) )


x = np.reshape(M_TO_M_ND, (4,6))
print("\n\n", np.shape(M_TO_M_ND), np.shape(x))


P = pd.DataFrame({leg[0]:x[0,:]})

for i in range(1,4):
    P[leg[i]] = x[i,:]

print(P)

















