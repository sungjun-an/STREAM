import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import pandas as pd

st.sidebar.header("Predict")

new_model = tf.keras.models.load_model('model.h5')
labels = ['비행기', '자동차', '새', '고양이', '사슴', '개', '개구리', '말', '배', '트럭']
width = 32
height = 32
channel = 3

def image_resize(image):
    return image.resize((32,32))

def image_rotate(image):
    return image.transpose(Image.ROTATE_180)

def image_change_bw(image):
    return image.convert('L')

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
    if 'image' not in st.session_state:
        st.session_state['image'] = img

if 'image' in st.session_state:
    st.image(st.session_state['image'])

predict=st.button("예측하기")

if predict:
    img = st.session_state['image']
    img = np.array(img)
    del st.session_state['image']
    x_test = img.astype('float32') / 255.0
    y_prob = new_model.predict(x_test.reshape(1,width, height, channel), verbose=0)
    st.write(labels[np.argmax(y_prob)])