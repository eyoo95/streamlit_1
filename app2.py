import streamlit as st

def main():
    st.title('웹 대시보드')
    st.text('웹 대시보드 개발하기')

    name = '홍길동' # 제 이름은 홍길동입니다.
    print('제 이름은 {}입니다.'.format(name))
    st.text('제 이름은 {}입니다.'.format(name))
    st.header('이 영역은 헤더 영역')

    st.subheader('서브헤더 영역')

    st.success('작업이 성공했을때 사용')

    st.warning('경고 문구 보여주고 싶을때 사용')

    st.info('정보를 보여주고 싶을때 사용')
    st.error('문제가 발생했을때 사용')

    # 파이썬의 함수 사용을 보여주고 싶을때
    st.help(sum)
    st.help(len)



if __name__ == '__main__':
    main()