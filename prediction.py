import streamlit as st
import pickle
import numpy as np
@st.cache
def load_model():
    model = pickle.load(open('saved_steps.pkl','rb'))
    return model
def show_predict_page():
    st.title("Software Developer Salary Prediction")
    model = load_model()
    country = st.selectbox("country",model['le_country'].classes_)
    education = st.selectbox("education level",model['le_education'].classes_)
    age = st.selectbox("age group",model['le_age'].classes_)
    experience = st.slider("Years of experience",0,50,1)
    ok = st.button("Calculate Salary")
    if ok:
        X = np.array([[country,age,education,experience]])
        X[:,0] = model['le_country'].transform(X[:,0])
        X[:,1] = model['le_age'].transform(X[:,1])
        X[:,2] = model['le_education'].transform(X[:,2])
        X = X.astype(float)
        salary = model['model'].predict(X)
        st.subheader(f"estimated salary is ${salary[0]:.2f}")
