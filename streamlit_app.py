import streamlit as st
import pickle
import pandas as pd

# Load the saved Linear Regression model
with open('regression_model.pkl', 'rb') as file:
    model = pickle.load(file)


def main():
    st.sidebar.title("Navigation")
    pages = ["Home", "Predict Energy Consumption", "About"]
    selected_page = st.sidebar.selectbox("Go to", pages)

    if selected_page == "Home":
        show_home_page()
    elif selected_page == "Predict Energy Consumption":
        show_prediction_page()
    elif selected_page == "About":
        show_about_page()


def show_home_page():
    st.title("Energy Consumption Predictor")

    # Header
    st.header("Welcome to the Energy Consumption Predictor app!")

    # Introduction
    st.write(
        "The objective of this project is to predict the Energy Consumption in the Steel Industry.")
    st.write("By utilizing machine learning techniques, we aim to develop a predictive model that can accurately estimate the energy consumption based on various input parameters.")
    st.write("This model can help in optimizing energy usage, identifying energy-saving opportunities, and improving overall operational efficiency in the steel industry.")

    # Project Details
    st.subheader("Project Details")
    st.write("This project focuses on developing a predictive model for energy consumption in the steel industry.")
    st.write("The model takes into account various factors such as lagging and leading current reactive power, CO2 emissions, power factor, NSM, week status, days of the week, and load type.")
    st.write("By analyzing historical data and training the model, we can make accurate predictions of energy consumption for future scenarios.")

    # Instructions
    st.subheader("Instructions")
    st.write("To use the Energy Consumption Predictor app, follow these steps:")
    st.write(
        "1. Use the sidebar to input the required parameters for energy consumption prediction.")
    st.write(
        "2. Click on the 'Predict Energy Consumption' button to generate the predicted results.")
    st.write(
        "3. The app will display the predicted energy consumption value in kilowatt-hours (kWh).")

    # Get Started
    st.subheader("Get Started")
    st.write("Start predicting energy consumption by providing the necessary input parameters in the sidebar.")
    st.write(
        "Click on the 'Predict Energy Consumption' button to see the predicted results.")


def show_prediction_page():
    st.title("Energy Consumption Predictor")

    # Create input fields for user input
    lagging_power = st.number_input('Lagging Current Reactive Power (kVarh)')
    leading_power = st.number_input('Leading Current Reactive Power (kVarh)')
    co2_emissions = st.number_input('CO2 Emissions (tCO2)')
    lagging_power_factor = st.number_input('Lagging Current Power Factor')
    leading_power_factor = st.number_input('Leading Current Power Factor')
    nsm = st.number_input('NSM')
    is_weekday = st.selectbox('Week Status', ['Weekday', 'Weekend'])
    days_of_week = st.selectbox('Days of Week', [
        'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
    load_type = st.selectbox(
        'Load Type', ['Light Load', 'Medium Load', 'Maximum Load'])

    # Create a dataframe from the user input
    user_input = pd.DataFrame(
        {
            'Lagging_Current_Reactive.Power_kVarh': [lagging_power],
            'Leading_Current_Reactive_Power_kVarh': [leading_power],
            'CO2(tCO2)': [co2_emissions],
            'Lagging_Current_Power_Factor': [lagging_power_factor],
            'Leading_Current_Power_Factor': [leading_power_factor],
            'NSM': [nsm],
            'WeekStatus_Weekday': [1 if is_weekday == 'Weekday' else 0],
            'WeekStatus_Weekend': [1 if is_weekday == 'Weekend' else 0],
            'Day_of_week_Friday': [1 if days_of_week == 'Friday' else 0],
            'Day_of_week_Monday': [1 if days_of_week == 'Monday' else 0],
            'Day_of_week_Saturday': [1 if days_of_week == 'Saturday' else 0],
            'Day_of_week_Sunday': [1 if days_of_week == 'Sunday' else 0],
            'Day_of_week_Thursday': [1 if days_of_week == 'Thursday' else 0],
            'Day_of_week_Tuesday': [1 if days_of_week == 'Tuesday' else 0],
            'Day_of_week_Wednesday': [1 if days_of_week == 'Wednesday' else 0],
            'Load_Type_Light_Load': [1 if load_type == 'Light Load' else 0],
            'Load_Type_Maximum_Load': [1 if load_type == 'Maximum Load' else 0],
            'Load_Type_Medium_Load': [1 if load_type == 'Medium Load' else 0]
        }
    )

    # Add a selectbox for choosing the prediction model
    prediction_model = st.selectbox('Prediction Model', [
                                    'Linear Regression', 'Ridge Regression', 'Lasso Regression', 'Elastic Net Regression'])

    # Load the selected prediction model
    if prediction_model == 'Linear Regression':
        with open('regression_model.pkl', 'rb') as file:
            model = pickle.load(file)
    elif prediction_model == 'Ridge Regression':
        with open('ridge_model.pkl', 'rb') as file:
            model = pickle.load(file)
    elif prediction_model == 'Lasso Regression':
        with open('lasso_model.pkl', 'rb') as file:
            model = pickle.load(file)
    elif prediction_model == 'Elastic Net Regression':
        with open('elsaticNet_model.pkl', 'rb') as file:
            model = pickle.load(file)

    # Add a predict button
    predict_button = st.button('Predict Energy Consumption')
    if predict_button:
        prediction = model.predict(user_input)

        # Display the predicted energy consumption
        st.success(
            'Predicted Energy Consumption: {:.3f} kWh'.format(prediction[0]))


def show_about_page():
    st.title("About")
    st.write("This app was created to predict the Energy Consumption using Machine Learning model."
             )
    st.markdown("### GitHub Repository")
    github_link = "https://github.com/Saurav0129/Steel-Industry-Energy-Consumption-Prediction"
    st.markdown(
        f"Check out the [GitHub repository]({github_link}) for more details and to access the source code."
    )


if __name__ == '__main__':
    main()
