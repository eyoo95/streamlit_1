import streamlit as st
import pandas as pd

def run_eda():
    st.subheader('EDA 화면')

    df = pd.read_csv('data2/iris.csv')

    # 컬럼이름을 보여주고 여러 컬럼들을 선택 가능하게 하며 선택한 컬럼만 화면에 보여준다.

    column_list = st.multiselect('컬럼 선택',df.columns)

    if len(column_list) != 0:
        st.dataframe(df[column_list])

    # 아무것도 선택하지 않으면 empty가 뜨는데- 이것을 안보고 싶다면?

    # 상관계수를 구하여 화면에 보여준다.

        st.dataframe(df[column_list].corr())