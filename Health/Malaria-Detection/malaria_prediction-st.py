# import streamlit as st

# # Everything is accessible via the st.secrets dict:

# st.write("DB username:", st.secrets["db_username"])
# st.write("DB password:", st.secrets["db_password"])
# st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])

# And the root-level secrets are also accessible as environment variables:

# import os

# st.write(
#     "Has environment variables been set:",
#     os.environ["db_username"] == st.secrets["db_username"],

import tensorflow as tf
import streamlit as st 
from tensorflow.keras.applications.xception import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
import os

def load_model():
    loaded_model = tf.keras.models.load_model(r'model-Malaria-Detection-xception')
    #loaded_model = tf.keras.models.load_model(r'model-Malaria-Detection-mobilenet2')
    
    # loaded_model.summary()
    #x = tf.random.uniform((10, 3))
    return loaded_model



def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    file = os.path.join(folder_path, selected_filename)
    st.image(file)
    return file

file1 = file_selector('./images/')

# file1 = st.file_uploader('Upload an Image')
# file1 = file1.name
btn = st.button('Submit Image for Prediction')
if btn and file1!=None:
    img = image.load_img(file1, target_size=(71, 71))
    print (img)
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    img_preprocessed = preprocess_input(img_batch)
    
    loaded_model = load_model()
    prediction = np.round(1-loaded_model.predict(img_preprocessed)[0][0],2)

    if prediction<.1:
        title = "Uninfected"       
    else:
        title = "Infected" 
        

    st.subheader("It is "+title)
    st.text('Infaction probability '+ str(prediction*100) +"%" )
    st.image(file1)
