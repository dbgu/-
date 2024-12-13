# streamlit_app.py
import pandas as pd
import streamlit as st
from fastai.vision.all import *
from PIL import Image
import gdown

# Google Drive 파일 ID
file_id = '1-L8ecCqrZj1QRxuGHbKe309nNciO305G'

# Google Drive에서 파일 다운로드 함수
@st.cache(allow_output_mutation=True)
def load_model_from_drive(file_id):
    url = f'https://drive.google.com/uc?id={file_id}'
    output = 'model.pkl'
    gdown.download(url, output, quiet=False)

    # Fastai 모델 로드
    learner = load_learner(output)
    return learner

# 모델 로드
st.write("모델을 로드 중입니다. 잠시만 기다려주세요...")
learner = load_model_from_drive(file_id)
st.success("모델이 성공적으로 로드되었습니다!")

# 1. 제목
st.title("Streamlit 기본 예제 페이지")

# 2. 부제목
st.subheader("이 페이지는 다양한 Streamlit 기능을 보여줍니다.")

# 3. 판다스 데이터프레임 기반 표 출력
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 30, 29],
    "Country": ["Korea", "USA", "UK"]
})
st.write("데이터프레임 예제")
st.dataframe(df)

# 4. HTML 활용 예제
st.write("HTML 예제")
st.markdown(
    """
    <div style="color: blue; font-size: 20px;">
        HTML을 활용한 예시 텍스트입니다.
    </div>
    """,
    unsafe_allow_html=True
)
# 3. 텍스트 입력에 따라 변경되는 동적 반응
st.write("텍스트를 입력해 보세요.")
text_input = st.text_input("텍스트 입력", "삼성 라이온즈")
if text_input:
    st.write(f"입력된 텍스트: {text_input}")

# 5. HTML과 CSS 활용 예제
st.write("HTML과 CSS 예제")
st.markdown(
    """
    <style>
    .styled-box {
        padding: 10px;
        margin: 5px;
        background-color: lightgreen;
        border-radius: 5px;
        color: darkgreen;
    }
    </style>
    <div class="styled-box">
        HTML과 CSS를 함께 사용하여 스타일링한 박스입니다.
    </div>
    """,
    unsafe_allow_html=True
)

# 6. 이미지 표시
st.write("이미지 표시 예제")
st.image("https://www.streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", caption="Streamlit 로고")

# 7. 유튜브 링크 (썸네일 표시)
st.write("유튜브 동영상 예제")
st.video("https://www.youtube.com/watch?v=B2iAodr0fOo")

