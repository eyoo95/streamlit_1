from sqlalchemy import column
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


    #체크박스
    if st.checkbox('헤드 5개 보기'):
        st.dataframe(df.head())
    else:
        st.text('헤드를 숨겼습니다.')



    # 셀렉트 박스: 여러개중 한개만 고른다.
    langauge = ['Python','C','Java','Go','PHP']
    my_choice = st.selectbox('좋아하는 언어 선택',langauge)

    if my_choice == langauge[0]:
        st.write('파이썬을 선택했습니다.')
    elif my_choice == langauge[1]:
        st.write('C를 선택했습니다.')
    elif my_choice == langauge[2]:
        st.write('자바를 선택했습니다.')


    # 멀티셀렉트: 여러개중 여러개를 선택한다.

    st.multiselect('좋아하는 언어 선택',langauge)

    # 멀티셀렉트를 이용해서 특정 컬럼들만 가져오기
    # 유저에게 iris의 컬럼들을 다 보여주고 
    # 유저가 선택한 컬럼들만 데이터프레임화면에 보여줄것

    column_list = df.columns

    choice_list = st.multiselect('컬럼을 고르세요',column_list)
    st.dataframe(df[choice_list])


    # 슬라이더: 숫자 조정에 사용

    #st.slider('나이',0,120, 30, 5)

    age = st.slider('나이',0,120, 30)

    st.text('제가 선택한 나이는 {}입니다.'.format(age))


    # 익스펜더

    with st.expander('Hello'):
        st.text('안녕하세요')
        st.dataframe(df)


   

    





if __name__ == '__main__':
    main()
