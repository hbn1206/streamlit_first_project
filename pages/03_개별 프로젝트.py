import streamlit as st
import pandas as pd

# 데이터 불러오기
@st.cache_data
def load_data():
    data = pd.read_csv("2024book50.csv")
    return data

data = load_data()

# 제목과 설명
st.title("\U0001F4DA 고등학생 도서 추천 프로그램 \U0001F4DA")
st.write("\U0001F9E0 자신의 **진로와 관심분야**를 입력하면 맞춤 도서를 추천해드립니다!")

# 사용자 입력
interest = st.text_input("\U0001F4DD 관심 분야나 진로를 입력해보세요 (예: 과학, 문학, 심리학 등)")

# 데이터 추천 필터링
def recommend_books(data, keyword):
    filtered = data[data.apply(lambda row: keyword.lower() in str(row.values).lower(), axis=1)]
    return filtered

if interest:
    recommendations = recommend_books(data, interest)
    
    if not recommendations.empty:
        st.subheader("\U0001F4A1 추천 도서")
        for index, row in recommendations.iterrows():
            st.write(f"**\U0001F4D6 {row['도서명']}**")
            st.write(f"- \U0001F4DA 저자: {row['저자']}")
            st.write(f"- \U0001F30F 출판사: {row['출판사']}")
            st.write(f"- \U0001F4AC 주제어: {row['주제어']}")
            st.write("---")
    else:
        st.warning("\U0001F615 해당 관심 분야에 대한 추천 도서가 없습니다. 다른 키워드를 입력해보세요!")
else:
    st.info("\U0001F50D 진로와 관심 분야를 입력하고 추천 도서를 확인해보세요!")
