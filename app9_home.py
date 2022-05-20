import streamlit as st
from PIL import Image
# 함수 단위로 만들어야 한다.

def run_home():
    st.subheader('홈 화면 입니다.')

    st.text('파일분리 실습중')

    img = Image.open('data2/birds.jpg')
    
    st.image(img)