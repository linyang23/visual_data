from re import S
from numpy.core.numeric import NaN
import streamlit as st
import pandas as pd
import numpy as np

st.title('covid19-20210622')

@st.cache
def load_data(path):
    data = pd.read_csv(path)
    data.columns = data.columns.str.lower()
    return data

data = load_data("data/covid19_20210622.csv")
if st.checkbox('show raw data'):
    st.write(data)

if st.checkbox('Show all cases'):
    st.subheader('all cases')
    all_data = pd.DataFrame(data.values.T, index=data.columns, columns=data["name"].unique())
    st.line_chart(all_data)