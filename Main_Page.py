import streamlit as st
import pandas as pd
from PIL import Image


st.title('Netflix Movies and TV Show ')

netflix_data = pd.read_csv('netflix_titles.csv')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(netflix_data)

area_data = netflix_data.groupby('type').count()

st.write(area_data)

image = Image.open('countplot.png')

st.image(image, caption='CountPlot Data')
