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


product_list = data.columns[2:]
product_type = st.sidebar.selectbox(
    "Which data to show",
    product_list,
    key = 'a'
)

st.title(f"{product_type} up to 6/22/2021")
sub_data = data[[product_type]]
sub_data.index = np.array(data['name'])
st.line_chart(sub_data)    