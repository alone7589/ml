import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data=pd.DataFrame({
 "sessions_before":np.random.poisson(10,1000),
 "time_spent_before":np.random.normal(120,30,1000),
 "purchases_before":np.random.poisson(2,1000)
})

data["sessions_after"]=data["sessions_before"]+np.random.normal(1,3,1000)
data["delta"]=data["sessions_after"]-data["sessions_before"]
data["churn"]=np.where(data["delta"]<-3,1,0)

X=data[["sessions_before","time_spent_before","purchases_before"]]
y=data["churn"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

model=RandomForestClassifier()
model.fit(X_train,y_train)

print(model.predict(X_test))