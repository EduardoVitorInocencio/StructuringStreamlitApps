# CORE PACKAGES
import streamlit as st


# LOAD EDA PACKAGES
import pandas as pd

def run_eda_app():
    st.subheader("From Exploratory Data Analysis")
    df = pd.read_csv("data/diabetes.csv")
    st.dataframe(df)
    
