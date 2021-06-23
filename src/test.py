# 这部分是使用streamlit的新手教程，尝试着练习一下

import streamlit as st
import pandas as pd
import numpy as np

# 标题
st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('./data/uber.csv')

# 读取数据
# 缓存工作机制
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# 加载ing提示
data_load_state = st.text('Loading data...')
# 加载10000行
data = load_data(10000)
# 加载完成提示
data_load_state.text("Done! (using st.cache)")

# 框1的小标题
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# 框2的小标题
st.subheader('Number of pickups by hour')
# np.histogram用于生成直方图
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# 画图
st.subheader('Map of all pickups')
st.map(data)

hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

