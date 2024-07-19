def make_model():
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


def predict_price(grade,lat,long,sqft_living,waterfront,yr_built):
    #load the model
    model_houseprice = pickle.load(open('model_houseprice.pkl', 'rb'))

    #["grade", "lat", "long", "sqft_living", "waterfront", "yr_built"]
    price = model_houseprice.predict([[grade,lat,long,sqft_living,waterfront,yr_built]])
    print(price)
    return price

import streamlit as st
import pickle
from sklearn.ensemble import GradientBoostingRegressor

st.header("House Price Pridction ")
grade = st.slider('House Grad', 1, 13)
lat = st.slider ("Latitude", 47.1559 , 47.7776)
long = st.slider("Longitude", -122.519, -121.315)
sqft_living = st.slider('Living area in Sqft.', 290,13500)
waterfront = st.checkbox("Water Front")
yr_built = st.slider("Year Built", 1900,2015)
predictbtn = st.button('Predict House Price')

if predictbtn:
    if grade==0 or lat==0 or long==0 or sqft_living==0 or waterfront==0 or yr_built==0 :
        st.error('Please Supply All the Inputs')
    else:
        price= int(predict_price(grade,lat,long,sqft_living,waterfront,yr_built))
        st.header("Price of this house should be around {0:,} Dollars".format(price))