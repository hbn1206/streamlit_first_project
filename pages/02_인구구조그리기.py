import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 데이터 불러오기
@st.cache_data
def load_data():
    file_path = "age2411.csv"  # 업로드된 파일 경로
    data = pd.read_csv(file_path)
    return data

data = load_data()

# 제목 및 설명
st.title("📊 지역별 인구 구조 시각화")
st.write("원하는 지역의 이름을 입력하면 해당 지역의 연령대별 인구 구조를 그래프로 보여줍니다.")

# 지역 입력창
input_region = st.text_input("지역명을 입력하세요 (예: 서울특별시 종로구):")

if input_region:
    # 입력한 지역으로 필터링
    filtered_data = data[data['행정구역'].str.contains(input_region)]

    if not filtered_data.empty:
        st.write(f"### 선택한 지역: {input_region}")

        # 연령대별 데이터 추출
        age_columns = [col for col in data.columns if '계_' in col and '세' in col]
        age_data = filtered_data[age_columns].iloc[0].T
        age_data.index = [col.split('_')[-1] for col in age_columns]  # 연령대 이름 추출

        # 그래프 시각화
        fig, ax = plt.subplots(figsize=(10, 6))
        age_data.plot(kind='bar', ax=ax, color='skyblue')
        ax.set_title(f"{input_region} 연령대별 인구 구조")
        ax.set_xlabel("연령대")
        ax.set_ylabel("인구 수")
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.error("입력하신 지역명을 찾을 수 없습니다. 다시 확인해주세요.")
