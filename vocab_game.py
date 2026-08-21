import random
import time
import streamlit as st

# กำหนดสไตล์ CSS เพิ่มขนาดตัวหนังสือและช่องกรอกข้อมูล
st.markdown(
    """
    <style>
    .big-font {
        font-size: 26px !important;
        font-weight: bold;
    }
    .question-font {
        font-size: 22px !important;
        color: #2E86C1;
    }
    input {
        font-size: 20px !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.title("⏰ เกมเติมศัพท์จับเวลา (สุ่ม 10 ข้อ)")

# คลังโจทย์ทั้งหมด (สุ่มมาใช้ 10 ข้อ)
QUESTION_BANK = [
    {"question": "An `a _ _ l e` a day keeps the doctor away. 🍎", "answer": "apple"},
    {"question": "Cats love to eat `f _ s h`. 🐟", "answer": "fish"},
    {"question": "Monkeys love to eat `b _ n _ n a`. 🍌", "answer": "banana"},
    {"question": "A `d _ g` is a man's best friend. 🐶", "answer": "dog"},
    {"question": "The sun rises in the `e _ s t`. 🌅", "answer": "east"},
    {"question": "Rabbits love to eat `c _ r r _ t`. 🥕", "answer": "carrot"},
    {"question": "Water is `h _ d r a t i n g`. 💧", "answer": "water"},
    {"question": "Birds fly in the `s k _`. ☁️", "answer": "sky"},
    {"question": "The earth is `r _ u n d`. 🌍", "answer": "round"},
    {"question": "Fire is very `h _ t`. 🔥", "answer": "hot"},
    {"question": "Ice is very `c _ l d`. 🧊", "answer": "cold"},
    {"question": "Books are for `r _ a d i n g`. 📚", "answer": "reading"},
]

TOTAL_QUESTIONS_PER_GAME = 10
TIME_PER_QUESTION = 5  # ข้อละ 5 วินาที
TOTAL_TIME = TOTAL_QUESTIONS_PER_GAME * TIME_PER_QUESTION  # รวม 50 วินาที


# 📌 ฟังก์ชันเริ่มเกมใหม่/เคลียร์ค่า
def reset_game():
    st.session_state.selected_questions = random.sample(
        QUESTION_BANK, TOTAL_QUESTIONS_PER_GAME
    )
    st.session_state.current_index = 0
    st.session_state.user_answers = []
    st.session_state.start = time.time()
    st.session_state.is_ended = False


# เริ่มต้น Session State
if "selected_questions" not in st.session_state:
    reset_game()


# 📌 ฟังก์ชัน แสดง Dialog สรุปผล
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog():
    st.balloons()
    score = 0

    st.markdown("<p class='big-font'>สรุปคะแนนของคุณ:</p>", unsafe_allow_html=True)

    for idx, q_data in enumerate(st.session_state.selected_questions):
        user_ans = (
            st.session_state.user_answers[idx]
            if idx < len(st.session_state.user_answers)
            else ""
        )
        if user_ans.strip().lower() == q_data["answer"]:
            st.success(f"✅ ข้อ {idx+1}: ถูกต้อง")
            score += 1
        else:
            st.error(
                f"❌ ข้อ {idx+1}: ไม่ถูกต้อง (เฉลย: {q_data['answer']} | คุณตอบ: '{user_ans}')"
            )

    st.info(f"🏆 ได้คะแนนรวม: {score} / {TOTAL_QUESTIONS_PER_GAME} คะแนน")

    if score == TOTAL_QUESTIONS_PER_GAME:
        st.success("🎉 Perfect! You win!")
    else:
        st.error("💀 Try Again!")


# --------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# --------------------------------------------------
st.button("🎮 เริ่มเล่นเกมใหม่", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.is_ended:
    time_left = int(TOTAL_TIME - (time.time() - st.session_state.start))

    if time_left > 0:
        st.markdown(
            f"<p class='big-font' style='color:red;'>⏳ เหลือเวลารวม: {time_left} วินาที (ข้อละ 5 วินาที)</p>",
            unsafe_allow_html=True,
        )
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 3. แสดงโจทย์ทีละข้อ
if not st.session_state.is_ended:
    curr_idx = st.session_state.current_index
    q_data = st.session_state.selected_questions[curr_idx]

    st.markdown(
        f"<p class='big-font'>ข้อที่ {curr_idx + 1} / {TOTAL_QUESTIONS_PER_GAME}</p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<p class='question-font'>{q_data['question']}</p>",
        unsafe_allow_html=True,
    )

    user_input = st.text_input(
        "ตอบคำถามที่นี่:", key=f"input_{curr_idx}", value=""
    )

    if curr_idx < TOTAL_QUESTIONS_PER_GAME - 1:
        if st.button("➡️ ข้อถัดไป"):
            st.session_state.user_answers.append(user_input)
            st.session_state.current_index += 1
            st.rerun()
    else:
        if st.button("📥 ส่งคำตอบทั้งหมด"):
            st.session_state.user_answers.append(user_input)
            st.session_state.is_ended = True
            st.rerun()

    time.sleep(1)
    st.rerun()

# 4. แสดง Dialog ผลลัพธ์เมื่อจบเกม
if st.session_state.is_ended:
    show_result_dialog()

st.divider()
st.write("นายจารุภัทร อรุณสิทธิ์ เลขที่ 9 ม.4/6")
