import streamlit as st
import pandas as pd

def main():
    df= pd.read_csv('data2/iris.csv')
    # 버튼 만들기

    #True가 됨
    # if st.button('데이터 보기'): 
    #     st.dataframe(df)
    
    # 대문자 버튼을 만들고 버튼을 누르면 species 컬럼의 값들을 대문자로 변경

    st.dataframe(df)

    if st.button('대문자'):
        df['species'] = df['species'].str.upper()
        st.dataframe(df)

    # 라디오 버튼: 여러개중 한개를 선택할때
    my_order = ['오름차순 정렬','내림차순 정렬']  # 리스트를 먼저 만듦

    status =  st.radio('정렬방법 선택', my_order)

    if status == my_order[0]:   # petal_length 를 오름차순으로
        st.dataframe(df.sort_values('petal_length'))  # 정렬한것을 메모리에 저장해야 화면에 나오게 된다.
    elif status == my_order[1]:
        df.sort_values('petal_length', ascending=False, inplace= True)
        st.dataframe(df)


     # 셀렉트 박스
    langauge = ['Python','C','Java','Go','PHP']
    st.selectbox('좋아하는 언어 선택',langauge)

    #체크박스
    if st.checkbox('헤드 5개 보기'):
        st.dataframe(df.head())
    else:
        st.text('헤드를 숨겼습니다.')

   



   


   




if __name__ == '__main__':
    main()