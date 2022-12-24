# library ui-dashboard
import streamlit as st;

# library manipulation dataset
import pandas as pd;

# library manipulation array
import numpy as np;

# library data visualization
import plotly.express as px
import plotly.graph_objects as go

# set config ui-dasboard streamlit
st.set_page_config(
    page_title="My Dasboard",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Get Help": "https://www.github.com/kusin",
        "Report a bug": "https://www.github.com/kusin",
        "About": "### Copyright 2022 all rights reserved by Aryajaya Alamsyah"
    }
);

# container-header-fuild
st.header("Comparison algorithm LSTM and GRU use architecture stacked and bidirectional");

# form configuration dataset
col1, col2, col3 = st.columns(3, gap="small");
with col1:
    sb_dataset = st.selectbox('choose dataset',('BTC-USD','MSFT','AAPL','GOOG','IBM'));
with col2:
    dt_start = st.date_input("start date");
with col3:
    dt_end = st.date_input("end date");

# load dataset stock price
if sb_dataset == "BTC-USD":
    dataset = pd.read_csv("dataset/btc-usd.csv");
elif sb_dataset == "MSFT":
    dataset = pd.read_csv("dataset/msft.csv");
elif sb_dataset == "AAPL":
    dataset = pd.read_csv("dataset/aapl.csv");
elif sb_dataset == "GOOG":
    dataset = pd.read_csv("dataset/goog.csv");
else:
    dataset = pd.read_csv("dataset/ibm.csv");

# show dataset with dataframe
st.text("show dataset "+sb_dataset);
st.dataframe(dataset, use_container_width=True);

# container-plot-time-series
st.text("data visualization open-high-low-close (OHLC)");
st.plotly_chart(
    px.line(dataset,
            x=dataset["Date"],
            y=["Close", "Open", "High", "Low"],
            color_discrete_sequence=["blue", "green", "orange", "red"]),
    use_container_width=True
);


