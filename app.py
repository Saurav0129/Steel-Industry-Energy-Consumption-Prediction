import streamlit as st
import pickle
import pandas as pd

# Load the saved Linear Regression model
with open('regression_model.pkl', 'rb') as file:
    model = pickle.load(file)


def main():
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

    # Reorder the columns to match the model's feature order
    user_input = user_input[[
        'Lagging_Current_Reactive.Power_kVarh',
        'Leading_Current_Reactive_Power_kVarh',
        'CO2(tCO2)',
        'Lagging_Current_Power_Factor',
        'Leading_Current_Power_Factor',
        'NSM',
        'WeekStatus_Weekday',
        'WeekStatus_Weekend',
        'Day_of_week_Friday',
        'Day_of_week_Monday',
        'Day_of_week_Saturday',
        'Day_of_week_Sunday',
        'Day_of_week_Thursday',
        'Day_of_week_Tuesday',
        'Day_of_week_Wednesday',
        'Load_Type_Light_Load',
        'Load_Type_Maximum_Load',
        'Load_Type_Medium_Load'
    ]]

    # Add a predict button
    predict_button = st.button('Predict Energy Consumption')
    if predict_button:
        prediction = model.predict(user_input)

        # Display the predicted energy consumption
        # st.success ('Predicted Energy Consumption: {}'.format(prediction))
        st.success('Predicted Energy Consumption: {:.3f} kWh'.format(prediction[0]))


        


if __name__ == '__main__':
    main()