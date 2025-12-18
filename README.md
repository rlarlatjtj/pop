# pop
This program is a personalized diet evaluation system that supports healthy decisions based on age, diet type, health conditions, and eating habits. Users select their age first, and adolescents automatically receive eating habit correction. The program analyzes meal frequency and breakfast habits, then provides feedback to encourage improvement.
import streamlit as st

# ==============================
# 기본 설정
# ==============================
st.set_page_config(page_title="Personalized Diet Program", layout="centered")

st.title("Personalized Diet Evaluation Program")
st.write(
    "This program evaluates food suitability based on age, dietary type, "
    "health conditions, medications, and eating habits, and provides "
    "a personalized example meal plan."
)

# ==============================
# 1. 나이 선택
# ==============================
st.header("1. User Information")
age = st.selectbox("Select your age", list(range(10, 31)))
is_teen = age < 20

# ==============================
# 2. 청소년 식습관 교정
# ==============================
if is_teen:
    st.header("2. Eating Habits (Adolescents Only)")
    meals_per_day = st.selectbox("Meals per day", (1, 2, 3, 4))
    breakfast = st.radio("Do you eat breakfast?", ("Rarely", "Sometimes", "Almost every day"))
    late_meal = st.radio("Do you eat late-night meals?", ("Often", "Sometimes", "Rarely"))

# ==============================
# 3. 비건 여부
# ==============================
st.header("3. Dietary Type")
vegan = st.radio("Do you follow a vegan diet?", ("Yes", "No"))

# ==============================
# 4. 질병 선택
# ==============================
st.header("4. Health Condition")
disease = st.selectbox(
    "Select any health condition",
    ("None", "Diabetes", "Obesity", "Dyslipidemia")
)

# ==============================
# 5. 복용 중인 약
# ==============================
st.header("5. Medication")
medicine = st.selectbox(
    "Select medication you are currently taking",
    ("None", "Painkiller", "Antibiotic", "Diabetes medication", "Iron supplement")
)

# ==============================
# 6. 음식 선택
# ==============================
st.header("6. Food Selection")
food = st.selectbox(
    "Select a food",
    ("Salad", "Instant noodles", "Cheesecake", "Brown rice", "Milk")
)

# ==============================
# 7. 평가 실행
# ==============================
if st.button("Evaluate Diet"):
    st.subheader("📊 Evaluation Result")

    # --- 비건 판정 ---
    if vegan == "Yes" and food in ["Cheesecake", "Milk"]:
        st.error("This food is not suitable for a vegan diet.")

    # --- 질병 관련 판정 ---
    if disease == "Diabetes" and food in ["Cheesecake", "Instant noodles"]:
        st.warning("This food may cause a rapid increase in blood glucose.")
    if disease == "Obesity" and food == "Cheesecake":
        st.warning("This food is high in calories and may not be suitable for weight control.")

    # ==========================
    # 약–음식 상호작용
    # ==========================
    st.subheader("💊 Medication–Food Interaction Check")

    if medicine == "Antibiotic" and food == "Milk":
        st.warning("Dairy products may reduce the absorption of some antibiotics.")
    elif medicine == "Iron supplement" and food == "Milk":
        st.warning("Calcium-rich foods may interfere with iron absorption.")
    elif medicine == "Diabetes medication" and food == "Cheesecake":
        st.warning("High-sugar foods may reduce blood glucose control.")
    else:
        st.success("No major food–medication interaction is generally reported.")

    # ==========================
    # 청소년 식습관 피드백
    # ==========================
    if is_teen:
        st.subheader("Eating Habit Feedback")
        if meals_per_day <= 2:
            st.info("Eating too few meals may cause energy imbalance.")
        if breakfast == "Rarely":
            st.info("Skipping breakfast may affect concentration and learning.")
        if late_meal == "Often":
            st.info("Frequent late-night meals may negatively affect metabolism.")

    # ==========================
    # 8. 맞춤 추천 식단
    # ==========================
    st.subheader("🍽 Recommended Daily Meal Plan")

    meal_plan = {"Breakfast": "", "Lunch": "", "Dinner": ""}

    # 기본 식단 (비건/일반)
    if vegan == "Yes":
        meal_plan["Breakfast"] = "Oatmeal with fruits and nuts"
        meal_plan["Lunch"] = "Brown rice with tofu and vegetables"
        meal_plan["Dinner"] = "Vegetable soup with legumes"
    else:
        meal_plan["Breakfast"] = "Eggs with whole-grain toast"
        meal_plan["Lunch"] = "Grilled chicken with vegetables"
        meal_plan["Dinner"] = "Fish with brown rice and salad"

    # 질병 반영
    if disease == "Diabetes":
        meal_plan["Breakfast"] = "Low-sugar oatmeal with nuts"
        meal_plan["Lunch"] = "Brown rice with vegetables and lean protein"
        meal_plan["Dinner"] = "Grilled fish with non-starchy vegetables"

    if disease == "Obesity":
        meal_plan["Breakfast"] = "High-protein, low-calorie breakfast"
        meal_plan["Lunch"] = "Lean protein with salad"
        meal_plan["Dinner"] = "Light vegetable-based meal"

    # 청소년 설명
    if is_teen:
        st.write(
            "This meal plan emphasizes regular meals and balanced nutrition "
            "to support growth during adolescence."
        )

    for meal, menu in meal_plan.items():
        st.write(f"**{meal}:** {menu}")
