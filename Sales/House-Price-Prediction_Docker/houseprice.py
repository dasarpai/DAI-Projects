import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
import pickle

data = pd.read_csv("kc_house_data.csv")

labels = data['price']
conv_dates = [1 if values == 2014 else 0 for values in data.date ]
data['date'] = conv_dates
train1 = data.drop(['id', 'price'],axis=1)

col_imp = ["grade", "lat", "long", "sqft_living", "waterfront", "yr_built"]

model_houseprice = GradientBoostingRegressor(n_estimators = 400, max_depth = 5, min_samples_split = 2)
model_houseprice.fit(train1[col_imp], labels)

#Save the model
pickle.dump(model_houseprice, open('model_houseprice.pkl', 'wb'))

#load the model
model_houseprice = pickle.load(open('model_houseprice.pkl', 'rb'))

#["grade", "lat", "long", "sqft_living", "waterfront", "yr_built"]
print(model_houseprice.predict([[13,47.2559, -122.419, 1600, 1, 2000]]))