import streamlit as st
from PIL import Image
import eda 
import predictions

page = st.sidebar.selectbox(label='Page:', options=['Beranda', 'Exploration Data Analysis', 'Prediction'])

if page == 'Beranda':
    st.title('Predicting Hotel Cancelation')
    st.write('FTDS - Phase 1')
    st.header('')

    #Tambahkan gambar
    image = Image.open('hotel2.jpg')
    st.image(image) 
    st.markdown('----')

    col1, col2 = st.columns(2)

    # ======================= Columns 1 =======================
    col1.write('**Nama             :**')
    col1.write('**Batch            :**')

    # ======================= Columns 2 =======================
    col2.write('Masayu Anandita Prameswari')
    col2.write('RMT-026')
    
    st.write('-----')
    with st.expander("Conceptual Problem "):
        st.caption("1. Jelaskan latar belakang adanya bagging dan cara kerja bagging !")
        st.write('''a. Bagging is a technique used to improve the performance and robustness of machine learning models.
                    b. The idea behind bagging is to reduce the variance of a model by training multiple instances of the model on different subsets of the training data and then combining their predictions.
                    c. Bagging works by involving creating multiple subsets of the training data with replacement (bootstrapping) and training a different model on each subset. Then, the prediction results from these models are taken as the average (for regression) or taken as the majority (for classification).''')
        st.caption("2. Jelaskan perbedaan cara kerja algoritma Random Forest dengan algoritma boosting yang Anda pilih !")
        st.write('''a. Boosting happens to be iterative learning which means the model will predict something initially and self analyses its mistakes as a predictive toiler and give more weightage to the data points in which it made a wrong prediction in the next iteration.
                    b. Random forest is just a collection of trees in which each of them gives a prediction and finally, we collect the outputs from all the trees and considers the mean, median, or mode of this collection as the prediction of this forest depending upon the nature of data (either continues or categorical).''')
        st.caption("3. Jelaskan apa yang dimaksud dengan Cross Validation !")
        st.write('Cross-validation is a technique for testing the effectiveness of a model by training it using a portion of input data and testing it on a portion of input data that is different and has never been used before. This helps determine how well the model performs on new data.')

    with st.expander("Kesimpulan"):
        st.write(" 1. In the 2017-2018 period, around 67% of customers canceled hotel reservations.")
        st.write("2. The majority of individuals who cancel their reservations are those who made hotel bookings through online channels.")
        st.write("3. The period from August to December sees a significant surge in customer demand for hotel bookings.")
        st.write("4. Long interval between hotel booking and the scheduled check-in time correlates with a reduced probability of reservation cancellation.")

elif page == 'Exploration Data Analysis':
    eda.run()
else:
    predictions.run()