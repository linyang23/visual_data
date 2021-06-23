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
st.write(data)

product_list = data["country name"].unique()
product_type = st.sidebar.selectbox(
    "Which kind of event do you want to explore?",
    product_list
)
part_data =[(data["country name"] == product_type)]

st.title(f"{product_type}的GDP折线图")
sub_data = data[(data["country name"] == product_type)]
sub_data2 = pd.DataFrame(sub_data.values.T, index=sub_data.columns, columns=sub_data.index)[4:]
print(sub_data2)
st.line_chart(sub_data2)