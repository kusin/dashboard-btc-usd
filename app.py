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
from func_plot import plot_multiple_line;

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
    st.header("Comparison LSTM and GRU use architecture stacked and bidirectional");

# container-price-OHLC
with st.container():
    
    # define columns with col-4 row-1
    col1, col2, col3, col4 = st.columns(4);

    # columns-1 open price
    col1.metric(
        label="Open Price",
        value="$"+"{:,.2f}".format(dataset["Open"].iloc[-1]),
        delta="0,00%"
    );

    # columns-2 high price
    col2.metric(
        label="High price",
        value="$"+"{:,.2f}".format(dataset["High"].iloc[-1]),
        delta="0,00%");

    # columns-3 low price
    col3.metric(
        label="Low price",
        value="$"+"{:,.2f}".format(dataset["Low"].iloc[-1]),
        delta="0,00%");

    # columns-4 close price
    col4.metric(
        label="Close price",
        value="$"+"{:,.2f}".format(dataset["Close"].iloc[-1]),
        delta="0,00%");

    # description dataset
    st.text("* Update dataset 2022-11-30");

# container-show-dataset
with st.container():
    st.plotly_chart(
        plot_multiple_line(dataset, "Date", ["Open", "High", "Low", "Close"]), use_container_width=True
    );
