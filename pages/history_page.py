import streamlit as st
import pandas as pd

import func

def history_page():
    data = pd.read_csv('data_log.csv')
    st.dataframe(data)