import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import tensorflow_hub as hub

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model

from keras import layers
import streamlit as st
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')

model = tf.keras.models.load_model('FINAL_TRF.h5', custom_objects={'KerasLayer': hub.KerasLayer})


def run():
    st.write('## Sentiment for Restaurant Reviews')
    st.markdown('***')

    with st.form(key='form_parameters'):
        review = st.text_input('Input Review', value='')
        st.markdown('***')
        submitted = st.form_submit_button('Detected Review')


    data_inf = { 
            'review': review
        }
    data_inf = pd.DataFrame(data_inf, index=[0])


    ##################################################### PREPROCESSED
        # Create Lemmatizer and Stopwords
    stpwds_eng = list(set(stopwords.words('english')))
    stpwds_eng.extend(['oh', 's'])

        # lemmatization
    lemmatizer = WordNetLemmatizer()

    #Create Preprocessing Function
    def text_preprocessing(text):

        text = text.lower() #to lowercase

        text = re.sub("@[A-Za-z0-9_]+", " ", text)# Remove Mention

        text = re.sub("#[A-Za-z0-9_]+", " ", text)# Remove Hashtag

        text = re.sub(r"\\n", " ",text)# Remove \n

        text = text.strip() # Remove Whitespace

        text = re.sub(r"http\S+", " ", text) # Remove Link
        text = re.sub(r"www.\S+", " ", text)

        text = re.sub("[^A-Za-z\s']", " ", text)# Remove symbols, emojis

        tokens = word_tokenize(text)# Tokenization

        text = ' '.join([word for word in tokens if word not in stopwords.words('english')])# Remove Stopwords

        text = lemmatizer.lemmatize(text)# Lemmatizing using WordLemmatizer

        return text
    
    # Applying the function of pre processing
    data_inf['text_processed'] = data_inf['review'].apply(lambda x: text_preprocessing(x))

    if submitted:
    # Prediction
        teks_prediction = model.predict(data_inf['text_processed'])
        sentiment_labels = ['Like' if pred >= 0.5 else 'Do not like' for pred in teks_prediction]
        data_inf['prediction_sentiment'] = sentiment_labels
        data_inf = pd.DataFrame(data_inf, index=[0])  # Explicitly set the index
        st.table(data_inf)



if __name__ == '__main__':
    run()