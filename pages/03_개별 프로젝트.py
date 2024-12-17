import streamlit as st
import pandas as pd

# 데이터 불러오기
@st.cache_data
def load_data():
    file_path = "2024book50.csv"
    data = pd.read_csv(file_path)
    # 컬럼 이름 재정의
    data.columns = ["권장연령", "도서명", "지은이", "출판사", "주제어", "가격", "ISBN", "도서소개"]
    return data

data = load_data()

# 제목과 설명
st.title("📚 고등학생 추천 도서 프로그램 📚")
st.write("🎯 **관심 분야나 주제어를 입력해보세요**! 맞춤 도서를 추천해드립니다. 😊")

# 사용자 입력
interest = st.text_input("🔍 관심 분야나 주제어를 입력해보세요 (예: 경제, 세계사, 수학 등)")

# 도서 추천 함수
def recommend_books(data, keyword):
    keyword = keyword.strip().lower()
    filtered = data[
        data["주제어"].astype(str).str.lower().str.contains(keyword, na=False)
        | data["도서명"].astype(str).str.lower().str.contains(keyword, na=False)
    ]
    return filtered

# 추천 도서 출력
if interest:
    recommendations = recommend_books(data, interest)
    if not recommendations.empty:
        st.subheader("📖 추천 도서 목록")
        for _, row in recommendations.iterrows():
            st.write(f"**📚 {row['도서명']}**")
            st.write(f"🖋️ **지은이:** {row['지은이']}")
            st.write(f"🏢 **출판사:** {row['출판사']}")
            st.write(f"🔖 **주제어:** {row['주제어']}")
            st.write(f"📝 **소개:** {row['도서소개']}")
            st.write("---")
    else:
        st.warning("😢 입력하신 주제에 해당하는 도서가 없습니다. 다른 키워드를 입력해보세요!")
else:
    st.info("🔎 관심 주제나 키워드를 입력해주세요. 예: 경제, 과학, 문학 등")
