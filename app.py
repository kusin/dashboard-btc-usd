# library ui-dashboard
import streamlit as st;

# library manipulation dataset
import pandas as pd;

# library manipulation array
import numpy as np;

# library data visualization
import plotly.express as px;
import plotly.graph_objects as go;

# import function any file .py
from func_plot import plot_line;

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

# load dataset
dataset = pd.read_csv("dataset/btc-usd.csv", parse_dates=["Date"]);

# container-header
with st.container():
    st.markdown("## Comparison LSTM and GRU use architecture stacked and bidirectional");

# container-dataset
with st.container():

    # set columns with col-3 row-1
    col1, col2, col3, col4 = st.columns(4);

    # columns col-1
    col1.selectbox("choose algorithm",("LSTM-RNN", "GRU-RNN"));

    # columns col-2
    col2.selectbox("choose dataset",("BTC-USD", "IBM"));

    # columns col-3
    col3.date_input("start date");

    # columns col-4
    col4.date_input("end date");

# container-show-dataset
with st.container():
    st.subheader("Data visualization time series");

    # plot line sst nina 3.4
    st.plotly_chart(
        plot_line(dataset, "Date", "Open", "#3457D5"), use_container_width=True
    );
