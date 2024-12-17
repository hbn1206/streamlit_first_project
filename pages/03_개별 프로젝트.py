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
st.title("📊 지역별 고등학생 인구 현황 시각화")
st.write("15세~18세 인구를 기준으로 지역별 고등학생 현황을 보여줍니다.")

# 고등학생 연령대 컬럼 추출
high_school_columns = ['2024년11월_계_15세', '2024년11월_계_16세', '2024년11월_계_17세', '2024년11월_계_18세']
data['고등학생인구'] = data[high_school_columns].sum(axis=1)

# 시각화 대상 지역 필터링
input_region = st.text_input("지역명을 입력하세요 (예: 서울특별시, 경기도):")

if input_region:
    filtered_data = data[data['행정구역'].str.contains(input_region)]
    if not filtered_data.empty:
        # 정렬 및 상위 10개 지역 선택
        sorted_data = filtered_data[['행정구역', '고등학생인구']].sort_values(by='고등학생인구', ascending=False).head(10)

        # 시각화
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.barh(sorted_data['행정구역'], sorted_data['고등학생인구'], color='skyblue')
        ax.set_title(f"{input_region} 지역의 고등학생 인구 현황 (상위 10개)")
        ax.set_xlabel("고등학생 인구 수")
        ax.set_ylabel("행정구역")
        st.pyplot(fig)
    else:
        st.error("입력한 지역명이 데이터에 없습니다. 다시 확인해 주세요.")
