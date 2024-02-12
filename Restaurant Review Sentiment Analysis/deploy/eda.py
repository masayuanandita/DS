import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')

def run():
    # Membuat title
    st.title('Sentiment Analysis Hotel Review')
    #Menambahkan deskripsi
    st.write('by Masayu Anandita Prameswari')
    st.markdown('----')

    #Membuat subheader
    st.write('## Exploratory Data Analysis')

    #Tambahkan gambar
    image = Image.open('restaurant_.jpg')
    st.image(image, caption=' "WELLCOME TO RINJANI RESTAURANT !" ') 
    st.markdown('----')

    #Show dataframe
    st.subheader('Restaurant Review Data')
    df = pd.read_csv('Restaurant_Reviews.tsv',sep='\t')
    st.table(df.head())
    st.markdown('---')

    #value counts
    st.subheader('Liked or Not Percentage')
    value_counts = df['Liked'].value_counts()
    # pie chart
    fig = plt.figure(figsize=(8,5)) 
    plt.pie(value_counts, autopct='%1.2f%%', explode = [0, 0.1], shadow=True, colors=sns.color_palette('pastel'))
    st.pyplot(fig)
    st.write('''In the pie chart above, 0 means customer like the restaurant and 1 stands for not.''')
    st.markdown('---')

    # display wordcloud
    st.subheader('Restaurant review words')
    all_messages = ' '.join(df['Review'])
    wordCloud = WordCloud(width=500, height=300, random_state=20, max_font_size=100).generate(all_messages)

    # Display the WordCloud image in Streamlit
    st.image(wordCloud.to_array(), caption='WordCloud', use_column_width=True)
    st.markdown('---')

    ############################################################################################# WORDCLOUD AFTER
    #Create Preprocessing Function

    # Stopwords
    stpwds_eng = list(set(stopwords.words('english')))
    stpwds_eng.append(['oh','s'])

        # lemmatization
    nltk.download('wordnet')
    # Initialize the lemmatizer
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
    df['text_processed'] = df['Review'].apply(lambda x: text_preprocessing(x))

    # display wordcloud
    st.subheader('Restaurant review words after preprocessing')
    all_messages = ' '.join(df['text_processed'])
    wordCloud = WordCloud(width=500, height=300, random_state=20, max_font_size=100, background_color="white").generate(all_messages)

    # Display the WordCloud image in Streamlit
    st.image(wordCloud.to_array(), caption='WordCloud', use_column_width=True)
    st.markdown('---')


if __name__ == '__main__':
    run()

