import streamlit as st


def main():
    # 유저들한테 입력을 받는 방법

    # 이름 입력받기

    name = st.text_input('이름을 입력하세요.')

    st.subheader(name + '님 안녕하세요.')

if __name__ == '__main__':
    main()