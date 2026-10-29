import streamlit as st

st.set_page_config(page_title="猜字谜小游戏", page_icon="🧩")

st.title("🧩 猜字谜小游戏")
st.write("欢迎参加猜字谜挑战！")

riddles = [
    {"question": "什么东西有头无脚？", "answer": "针"},
    {"question": "什么东西越洗越脏？", "answer": "水"},
    {"question": "一口咬掉牛尾巴，猜一个字。", "answer": "告"},
    {"question": "什么门永远关不上？", "answer": "球门"},
    {"question": "什么东西晚上满天都是？", "answer": "星星"}
]

if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.feedback = None

index = st.session_state.index

if index < len(riddles):
    st.progress((index + 1) / len(riddles))
    st.write(f"第 {index + 1} 题，共 {len(riddles)} 题")
    st.subheader(riddles[index]["question"])

    answer = st.text_input("请输入你的答案", key=f"answer_{index}")

    if st.session_state.feedback is None:
        if st.button("提交答案"):
            if not answer.strip():
                st.warning("请先输入答案！")
            elif answer.strip() == riddles[index]["answer"]:
                st.session_state.score += 1
                st.session_state.feedback = "correct"
                st.rerun()
            else:
                st.session_state.feedback = "wrong"
                st.rerun()

    if st.session_state.feedback == "correct":
        st.success("回答正确！🎉")
    elif st.session_state.feedback == "wrong":
        st.info("正确答案是：" + riddles[index]["answer"])

    if st.session_state.feedback is not None:
        if st.button("下一题"):
            st.session_state.index += 1
            st.session_state.feedback = None
            st.rerun()

else:
    st.success("游戏结束！")
    st.write(f"你的得分：{st.session_state.score}/{len(riddles)}")

    if st.button("重新开始"):
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.feedback = None
        st.rerun()
