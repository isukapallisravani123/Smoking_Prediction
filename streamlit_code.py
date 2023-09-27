import pickle
import streamlit as st

# Load the trained model
with open('random_forest_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

feature_names = ['age', 'height(cm)', 'weight(kg)', 'waist(cm)', 'systolic',
                 'relaxation', 'fasting blood sugar', 'Cholesterol', 'triglyceride',
                 'HDL', 'LDL', 'hemoglobin', 'serum creatinine', 'AST', 'ALT', 'Gtp',
                 'dental caries']

def predict_smoking(features, feature_names, loaded_model):
    """Predict smoking based on input features."""
    
    # Prepare input data for prediction
    try:
        input_data = [float(features[feature_name]) for feature_name in feature_names]
    
        # Make prediction
        prediction = loaded_model.predict([input_data])
    
        return "Yes" if prediction[0] == 1 else "No"
    except ValueError:
        return "Invalid input. Please enter valid numeric values for all features."


def main():
    st.title("Smoking Prediction")

    # Create a dictionary to store user inputs for features
    user_inputs = {}

    # Add user input elements for various features
    for feature_name in feature_names:
        user_input = st.text_input(f"{feature_name.capitalize()}", "")  # Initialize with empty string
        user_inputs[feature_name] = user_input

    # Make a prediction when the user clicks the "Predict" button
    if st.button("Predict"):
        result = predict_smoking(user_inputs, feature_names, loaded_model)
        st.success(f"Prediction: {result}")

if __name__ == '__main__':
    main()
