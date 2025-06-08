import gradio as gr
import pickle
import numpy as np

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Encode categories as integers
event_type_map = {'Competition': 0, 'Lecture': 1, 'Seminar': 2,'Workshop':3}
venue_map = {'Auditorium': 0, 'Hall': 1,'Online':2, 'Ground':3}
target_audience_map = {'General Public': 1, 'Faculty': 0, 'Students': 2}
weather_condition_map = {'Clear': 0, 'Rainy': 1, 'Stormy': 2, 'stormy':3}

# Prediction function
def predict_attendance(event_type, venue, audience, weather, social_activity):
    try:
        # Encode categorical features
        event_encoded = event_type_map.get(event_type, -1)
        venue_encoded = venue_map.get(venue, -1)
        target_audience_encoded = target_audience_map.get(audience, -1)
        weather_condition_encoded = weather_condition_map.get(weather, -1)

        # Create input array
        features = np.array([[event_encoded, venue_encoded, target_audience_encoded, weather_condition_encoded, int(social_activity)]])
        prediction = model.predict(features)
        return f"Predicted Attendance: {int(prediction[0])}"
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio UI
iface = gr.Interface(
    fn=predict_attendance,
    inputs=[
        gr.Dropdown(choices=list(event_type_map.keys()), label="Event Type"),
        gr.Dropdown(choices=list(venue_map.keys()), label="Venue"),
        gr.Dropdown(choices=list(target_audience_map.keys()), label="Target Audience"),
        gr.Dropdown(choices=list(weather_condition_map.keys()), label="Weather Condition"),
        gr.Number(label="Social Media Activity Score")
    ],
    outputs="text",
    title="Event Attendance Predictor",
    description="Predict attendance using event type, venue, audience, weather, and social engagement."
)

if __name__ == "__main__":
    iface.launch()
