from re import S
from numpy.core.numeric import NaN
import streamlit as st
import pandas as pd
import numpy as np

st.title('world gdp')
DATE_COLUMN = '1960'

@st.cache
def load_data(path):
    data = pd.read_csv(path)
    data.columns = data.columns.str.lower()
    return data

data = load_data("data/gdp.csv")
if st.checkbox('show raw data'):
    st.write(data)

if st.checkbox('Show all gdp'):
    st.subheader('all')
    all_data = pd.DataFrame(data.values.T, index=data.columns, columns=data["country name"].unique())[4:]
    st.line_chart(all_data)

product_list = data["country name"].unique()
print(product_list)

product_type = st.sidebar.selectbox(
    "Which kind of event do you want to compare?",
    product_list,
    key = 'ada'
)

product_type_2 = st.sidebar.selectbox(
    "Which kind of event do you want to compare?",
    product_list,
    key = 'ava'
)

if(product_type != product_type_2):
    st.title(f"{product_type} vs {product_type_2} 的GDP对比图")
    sub_data = data[(data["country name"] == product_type) | (data["country name"] == product_type_2)]
    sub_data2 = pd.DataFrame(sub_data.values.T, index=sub_data.columns, columns=[product_type, product_type_2])[4:]

    st.line_chart(sub_data2)

else:
    st.title(f"{product_type}的GDP折线图")
    sub_data = data[(data["country name"] == product_type) | (data["country name"] == product_type_2)]
    sub_data2 = pd.DataFrame(sub_data.values.T, index=sub_data.columns, columns=[product_type])[4:]
    st.line_chart(sub_data2)
