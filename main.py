import streamlit as st

def get_mbti_info(mbti):
    mbti_data = {
        "ISTJ": ("✈️ 관리자형", "🎓 세밀하고 책임감이 강해 공무원, 관리자, 회계사와 잘 어울림!", "👯 ISFJ와 최고의 팀워크를 자랑함!"),
        "ISFJ": ("🛏️ 수호자형", "✨ 봉사정신이 강하고 꼼꼼해서 간호사, 교사, 비서로 안성맞춤!", "🤝 ESFP와 함께라면 환상의 호흡!"),
        "INFJ": ("🌍 옹호자형", "🕊❤️ 직관적이고 배려심이 깊어 상담가, 심리학자, 예술가로 활약함!", "💕 ENFP와 깊은 관계를 형성함."),
        "INTJ": ("📊 전략가형", "💡 체계적이며 혁신적이라 연구원, 과학자, 개발자에 적합함.", "⚡ ENTJ와 시너지 폭발!"),
        "ISTP": ("⚖️ 만능 재주꾼형", "🛠️ 논리적이고 손재주가 뛰어나 엔지니어, 기술자에 딱 맞음.", "❤️ ESTP와 최고의 파트너십!"),
        "ISFP": ("🎨 예술가형", "🌟 감각적이고 따뜻해서 디자이너, 예술가, 요리사로 빛남!", "🤍 ESFJ와 아름다운 조화를 이룸."),
        "INFP": ("🌍 중재자형", "🌟 이상적이고 창의적이라 작가, 심리학자, 상담가가 어울림!", "💖 ENFJ와 깊은 유대감을 형성함."),
        "INTP": ("🤝 논리술사형", "⚛️ 지적 호기심이 많아 과학자, 철학자, 연구자에 적합함.", "📏 ENTJ와 지식 시너지를 이룸."),
        "ESTP": ("🏆 모험가형", "🎈 활동적이고 현실적이라 사업가, 경찰, 운동선수로 어울림!", "👨‍💼 ISFP와 최고의 조합!"),
        "ESFP": ("🎉 엔터테이너형", "🎤 사교적이고 긍정적이라 연예인, 이벤트 기획자로 두각을 나타냄!", "🥰 ISFJ와 함께라면 행복 두 배!"),
        "ENFP": ("💫 활동가형", "✨ 열정적이고 창의적이라 마케터, 작가, 예술가에 적합함!", "🤝 INFJ와 놀라운 케미를 보여줌."),
        "ENTP": ("⚡ 변론가형", "📢 도전적이고 독창적이라 발명가, 기업가, 언론인이 제격!", "⚡ INTJ와 함께라면 무적 콤비!"),
        "ESTJ": ("💼 경영자형", "📈 체계적이고 리더십이 강해 관리자, 경영자, 군인으로 어울림.", "🤍 ISFJ와 최고의 조직력을 만듦."),
        "ESFJ": ("🎓 집정관형", "💖 친절하고 사교적이라 교사, 간호사, 사회복지사로 활약함.", "🤝 ISFP와 환상적인 조합!"),
        "ENFJ": ("❤️ 선도자형", "✨ 사람을 이끄는 리더십으로 교사, 멘토, 리더에 적합함.", "💕 INFP와 영적인 연결을 형성함."),
        "ENTJ": ("💥 지휘관형", "⚛️ 야망있고 효율적이라 CEO, 경영자, 정치인으로 활약함!", "⚡ INTJ와 혁신을 만들어냄.")
    }
    return mbti_data.get(mbti, ("\U0001F914 잘못된 선택", "선택한 MBTI가 없습니다.", "⚠️ 다시 확인해주세요."))

# Streamlit UI 시작
st.title("MBTI✨ 직업과 궁합 탐색기")
st.write("당신의 MBTI를 선택하면 잘 맞는 직업과 사람을 알려드릴게요! 🚀")

# MBTI 선택 드롭다운
mbti_options = [
    "ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]
user_mbti = st.selectbox("당신의 MBTI를 선택해주세요! 🔍", options=mbti_options)

# MBTI 설명 가져오기
mbti_type, career, compatibility = get_mbti_info(user_mbti)

# 결과 출력
st.subheader(f"{user_mbti} - {mbti_type}")
st.write(f"**💼 잘 맞는 직업:** {career}")
st.write(f"**💖 잘 맞는 사람:** {compatibility}")

st.write("\n")
st.write("MBTI를 통해 더 많은 자신을 발견해보세요! 🌠")
