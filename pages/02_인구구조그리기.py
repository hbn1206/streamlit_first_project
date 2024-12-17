import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
import platform

# 한글 폰트 자동 설정
def set_font():
    if platform.system() == 'Windows':
        rc('font', family='Malgun Gothic')  # Windows 기본 한글 폰트
    elif platform.system() == 'Darwin':
        rc('font', family='AppleGothic')  # Mac 기본 한글 폰트
    else:
        rc('font', family='DejaVu Sans')  # Linux 기본 폰트 (한글 지원)

set_font()

# 데이터 불러오기
@st.cache_data
def load_data():
    file_path = "age2411.csv"  # 업로드된 파일 경로
    data = pd.read_csv(file_path)
    return data

data = load_data()

# 제목 및 설명
st.title("📊 두 지역의 인구 구조 비교 시각화")
st.write("두 지역명을 입력하면 해당 지역의 연령대별 인구 구조를 꺾은선 그래프로 비교해 보여줍니다.")

# 지역 입력창
region1 = st.text_input("첫 번째 지역명을 입력하세요 (예: 서울특별시 종로구):")
region2 = st.text_input("두 번째 지역명을 입력하세요 (예: 경기도 하남시):")

if region1 and region2:
    # 입력한 두 지역으로 필터링
    data1 = data[data['행정구역'].str.contains(region1)]
    data2 = data[data['행정구역'].str.contains(region2)]

    if not data1.empty and not data2.empty:
        st.write(f"### 비교 지역: {region1} vs {region2}")

        # 연령대별 데이터 추출
        age_columns = [col for col in data.columns if '계_' in col and '세' in col]
        age_data1 = data1[age_columns].iloc[0].T
        age_data2 = data2[age_columns].iloc[0].T

        age_data1.index = [col.split('_')[-1] for col in age_columns]
        age_data2.index = [col.split('_')[-1] for col in age_columns]

        # 그래프 시각화 (꺾은선 그래프)
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(age_data1.index, age_data1.values, label=region1, color='red')
        ax.plot(age_data2.index, age_data2.values, label=region2, color='blue')
        ax.set_title("두 지역의 연령대별 인구 구조 비교")
        ax.set_xlabel("연령대")
        ax.set_ylabel("인구 수")
        plt.xticks(rotation=45)
        plt.legend()
        st.pyplot(fig)
    else:
        st.error("입력한 지역명 중 하나 또는 둘 모두를 찾을 수 없습니다. 다시 확인해주세요.")
