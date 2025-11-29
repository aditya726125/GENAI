import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("placement.csv")
#print(df)
'''plt.scatter(df["cgpa"], df["package"])
plt.xlabel("CGPA")
plt.ylabel("PACKAGE")
plt.show()'''

#find the null value
#print(df.isnull().sum())

#find the independent and dependent features
x = df.iloc[:,0]
y = df.iloc[:,1]
#print(x)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state = 42)
#print(x_train)

#Train the model
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
print(lr.fit(x_train.values.reshape(-1,1),y_train))
m= lr.coef_
print(m)

b=lr.intercept_
print(b)

cgpa = 9.5
package = m*cgpa + b
print(package)