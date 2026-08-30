# ============================================================
# STUDENT STRESS DETECTOR - Streamlit Web App (BONUS UI)
# Run with: streamlit run app_streamlit.py
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import warnings
warnings.filterwarnings('ignore')

# --- Train Model (same as main script) ---
@st.cache_resource
def train_model():
    np.random.seed(42)
    n = 300
    data = {
        'sleep_hours':         np.random.uniform(3, 9, n),
        'study_hours_per_day': np.random.uniform(1, 12, n),
        'assignments_pending': np.random.randint(0, 10, n),
        'screen_time_hours':   np.random.uniform(1, 10, n),
        'social_activity':     np.random.randint(1, 6, n),
        'attendance_percent':  np.random.uniform(40, 100, n),
        'exercise_days_week':  np.random.randint(0, 7, n),
    }
    df = pd.DataFrame(data)

    def assign_stress(row):
        score = 0
        if row['sleep_hours'] < 5: score += 3
        elif row['sleep_hours'] < 6: score += 1
        if row['assignments_pending'] > 6: score += 3
        elif row['assignments_pending'] > 3: score += 1
        if row['study_hours_per_day'] > 9: score += 2
        if row['screen_time_hours'] > 7: score += 2
        if row['social_activity'] < 2: score += 1
        if row['attendance_percent'] < 60: score += 2
        if row['exercise_days_week'] == 0: score += 1
        if score >= 7: return 'High'
        elif score >= 4: return 'Medium'
        else: return 'Low'

    df['stress_level'] = df.apply(assign_stress, axis=1)
    X = df.drop('stress_level', axis=1)
    y = df['stress_level']
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

# --- UI ---
st.set_page_config(page_title="Student Stress Detector", page_icon="🧠")
st.title("🧠 Student Stress Level Detector")
st.markdown("Fill in your daily habits and find out your stress level!")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    sleep = st.slider("😴 Sleep Hours per Day", 3.0, 10.0, 6.0, 0.5)
    study = st.slider("📚 Study Hours per Day", 0.0, 12.0, 5.0, 0.5)
    assignments = st.slider("📝 Pending Assignments", 0, 10, 3)

with col2:
    screen = st.slider("📱 Screen Time (hrs/day)", 1.0, 12.0, 4.0, 0.5)
    social = st.slider("🤝 Social Activity (1=Low, 5=High)", 1, 5, 3)
    attendance = st.slider("🏫 Attendance %", 40, 100, 75)
    exercise = st.slider("🏃 Exercise Days per Week", 0, 7, 2)

if st.button("🔮 Predict My Stress Level", use_container_width=True):
    model = train_model()
    input_data = pd.DataFrame([{
        'sleep_hours': sleep,
        'study_hours_per_day': study,
        'assignments_pending': assignments,
        'screen_time_hours': screen,
        'social_activity': social,
        'attendance_percent': attendance,
        'exercise_days_week': exercise
    }])

    prediction = model.predict(input_data)[0]
    probs = model.predict_proba(input_data)[0]
    classes = model.classes_

    st.markdown("---")
    if prediction == 'High':
        st.error(f"## 🔴 Stress Level: HIGH")
        st.warning("Take breaks, sleep more, and talk to someone you trust!")
    elif prediction == 'Medium':
        st.warning(f"## 🟡 Stress Level: MEDIUM")
        st.info("You're managing okay, but try to exercise and sleep better.")
    else:
        st.success(f"## 🟢 Stress Level: LOW")
        st.info("Great job maintaining a healthy balance!")

    st.markdown("### Confidence:")
    for cls, prob in zip(classes, probs):
        st.progress(float(prob), text=f"{cls}: {prob*100:.1f}%")
