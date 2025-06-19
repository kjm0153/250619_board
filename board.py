import streamlit as st
import pandas as pd
import os

# CSV 파일 경로
FILENAME = "posts.csv"

# 기존 게시글 불러오기
if os.path.exists(FILENAME):
    posts_df = pd.read_csv(FILENAME)
else:
    posts_df = pd.DataFrame(columns=["이름", "내용"])

st.title("📝 CSV 기반 게시판")

# 글 작성 폼
with st.form("post_form"):
    name = st.text_input("이름")
    content = st.text_area("내용")
    submitted = st.form_submit_button("글 등록")

    if submitted:
        if name and content:
            new_post = pd.DataFrame([[name, content]], columns=["이름", "내용"])
            posts_df = pd.concat([new_post, posts_df], ignore_index=True)  # 최신 글이 위로
            posts_df.to_csv(FILENAME, index=False, encoding='utf-8-sig')  # 저장
            st.success("게시물이 등록되었습니다!")
        else:
            st.warning("이름과 내용을 모두 입력해주세요.")

# 게시글 목록 출력
st.subheader("📚 게시글 목록")

if not posts_df.empty:
    for i, row in posts_df.iterrows():
        st.markdown(f"### {row['이름']}")
        st.markdown(f"{row['내용']}")
        st.markdown("---")
else:
    st.info("아직 게시물이 없습니다.")