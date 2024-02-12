import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image



def run():
    # Membuat title
    st.title('Predicting Hotel Cancelation ')
    #Menambahkan deskripsi
    st.write('by Masayu Anandita Prameswari')
    st.markdown('----')

    #Membuat subheader
    st.write('## Exploratory Data Customer')

    #Tambahkan gambar
    image = Image.open('hotel2.jpg')
    st.image(image, caption=' "WELLCOME TO GRAND RINJANI HOTEL !" ') 
    st.markdown('----')

    #Show dataframe
    st.subheader('Reservation Data')
    df = pd.read_csv('Hotel_Reservations.csv')
    st.table(df.head())
    st.markdown('---')

    #value counts
    st.subheader('Hotel Boking Cancelation Percentage')
    value_counts = df['booking_status'].value_counts()
    # pie chart
    fig = plt.figure(figsize=(8,5)) 
    plt.pie(value_counts, autopct='%1.2f%%', explode = [0, 0.1], shadow=True, colors=sns.color_palette('pastel'))
    st.pyplot(fig)
    st.write('''The percentage of customers who canceled in the period 2017 to 2018 was around 67%''')
    st.markdown('---')

    #visualization of month
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.subheader('Room Type Reserved Distribution')
    # Plot using seaborn
    plt.figure(figsize=(20, 25))
    plt.subplot(4, 2, 2)
    plt.title('Room Type Reserved')
    sns.countplot(x='room_type_reserved', palette='pastel', data=df)
    plt.xlabel('Room Count Reserved')
    st.pyplot()
    st.write('''There are 7 type room in Grand Rinjani hotel, the most reserved room is room type 1, follow by room type 4 and type 6.''')
    st.markdown('---')


    plt.figure(figsize=(10, 8))
    st.subheader('Booking Status with Market Segment')
    # presentase cancel online dan offline
    sns.histplot(data = df,x='market_segment_type', hue='booking_status', palette='magma')
    st.pyplot()
    st.write('''Most customers choose to book hotels online compared to offline, but it also appears that more customers are canceling reservations. 
             There are not as many corporate bookings but the chances of canceling them are much less.''')
    st.markdown('***')


    plt.figure(figsize=(10, 8))
    st.subheader('Bookings by Month')
    # presentase cancel online dan offline
    sns.histplot(data=df, x='arrival_month', palette='flare', hue='market_segment_type')
    st.pyplot()
    st.write('''The number of bookings increases on August to December and mostly customer booking by online.''')
    st.markdown('***')


    st.write('### Lead Time & Booking Status')
    sns.displot(df, x='lead_time', hue='booking_status', kind='kde', fill=True, height=5, aspect=1.5)
    plt.axvline(df[df.booking_status == 'Not_Canceled'].lead_time.mean(),ls='--')
    plt.axvline(df[df.booking_status == 'Canceled'].lead_time.mean(),ls='--', c='orange')
    st.pyplot()
    st.write('''Customers who make bookings on average around > 100 days from the check-in date have a greater possibility of canceling, 
             whereas if customers make bookings for a maximum of 90 days in the future, they tend not to cancel.''')
    st.markdown('***')

if __name__ == '__main__':
    run()