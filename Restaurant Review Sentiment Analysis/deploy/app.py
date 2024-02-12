import streamlit as st
import eda 
import predictions


navigation = st.sidebar.selectbox('Page : ', ('Explore Data', 'Predict Sentiment'))

if navigation == 'Explore Data':
    eda.run()
else:
    predictions.run()