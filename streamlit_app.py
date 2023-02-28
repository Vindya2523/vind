import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('jp.png'))

st.header('G.VINDYA')

st.info('Data science intern, Content Creator')

icon_size = 20

st_button('linkedin', 'https://www.linkedin.com/in/g-vindya-82481a1b0', 'G.Vindya', icon_size)
st_button('instagram', 'https://instagram.com/_vindyaa__?igshid=ZDdkNTZiNTM=', '__vindyaa_', icon_size)
