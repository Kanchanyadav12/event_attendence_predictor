
# 🎯 Event Attendance Predictor

A machine learning-based application that predicts the **expected attendance** for an event based on event details and social media engagement. The model is deployed as an interactive Gradio app on Hugging Face Spaces.

> 🚀 **Live App:** [Try it on Hugging Face](https://huggingface.co/spaces/kanchanyadav/event_attendence_predictor)

---

## 📌 Objective

This tool is designed to assist event organizers in forecasting how many people might attend an event based on multiple factors like type of event, venue, audience, weather conditions, and social media activity.

---

## 🧠 Features Used for Prediction

| Feature                | Type         | Example Values                             |
|------------------------|--------------|--------------------------------------------|
| `Event_Type`           | Categorical  | Competition, Lecture, Seminar, Workshop    |
| `Venue`                | Categorical  | Auditorium, Hall, Online, Ground           |
| `Target_Audience`      | Categorical  | Faculty, General Public, Students          |
| `Weather_Condition`    | Categorical  | Clear, Rainy, Stormy                       |
| `Social_Media_Activity`| Numerical    | e.g. 2384, 1456                             |

These features are internally encoded before being passed to the trained model.

---

## 🧠 Model Info

- **Model Used**: `RandomForestRegressor`
- **Framework**: `scikit-learn`
- **Encoding**: All categorical values are label-encoded
- **Input Shape**: 5 features
- **Output**: A single integer prediction for attendance

---

## 🖥️ Gradio Interface

Inputs:
- Event Type (Dropdown)
- Venue (Dropdown)
- Target Audience (Dropdown)
- Weather Condition (Dropdown)
- Social Media Activity Score (Number)

Outputs:
- Predicted number of attendees

---

## 📂 Files in This Repository

| File Name           | Description                                      |
|---------------------|--------------------------------------------------|
| `app.py`            | Gradio app with encoded input mapping            |
| `model.pkl`         | Pre-trained machine learning model               |
| `requirements.txt`  | Python dependencies                              |
| `event_attendence_model.ipynb` | Notebook used for training & evaluation  |
| `README.md`         | This file                                        |

---

## 🛠️ Running Locally

```bash
# Clone the repo
git clone https://github.com/yourusername/event_attendance_predictor.git
cd event_attendance_predictor

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
