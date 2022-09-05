from json import load
import streamlit as st
import pickle
import matplotlib.pyplot as plt
@st.cache
def load_data():
    data = pickle.load(open('data.pkl','rb'))
    return data
def show_explore_page():
    data = load_data()
    fig1,ax1 = plt.subplots()
    ax1.pie(data['Country'].value_counts(),labels=data['Country'].value_counts().index)
    ax1.axis("equal")
    st.pyplot(fig1)
    st.write("""#### 
    Mean salary based on countries
    """)
    x = data.groupby('Country')["salary"].mean().sort_values(ascending=True)
    st.bar_chart(x)
    st.write("""#### 
    Mean salary based on experience
    """)
    x = data.groupby('experience')["salary"].mean().sort_values(ascending=True)
    st.line_chart(x)
    st.write("""#### 
    Mean salary based on Age
    """)
    x = data.groupby('Age')["salary"].mean().sort_values(ascending=True)
    st.bar_chart(x)