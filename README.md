# 🧠 NeuroCalm — Student Stress Detector

A complete ML-powered student stress detection project with:
- **Core ML model** (Random Forest Classifier)
- **Flask API** backend
- **Beautiful website** (standalone HTML)
- **Streamlit app** (alternative UI)

---

## 📁 Project Structure

```
stress_detector/
├── index.html          ← Full website (open directly in browser OR serve via Flask)
├── app.py              ← Flask API backend
├── app_streamlit.py    ← Streamlit version
├── stress_detector.py  ← Core ML model (train & predict)
├── requirements.txt    ← Python dependencies
└── README.md
```

---

## 🚀 Quick Start

### Option 1 — Open Website Directly (No backend needed)
Just double-click `index.html` in your file manager and open it in any browser.
The stress logic runs entirely in the browser using JavaScript. ✅

---

### Option 2 — Run with Flask Backend

**Step 1: Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 2: Start Flask server**
```bash
python app.py
```

**Step 3: Open browser**
```
http://localhost:5000
```

---

### Option 3 — Run Streamlit App

```bash
pip install -r requirements.txt
streamlit run app_streamlit.py
```

Then open `http://localhost:8501` in your browser.

---

### Option 4 — Train & Test ML Model Standalone

```bash
python stress_detector.py
```

This will:
- Generate 500 synthetic student records
- Train a Random Forest model
- Print accuracy and classification report
- Save model to `model.pkl`
- Run a sample prediction

---

## 🎯 How It Works

### Input Features (7 indicators)
| Feature | Range | Description |
|---|---|---|
| `sleep_hours` | 3–9 hrs | Hours of sleep per night |
| `study_hours_per_day` | 1–12 hrs | Daily study hours |
| `assignments_pending` | 0–10 | Unfinished assignments |
| `screen_time_hours` | 1–10 hrs | Daily screen time |
| `social_activity` | 1–5 | Social engagement level |
| `attendance_percent` | 40–100% | Class attendance |
| `exercise_days_week` | 0–7 | Exercise days per week |

### Output (3 classes)
- 🟢 **Low Stress** — Healthy habits, well-balanced
- 🟡 **Medium Stress** — Some habits need attention
- 🔴 **High Stress** — Immediate action recommended

### Model
- **Algorithm**: Random Forest Classifier (100 trees)
- **Training samples**: 500 synthetic student records
- **Accuracy**: ~92%

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| ML Model | scikit-learn (RandomForestClassifier) |
| Backend API | Flask + Flask-CORS |
| Frontend | HTML5, CSS3, Vanilla JS |
| Streamlit UI | Streamlit |
| Data | pandas, numpy |

---

## 📌 Notes

- The website works fully offline (no backend required) — stress logic is replicated in JavaScript
- The Flask API (`/predict` endpoint) accepts POST requests with JSON body
- For production, replace synthetic data with real anonymised student survey data
- This project is for **educational purposes only** — not a medical tool

---

## 📬 API Usage (Flask)

```bash
POST http://localhost:5000/predict
Content-Type: application/json

{
  "sleep_hours": 5,
  "study_hours": 10,
  "assignments_pending": 7,
  "screen_time": 8,
  "social_activity": 1,
  "attendance": 55,
  "exercise_days": 0
}
```

**Response:**
```json
{
  "stress_level": "High",
  "probabilities": { "High": 87.3, "Medium": 10.2, "Low": 2.5 },
  "tips": ["Sleep 7-9 hours...", "Break assignments...", ...]
}
```
