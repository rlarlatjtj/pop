import streamlit as st

# ==============================
# 언어 선택
# ==============================
language = st.selectbox("Language / 언어 선택", ("한국어", "English"))

# ==============================
# 언어별 텍스트 사전
# ==============================
TEXT = {
    "title": {
        "한국어": "맞춤형 식단 평가 프로그램",
        "English": "Personalized Diet Evaluation Program"
    },
    "intro": {
        "한국어": "이 프로그램은 나이, 식습관, 식단 유형, 질병, 복용 중인 약을 고려하여 음식 적합성을 평가하고 예시 식단을 제안합니다.",
        "English": "This program evaluates food suitability based on age, eating habits, dietary type, health conditions, and medications, and suggests an example meal plan."
    },
    "age": {"한국어": "나이 선택", "English": "Select your age"},
    "teen": {"한국어": "청소년 식습관", "English": "Eating Habits (Adolescents Only)"},
    "vegan": {"한국어": "비건 여부", "English": "Do you follow a vegan diet?"},
    "disease": {"한국어": "질병 선택", "English": "Health Condition"},
    "medicine": {"한국어": "복용 중인 약", "English": "Medication"},
    "food": {"한국어": "음식 선택", "English": "Food Selection"},
    "evaluate": {"한국어": "식단 평가하기", "English": "Evaluate Diet"},
    "mealplan": {"한국어": "추천 식단", "English": "Recommended Meal Plan"}
}

# ==============================
# 기본 설정
# ==============================
st.set_page_config(page_title=TEXT["title"][language], layout="centered")

st.title(TEXT["title"][language])
st.write(TEXT["intro"][language])

# ==============================
# 1. 나이
# ==============================
st.header("1. " + TEXT["age"][language])
age = st.selectbox(TEXT["age"][language], list(range(10, 31)))
is_teen = age < 20

# ==============================
# 2. 청소년 식습관
# ==============================
if is_teen:
    st.header("2. " + TEXT["teen"][language])
    meals_per_day = st.selectbox(
        "하루 식사 횟수 / Meals per day", (1, 2, 3, 4)
    )
    breakfast = st.radio(
        "아침 식사 여부 / Breakfast",
        ("Rarely", "Sometimes", "Almost every day")
    )
    late_meal = st.radio(
        "야식 빈도 / Late-night meals",
        ("Often", "Sometimes", "Rarely")
    )

# ==============================
# 3. 비건
# ==============================
st.header("3. " + TEXT["vegan"][language])
vegan = st.radio(TEXT["vegan"][language], ("Yes", "No"))

# ==============================
# 4. 질병
# ==============================
st.header("4. " + TEXT["disease"][language])
disease = st.selectbox(
    TEXT["disease"][language],
    ("None", "Diabetes", "Obesity", "Dyslipidemia")
)

# ==============================
# 5. 약
# ==============================
st.header("5. " + TEXT["medicine"][language])
medicine = st.selectbox(
    TEXT["medicine"][language],
    ("None", "Painkiller", "Antibiotic", "Diabetes medication", "Iron supplement")
)

# ==============================
# 6. 음식
# ==============================
st.header("6. " + TEXT["food"][language])
food = st.selectbox(
    TEXT["food"][language],
    ("Salad", "Instant noodles", "Cheesecake", "Brown rice", "Milk")
)

# ==============================
# 7. 평가
# ==============================
if st.button(TEXT["evaluate"][language]):
    st.subheader("📊 Result")

    # 비건
    if vegan == "Yes" and food in ["Cheesecake", "Milk"]:
        st.error(
            "비건 식단에 적합하지 않습니다."
            if language == "한국어"
            else "This food is not suitable for a vegan diet."
        )

    # 질병
    if disease == "Diabetes" and food in ["Cheesecake", "Instant noodles"]:
        st.warning(
            "혈당을 급격히 상승시킬 수 있습니다."
            if language == "한국어"
            else "This food may raise blood glucose levels."
        )

    # ==========================
    # 약–음식 상호작용
    # ==========================
    st.subheader("💊 Medication–Food Check")

    if medicine == "Antibiotic" and food == "Milk":
        st.warning(
            "우유는 일부 항생제 흡수를 방해할 수 있습니다."
            if language == "한국어"
            else "Dairy products may reduce antibiotic absorption."
        )
    elif medicine == "Iron supplement" and food == "Milk":
        st.warning(
            "칼슘은 철분 흡수를 방해할 수 있습니다."
            if language == "한국어"
            else "Calcium-rich foods may interfere with iron absorption."
        )
    else:
        st.success(
            "일반적으로 알려진 큰 상호작용은 없습니다."
            if language == "한국어"
            else "No major food–medication interaction is generally reported."
        )

    # ==========================
    # 추천 식단
    # ==========================
    st.subheader("🍽 " + TEXT["mealplan"][language])

    if vegan == "Yes":
        st.write("- Breakfast: Oatmeal with fruits and nuts")
        st.write("- Lunch: Brown rice with tofu and vegetables")
        st.write("- Dinner: Vegetable soup with legumes")
    else:
        st.write("- Breakfast: Eggs with whole-grain toast")
        st.write("- Lunch: Grilled chicken with vegetables")
        st.write("- Dinner: Fish with brown rice and salad")

    if is_teen:
        st.info(
            "청소년의 성장과 규칙적인 식습관 형성을 고려한 식단입니다."
            if language == "한국어"
            else "This meal plan supports growth and regular eating habits during adolescence."
        )
