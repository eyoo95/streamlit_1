import streamlit as st
import pandas as pd
import altair as alt

def main():
    # 스트림릿에서 제공해주는 line_chart, area_chart

    df1 = pd.read_csv('data2/lang_data.csv')
    st.dataframe(df1)

    lang_list = df1.columns[1:]
    choice_list = st.multiselect('언어를 선택하세요',lang_list)
    if len(choice_list)!=0:
        df_choice = df1[choice_list]
        st.dataframe(df_choice)

        # 스트림릿이 제공하는 line_chart
        st.line_chart(df_choice)

        # 스트림릿이 제공하는 area_chart
        st.area_chart(df_choice)

    df2 = pd.read_csv('data2/iris.csv')

    # 스트림릿이 제공하는 bar_chart
    st.bar_chart(df2.iloc[:,0:-1])


    # 웹에서 사용할수있는 차트 라이브러리 중 Altair 차트

    alt_chart = alt.Chart(df2).mark_circle().encode(
        x = 'petal_length',
        y = 'petal_width',
        color = 'species'
    )

    st.altair_chart(alt_chart)









if __name__ == '__main__':
    main()