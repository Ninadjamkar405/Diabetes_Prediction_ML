import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open("N:/Diabetes Prediction (ML Project)/trained_model.sav",'rb'))

def diabetes_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'


def main():
    st.title('Diabetes Prediction Web Page')

    pregnancies = st.text_input("Enter number of pregnencies: ")
    glucose = st.text_input("Enter glucose level: ")
    BloodPressure = st.text_input("Enter Blood Pressure value: ")
    SkinThickness = st.text_input("Enter Skin Thickness value: ")
    Insuline = st.text_input("Enter Insuline level: ")
    BMI = st.text_input("Enter BMI value: ")
    DiabetesPedigreeValue = st.text_input("Enter Diabetes Pedigree Value value: ")
    Age = st.text_input("Enter Age: ")

    #code for prediction
    diagnosis = ''

    if st.button("Daibetes test result"):
        diagnosis = diabetes_prediction([pregnancies, glucose, BloodPressure, SkinThickness, Insuline, BMI, DiabetesPedigreeValue, Age])

    st.success(diagnosis)

if __name__ == "__main__":
    main()
