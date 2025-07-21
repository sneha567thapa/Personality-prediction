# test.py
import streamlit as st
import pandas as pd
import joblib

# Load your trained model
try:
    model = joblib.load('D:\Project_3\model_presonality.pt')  # Update with your actual model file
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(f"Error loading model: {e}")

# Function to process input and make prediction
def predict_personality(input_data):
    try:
        # Convert input to DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Ensure columns match training data (adjust as needed)
        expected_columns = [
            'social_energy', 'alone_time_preference', 'talkativeness', 
            'deep_reflection', 'group_comfort', 'party_liking', 
            'listening_skill', 'empathy', 'creativity', 'organization',
            'leadership', 'risk_taking', 'public_speaking_comfort', 
            'curiosity', 'routine_preference', 'excitement_seeking',
            'friendliness', 'emotional_stability', 'planning', 
            'spontaneity', 'adventurousness', 'reading_habit',
            'sports_interest', 'online_social_usage', 'travel_desire',
            'gadget_usage', 'work_style_collaborative', 'decision_speed',
            'stress_handling'
        ]
        
        # Reorder columns to match training data
        input_df = input_df[expected_columns]
        
        # Make prediction
        prediction = model.predict(input_df)
        return prediction[0]
    except Exception as e:
        st.error(f"Prediction error: {e}")
        return None

# Streamlit UI
st.title("Personality Type Classifier")
st.write("Rate each trait on a scale from 0 to 10")

# Create input sliders for all features
with st.form("personality_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        social_energy = st.slider("Social Energy", 0.0, 10.0, 5.0)
        alone_time_preference = st.slider("Alone Time Preference", 0.0, 10.0, 5.0)
        talkativeness = st.slider("Talkativeness", 0.0, 10.0, 5.0)
        deep_reflection = st.slider("Deep Reflection", 0.0, 10.0, 5.0)
        group_comfort = st.slider("Group Comfort", 0.0, 10.0, 5.0)
        party_liking = st.slider("Party Liking", 0.0, 10.0, 5.0)
        listening_skill = st.slider("Listening Skill", 0.0, 10.0, 5.0)
        empathy = st.slider("Empathy", 0.0, 10.0, 5.0)
        creativity = st.slider("Creativity", 0.0, 10.0, 5.0)
        organization = st.slider("Organization", 0.0, 10.0, 5.0)
        leadership = st.slider("Leadership", 0.0, 10.0, 5.0)
        risk_taking = st.slider("Risk Taking", 0.0, 10.0, 5.0)
        public_speaking_comfort = st.slider("Public Speaking Comfort", 0.0, 10.0, 5.0)
        curiosity = st.slider("Curiosity", 0.0, 10.0, 5.0)
        routine_preference = st.slider("Routine Preference", 0.0, 10.0, 5.0)
    
    with col2:
        excitement_seeking = st.slider("Excitement Seeking", 0.0, 10.0, 5.0)
        friendliness = st.slider("Friendliness", 0.0, 10.0, 5.0)
        emotional_stability = st.slider("Emotional Stability", 0.0, 10.0, 5.0)
        planning = st.slider("Planning", 0.0, 10.0, 5.0)
        spontaneity = st.slider("Spontaneity", 0.0, 10.0, 5.0)
        adventurousness = st.slider("Adventurousness", 0.0, 10.0, 5.0)
        reading_habit = st.slider("Reading Habit", 0.0, 10.0, 5.0)
        sports_interest = st.slider("Sports Interest", 0.0, 10.0, 5.0)
        online_social_usage = st.slider("Online Social Usage", 0.0, 10.0, 5.0)
        travel_desire = st.slider("Travel Desire", 0.0, 10.0, 5.0)
        gadget_usage = st.slider("Gadget Usage", 0.0, 10.0, 5.0)
        work_style_collaborative = st.slider("Work Style Collaborative", 0.0, 10.0, 5.0)
        decision_speed = st.slider("Decision Speed", 0.0, 10.0, 5.0)
        stress_handling = st.slider("Stress Handling", 0.0, 10.0, 5.0)
    
    submitted = st.form_submit_button("Predict Personality Type")

if submitted:
    # Prepare input data dictionary
    input_data = {
        'social_energy': social_energy,
        'alone_time_preference': alone_time_preference,
        'talkativeness': talkativeness,
        'deep_reflection': deep_reflection,
        'group_comfort': group_comfort,
        'party_liking': party_liking,
        'listening_skill': listening_skill,
        'empathy': empathy,
        'creativity': creativity,
        'organization': organization,
        'leadership': leadership,
        'risk_taking': risk_taking,
        'public_speaking_comfort': public_speaking_comfort,
        'curiosity': curiosity,
        'routine_preference': routine_preference,
        'excitement_seeking': excitement_seeking,
        'friendliness': friendliness,
        'emotional_stability': emotional_stability,
        'planning': planning,
        'spontaneity': spontaneity,
        'adventurousness': adventurousness,
        'reading_habit': reading_habit,
        'sports_interest': sports_interest,
        'online_social_usage': online_social_usage,
        'travel_desire': travel_desire,
        'gadget_usage': gadget_usage,
        'work_style_collaborative': work_style_collaborative,
        'decision_speed': decision_speed,
        'stress_handling': stress_handling
    }
    
    # Make prediction
    prediction = predict_personality(input_data)
    
    if prediction is not None:
        st.success(f"Predicted Personality Type: {prediction}")
        
        # Optional: Add some interpretation
        if prediction == "Extrovert":
            st.write("You're likely outgoing and energized by social interactions!")
        elif prediction == "Introvert":
            st.write("You probably prefer quiet environments and need alone time to recharge.")
        elif prediction == "Ambivert":
            st.write("You're a balance of both extrovert and introvert traits!")