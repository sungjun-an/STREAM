import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import numpy as np

def image_resize(image):
    return image.resize((224,224))

def image_rotate(image):
    return image.transpose(Image.ROTATE_180)

def image_change_bw(image):
    return image.convert('L')

st.markdown('''
 # Avocado Prices dashboard
 테스트용 데시보드를 만들어봅시다.
 Data source: [kaggle](https://www.kaggle.com/datasets/timmate/avocado-prices-2020)
 ''')

avocado = pd.read_csv("avocado.csv")

table = avocado.groupby("type")[['total_volume','average_price']].mean()

st.dataframe(table)

selected_geo = st.selectbox(label="Geography", options=avocado['geography'].unique())

submitted = st.button("Submit")

if submitted:
    line_fig = px.line(
    avocado[avocado['geography']==selected_geo],
    x='date',y='average_price',
    color='type',
    title=f'{selected_geo} dashboard'
    )
    st.plotly_chart(line_fig)

file = st.file_uploader("이미지 선택", type=['png'])

if file is not None:
    img = Image.open(file)
    st.image(file)

img_resize=st.checkbox(label="이미지 크기")
img_rotation=st.checkbox(label="이미지 회전")
img_color=st.checkbox(label="이미지 흑백")
submite=st.button("변경하기")

if submite:
    if img_resize:
        img = image_resize(img)
    if img_color:
        img = image_change_bw(img)
    if img_rotation:
        img = image_rotate(img)
    st.image(img)