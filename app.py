import streamlit as st
from recommender import recommend_program

st.set_page_config(page_title="영어 영상 추천 챗봇", page_icon="🎬")

st.title("🎬 영어 영상 추천 챗봇")
st.write("학생의 SR지수와 AR지수를 입력하면, 적절한 영어 영상 프로그램을 추천해드려요.")

sr_index = st.number_input("SR지수 (예: 3.2)", min_value=0.0, step=0.1, format="%.1f")
ar_index = st.number_input("AR지수 (예: 2.5)", min_value=0.0, step=0.1, format="%.1f")

if st.button("추천 받기"):
    with st.spinner("추천 프로그램을 분석 중입니다..."):
        result = recommend_program(sr_index, ar_index)
        st.success("추천 결과:")
        st.markdown(result)
