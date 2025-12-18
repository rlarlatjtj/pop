import streamlit as st
import time

# ==============================
# 🌐 Language Selection
# ==============================
language = st.selectbox("🌐 Language / 언어 선택", ("한국어", "English"))

def t(ko, en):
    return ko if language == "한국어" else en

# ==============================
# 🎨 Page Setup
# ==============================
st.set_page_config(
    page_title=t("🤖 AI 식단 분석기", "🤖 AI Diet Analyzer"),
    layout="centered"
)

st.markdown(
    f"""
    <h1 style='text-align: center;'>🤖 {t("AI 기반 맞춤형 식단 분석기", "AI-Based Personalized Diet Analyzer")}</h1>
    <p style='text-align: center; font-size: 18px;'>
    {t(
        "인공지능처럼 분석하여 건강한 식단 선택을 도와줍니다.",
        "Simulates AI analysis to support healthy dietary decisions."
    )}
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ==============================
# 👤 User Info
# ==============================
st.header("👤 " + t("사용자 정보", "User Information"))

age = st.selectbox(t("나이를 선택하세요", "Select your age"), list(range(10, 31)))
is_teen = age < 20

# ==============================
# 🧒 Teen Eating Habits
# ==============================
if is_teen:
    st.subheader("🧒 " + t("청소년 식습관 체크", "Teen Eating Habits"))
    meals = st.selectbox(t("하루 식사 횟수", "Meals per day"), (1, 2, 3, 4))
    breakfast = st.radio(t("아침 식사 여부", "Do you eat breakfast?"),
                          ("Rarely", "Sometimes", "Almost every day"))
    late_meal = st.radio(t("야식 빈도", "Late-night meals"),
                         ("Often", "Sometimes", "Rarely"))

st.divider()

# ==============================
# 🥗 Diet Type
# ==============================
st.header("🥗 " + t("식단 유형", "Diet Type"))
vegan = st.radio(t("비건 식단인가요?", "Do you follow a vegan diet?"), ("Yes", "No"))

# ==============================
# 🩺 Health Condition
# ==============================
st.header("🩺 " + t("건강 상태", "Health Condition"))
disease = st.selectbox(
    t("질병 선택", "Select health condition"),
    ("None", "Diabetes", "Obesity", "Dyslipidemia")
)

# ==============================
# 💊 Medication
# ==============================
st.header("💊 " + t("복용 중인 약", "Medication"))
medicine = st.selectbox(
    t("현재 복용 중인 약", "Current medication"),
    ("None", "Painkiller", "Antibiotic", "Diabetes medication", "Iron supplement")
)

# ==============================
# 🍽 Food Selection
# ==============================
st.header("🍽 " + t("음식 선택", "Food Selection"))
food = st.selectbox(
    t("먹고 싶은 음식", "Food you want to eat"),
    ("Salad", "Instant noodles", "Cheesecake", "Brown rice", "Milk")
)

st.divider()

# ==============================
# 🤖 AI Analysis Button
# ==============================
if st.button("🤖 " + t("AI 분석 시작", "Start AI Analysis")):
    with st.spinner(
        t("🤖 인공지능이 데이터를 분석 중입니다...", "🤖 AI is analyzing your data...")
    ):
        time.sleep(2.5)

    st.success(t("✅ 분석 완료!", "✅ Analysis complete!"))

    # ==========================
    # ⚠️ Evaluation
    # ==========================
    st.subheader("📊 " + t("AI 판단 결과", "AI Evaluation Result"))

    if vegan == "Yes" and food in ["Cheesecake", "Milk"]:
        st.error(t("비건 식단에 적합하지 않습니다.", "Not suitable for a vegan diet."))

    if disease == "Diabetes" and food in ["Cheesecake", "Instant noodles"]:
        st.warning(t("혈당 상승 위험이 있습니다.", "May rapidly increase blood glucose."))

    # ==========================
    # 💊 Medication–Food Check
    # ==========================
    st.subheader("💊 " + t("약–음식 상호작용", "Medication–Food Interaction"))

    if medicine == "Antibiotic" and food == "Milk":
        st.warning(t("우유는 항생제 흡수를 방해할 수 있습니다.",
                     "Milk may reduce antibiotic absorption."))
    elif medicine == "Iron supplement" and food == "Milk":
        st.warning(t("칼슘은 철분 흡수를 방해할 수 있습니다.",
                     "Calcium may interfere with iron absorption."))
    else:
        st.info(t("큰 상호작용은 알려져 있지 않습니다.",
                  "No major interaction is generally reported."))

    # ==========================
    # 🍽 AI Meal Plan
    # ==========================
    st.subheader("🍽 " + t("AI 추천 식단", "AI Recommended Meal Plan"))

    if vegan == "Yes":
        st.markdown("🌱 **Breakfast:** Oatmeal with fruits and nuts")
        st.markdown("🌱 **Lunch:** Brown rice with tofu and vegetables")
        st.markdown("🌱 **Dinner:** Vegetable soup with legumes")
    else:
        st.markdown("🥚 **Breakfast:** Eggs with whole-grain toast")
        st.markdown("🍗 **Lunch:** Grilled chicken with vegetables")
        st.markdown("🐟 **Dinner:** Fish with brown rice and salad")

    if is_teen:
        st.info(
            t(
                "🧠 AI는 청소년의 성장과 규칙적인 식습관을 우선 고려했습니다.",
                "🧠 AI prioritized growth and regular eating habits for adolescents."
            )
        )

    st.balloons()
