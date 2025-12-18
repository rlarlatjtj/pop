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
    <p style='text-align: center; font-size: 17px;'>
    {t(
        "연령, 질병, 약물, 식습관을 종합해 인공지능처럼 분석합니다.",
        "Simulates AI reasoning using age, health, medication, and eating habits."
    )}
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ==============================
# 👤 User Information
# ==============================
st.header("👤 " + t("사용자 정보", "User Information"))

age = st.selectbox(t("나이를 선택하세요", "Select your age"), list(range(8, 91)))

if age <= 12:
    age_group = "child"
elif age <= 19:
    age_group = "teen"
elif age <= 64:
    age_group = "adult"
else:
    age_group = "senior"

is_teen = age_group == "teen"

# ==============================
# 🧒 Teen Eating Habits
# ==============================
if is_teen:
    st.subheader("🧒 " + t("청소년 식습관 체크", "Teen Eating Habits"))
    meals = st.selectbox(t("하루 식사 횟수", "Meals per day"), (1, 2, 3, 4))
    breakfast = st.radio(t("아침 식사 여부", "Breakfast habit"), ("Rarely", "Sometimes", "Almost every day"))
    late_meal = st.radio(t("야식 빈도", "Late-night meals"), ("Often", "Sometimes", "Rarely"))

st.divider()

# ==============================
# 🥗 Diet Type
# ==============================
st.header("🥗 " + t("식단 유형", "Diet Type"))
vegan = st.radio(t("비건 식단인가요?", "Vegan diet?"), ("Yes", "No"))

# ==============================
# 🩺 Health Condition
# ==============================
st.header("🩺 " + t("건강 상태", "Health Condition"))
disease = st.selectbox(
    t("질병 선택", "Health condition"),
    ("None", "Diabetes", "Obesity", "Dyslipidemia")
)

# ==============================
# 💊 Medication
# ==============================
st.header("💊 " + t("복용 중인 약", "Medication"))
medicine = st.selectbox(
    t("현재 복용 중인 약", "Medication"),
    ("None", "Antibiotic", "Iron supplement", "Diabetes medication")
)

# ==============================
# 🍽 Food
# ==============================
st.header("🍽 " + t("음식 선택", "Food Selection"))
food = st.selectbox(
    t("먹고 싶은 음식", "Selected food"),
    ("Salad", "Instant noodles", "Cheesecake", "Brown rice", "Milk")
)

st.divider()

# ==============================
# 🤖 AI Analysis
# ==============================
if st.button("🤖 " + t("AI 분석 시작", "Start AI Analysis")):
    with st.spinner(t("🤖 인공지능이 분석 중입니다...", "🤖 AI is analyzing...")):
        time.sleep(2.5)

    st.success(t("✅ 분석 완료!", "✅ Analysis complete!"))

    # ==========================
    # 🎂 Age Insight
    # ==========================
    st.subheader("🎂 " + t("연령대별 AI 분석", "Age-Based Insight"))

    age_msg = {
        "child": t("👶 성장기에는 에너지와 칼슘 섭취가 중요합니다.", "👶 Growth requires sufficient energy and calcium."),
        "teen": t("🧒 결식과 편식은 성장에 부정적 영향을 줍니다.", "🧒 Skipping meals negatively affects growth."),
        "adult": t("🧑 질병 예방을 위한 균형 잡힌 식단이 중요합니다.", "🧑 Balanced diets help prevent disease."),
        "senior": t("👴 소화가 쉽고 단백질이 충분한 식단이 필요합니다.", "👴 Easy digestion and protein intake are important.")
    }
    st.info(age_msg[age_group])

    # ==========================
    # 💊 Medication–Food Check
    # ==========================
    st.subheader("💊 " + t("약–음식 상호작용", "Medication–Food Interaction"))

    if medicine == "Antibiotic" and food == "Milk":
        st.warning(t("우유는 항생제 흡수를 방해할 수 있습니다.", "Milk may reduce antibiotic absorption."))
    elif medicine == "Iron supplement" and food == "Milk":
        st.warning(t("칼슘은 철분 흡수를 저해합니다.", "Calcium interferes with iron absorption."))
    else:
        st.info(t("유의미한 상호작용은 없습니다.", "No significant interaction detected."))

    # ==========================
    # 🍽 Age-Based Meal Plan
    # ==========================
    st.subheader("🍽 " + t("연령대별 AI 추천 식단", "Age-Based AI Meal Plan"))

    if age_group == "child":
        st.markdown("🥣 **Breakfast:** Milk + whole-grain cereal")
        st.markdown("🍱 **Lunch:** Rice, eggs, vegetables")
        st.markdown("🍲 **Dinner:** Soup, tofu, fruits")

    elif age_group == "teen":
        st.markdown("🍞 **Breakfast:** Eggs, toast, fruit")
        st.markdown("🍛 **Lunch:** Brown rice, chicken/tofu, vegetables")
        st.markdown("🍲 **Dinner:** Fish or legumes with salad")

    elif age_group == "adult":
        st.markdown("🥗 **Breakfast:** Oatmeal with nuts")
        st.markdown("🍗 **Lunch:** Lean protein + vegetables")
        st.markdown("🥣 **Dinner:** Light soup and whole grains")

    else:
        st.markdown("🍵 **Breakfast:** Soft porridge")
        st.markdown("🐟 **Lunch:** Steamed fish, vegetables")
        st.markdown("🥣 **Dinner:** Tofu soup, soft rice")

    # ==========================
    # 🧠 AI Reasoning Card
    # ==========================
    st.subheader("🧠 " + t("AI 판단 근거", "AI Reasoning Explanation"))

    st.markdown(
        t(
            """
            **AI는 다음 기준을 종합하여 판단했습니다:**
            - 연령에 따른 생리적 영양 요구
            - 질병과 대사성 위험 요인
            - 약물–음식 상호작용 가능성
            - 비건 여부 및 식습관
            - 청소년의 경우 성장과 규칙성 우선
            """,
            """
            **The AI decision is based on:**
            - Age-specific nutritional needs
            - Disease and metabolic risk
            - Medication–food interactions
            - Vegan preference and eating habits
            - Growth and regularity for adolescents
            """
        )
    )

    st.balloons()
