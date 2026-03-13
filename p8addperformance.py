import pandas as pd
import numpy as np
from sklearn.metrics import roc_auc_score,log_loss

n=1000

data=pd.DataFrame({
 "predicted_ctr":np.random.uniform(0.01,0.9,n),
 "actual_click":np.random.binomial(1,0.3,n),
 "bid":np.random.uniform(1,10,n)
})

data["revenue"]=data["actual_click"]*data["bid"]

print("CTR:",data["actual_click"].mean())
print("LogLoss:",log_loss(data["actual_click"],data["predicted_ctr"]))
print("AUC:",roc_auc_score(data["actual_click"],data["predicted_ctr"]))
print("Revenue:",data["revenue"].sum())