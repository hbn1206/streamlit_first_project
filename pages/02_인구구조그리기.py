import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
@st.cache_data
def load_data():
    file_path = "age2411.csv"  # 업로드된 파일 경로
    data = pd.read_csv(file_path)
    return data

data = load_data()

# 지역 선택 및 데이터 처리
st.title("📊 지역별 인구 구조 시각화")
st.write("원하는 지역을 선택하면 해당 지역의 연령대별 인구 구조를 그래프로 보여줍니다.")

# 지역 목록 가져오기
regions = data['행정구역'].unique()
selected_region = st.selectbox("지역을 선택하세요:", regions)

# 선택한 지역 데이터 필터링
filtered_data = data[data['행정구역'] == selected_region]

# 연령대별 데이터 추출
age_columns = [col for col in data.columns if '계_' in col and '세' in col]
age_data = filtered_data[age_columns].T
age_data.columns = ['Population']
age_data.index = [col.split('_')[-1] for col in age_columns]  # 연령대 이름 추출

# 그래프 시각화
fig, ax = plt.subplots(figsize=(10, 6))
age_data['Population'].plot(kind='bar', ax=ax)
ax.set_title(f"{selected_region} 연령대별 인구 구조")
ax.set_xlabel("연령대")
ax.set_ylabel("인구 수")
plt.xticks(rotation=45)
st.pyplot(fig)
