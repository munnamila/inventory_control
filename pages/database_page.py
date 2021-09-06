import streamlit as st
import pandas as pd

def database_page():

    data = pd.read_csv('database.csv')

    st.dataframe(data)