import numpy as np
import pandas as pd
df2 =  pd.DataFrame([[1, 'j', 'good', 'male'],[2, 'k', 'better', 'male'],
                     [3, 'l', 'average', 'female'],[4, 'm', 'best', 'male']], 
                    columns=['id', 'name', 'feedback', 'gender'])
#print(df2)
gen = {'male':1, 'female':2}
feed = {'good':1, 'better':2, 'average':3, 'best':4}
#print(df2['gender'].map(gen))
#print(df2['feedback'].map(feed))
data =  pd.get_dummies(df2, columns=['gender', 'feedback'])
#print(data)
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

df3 = pd.DataFrame([[0.0],[1.0],[2.0],[3.0],[4.0],[5.0]])
print(MinMaxScaler().fit_transform(df3))
print(StandardScaler().fit_transform(df3))