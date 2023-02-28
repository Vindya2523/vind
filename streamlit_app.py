import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()


col1, col2, col3 = st.columns(3)
col2.image(Image.open('IMG_1677565927967.png'))

st.header('Hello guys!')

st.info('Add  me  on  linkedin  by  clicking  the  button  below')

icon_size = 20

st_button('linkedin', 'https://www.linkedin.com/in/g-vindya-82481a1b0', 'G.Vindya', icon_size)

