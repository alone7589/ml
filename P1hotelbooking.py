import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("hotel_bookings.csv")

le = LabelEncoder()
data["hotel"] = le.fit_transform(data["hotel"])

X = data[["hotel","lead_time","stays_in_weekend_nights","stays_in_week_nights"]]
y = data["is_canceled"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train,y_train)

hotel = le.transform([input("Hotel: ")])[0]
lead = int(input("Lead time: "))
weekend = int(input("Weekend nights: "))
week = int(input("Week nights: "))

pred = model.predict([[hotel,lead,weekend,week]])

print("High cancellation risk" if pred[0]==1 else "Booking safe")