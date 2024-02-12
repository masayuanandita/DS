import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
import json
import sklearn
from sklearn.ensemble import RandomForestClassifier


# Load All Files
pipe_rf_tuned = load('RF_pipe.joblib')

with open('list_num_cols.txt', 'r') as file_2:
  list_num_cols = json.load(file_2)


def run():

  st.write('## Predicting Hotel Cancelation')
  st.markdown('***')

  # Membuat Form
  with st.form(key='form_parameters'):
      name = st.text_input('Name', value='')
      lead_time = st.number_input('Lead Time', min_value=7, max_value=365, step=1, value=20)
      avg_price_per_room = st.number_input('Selected Room Price', min_value=0, max_value=400, value=70)
      no_of_special_requests = st.selectbox(label='Number of Special Request',options=[1, 2, 3, 4, 5]) 
      repeated_guest = st.radio('Regular guest ?', (('Yes','No')))

      st.markdown('***')
  
      
      submitted = st.form_submit_button('Check')
      

  data_inf = { 
      'lead_time': lead_time, 
      'avg_price_per_room': avg_price_per_room, 
      'no_of_special_requests': no_of_special_requests, 
      'repeated_guest': repeated_guest, 

  }

  data_inf = pd.DataFrame([data_inf])
  target_map = {'Yes': 1, 'No' : 0}
  data_inf['repeated_guest'] = data_inf['repeated_guest'].map(target_map)


  st.dataframe(data_inf)

  if submitted:
      
      # Predict using Linear Regression
      y_pred_inf = pipe_rf_tuned.predict(data_inf)
      
      if y_pred_inf == 1:

        st.write('### Will they cancel ? : No ')

      else:
        st.write('### Will they cancel ? : Yes ')

if __name__ == '__main__':
    run()