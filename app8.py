import streamlit as st
from PIL import Image
import pandas as pd
import os 
from datetime import datetime

# 디렉토리 정보와 파일을 알려주면, 해당 디렉토리에
# 파일을 저장하는 함수
def save_uploaded_file(directory, file) :
    # 1.디렉토리가 있는지 확인하여, 없으면 디렉토리부터만든다.
    if not os.path.exists(directory) :
        os.makedirs(directory)
    # 2. 디렉토리가 있으니, 파일을 저장.
    with open(os.path.join(directory, file.name), 'wb') as f :
        f.write(file.getbuffer())
    return st.success("Saved file : {} in {}".format(file.name, directory))

# 스트림릿 라이브러리를 사용하기 위한 임포트
import streamlit as st

# 웹 대시보드 개발 라이브러리인 스트림릿은 main 함수가 있어야 한다.

def main():
    st.title('여러파일 한번에 업로드 하는 앱')
    
    menu = ['Image','CSV','About']
    choice = st.sidebar.selectbox('메뉴',menu)


    if choice == menu[0]:   # accept multiplefiles를 세팅하면 여러파일을 한꺼번에 올릴수있다.
        upload_files = st.file_uploader('이미지 파일을 선택', type=['jpg','png','jpeg','jfif'],accept_multiple_files=True)

        if upload_files is not None:  # upload_files는 여러 파일을 저장하고 있는 리스트다, 따라서 업로드 파일이 있는 경우에만 아래코드를 실행해 저장해야 한다.
            for file in upload_files: # 업로드 파일이 리스트니까 하나씩 가져와서 폴더에 저장할것
            #파일명을 유니크하게 만들어서 저장
            # 현재시간을 활용해서 만든다.
                current_time = datetime.now()
                new_filename = current_time.isoformat().replace(':','_') + '.png'


                file.name = new_filename
                save_uploaded_file('temp', file)  # 여기까지가 저장

            #저장이 다 끝나면 웹브라우저에 이미지를 표시하자
            for file in upload_files:
                img = Image.open(file)
                st.image(img)
    # CSV파일을 저장하면 temp에 올리고 데이터프레임으로 읽어서 화면에 표시
    elif choice == menu[1]:
        upload_files = st.file_uploader('csv 파일을 선택',type={'csv'}, accept_multiple_files=True)

        if upload_files is not None:
            for file in upload_files:
                current_time = datetime.now()
                new_filename = current_time.isoformat().replace(':','_')+'.csv'
                file.name = new_filename
                save_uploaded_file('temp',file)

            for file in upload_files:
                df = pd.read_csv(file)
                st.dataframe(df)  #UTF-8로 변환해서 저장





if __name__ == '__main__':
    main()