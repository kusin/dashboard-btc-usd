# library ui-dashboard
import streamlit as st;

# library manipulation dataset
import pandas as pd;
import pandas_datareader.data as web
#from pandas_datareader import DataReader as web

# library manipulation array
import numpy as np;

# library data visualization
import plotly.express as px;

# set config ui-dasboard streamlit
st.set_page_config(
    page_title="My Dasboard",
    page_icon="",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Get Help": "https://www.github.com/kusin",
        "Report a bug": "https://www.github.com/kusin",
        "About": "### Copyright 2022 all rights reserved by Aryajaya Alamsyah"
    }
);

# container-header
with st.container():
    st.markdown("## Comparison algorithm LSTM and GRU use architecture stacked and bidirectional");

# container-dataset
with st.container():

    # set columns with col-3 row-1
    col1, col2, col3 = st.columns(3);

    # columns col-1
    col1.selectbox('choose dataset',('BTC-USD','IBM'));

    # columns col-2
    col2.date_input("start date");

    # columns col-3
    col3.date_input("end date");

# container-show-dataset
with st.container():
    #dataset = web("BTC-USD", data_source="yahoo", start='2019-09-10', end='2019-10-09');
    df = web.DataReader('GE', 'yahoo', start='2019-09-10', end='2019-10-09')

st.dataframe(df);

