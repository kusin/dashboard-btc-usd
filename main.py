# library ui-dashboard
import streamlit as st;

# library manipulation dataset
import pandas as pd;

# library manipulation array
import numpy as np;

# library data visualization
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.graph_objs import Line


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
    sb_dataset = st.selectbox('choose dataset',('BTC-USD','IBM'));
with col2:
    dt_start = st.date_input("start date");
with col3:
    dt_end = st.date_input("end date");

# load dataset stock price
if sb_dataset == "BTC-USD":
    dataset = pd.read_csv("dataset/btc-usd.csv", parse_dates=["Date"]);
else:
    dataset = pd.read_csv("dataset/ibm.csv", parse_dates=["Date"]);

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

# set two columns
fig1, fig2 = st.columns(2, gap="large");
with fig1:
    st.text("Open price visualization");
    st.plotly_chart(px.line(dataset, x='Date', y='Open', color_discrete_sequence=["#0051ee"]), use_container_width=True);
with fig2:
    st.text("Close price visualization");
    st.plotly_chart(px.line(dataset, x='Date', y='Close', color_discrete_sequence=["#20B2AA"]), use_container_width=True);

# set two columns
fig1, fig2 = st.columns(2, gap="large");
with fig1:
    st.text("High price visualization");
    st.plotly_chart(px.line(dataset, x='Date', y='High', color_discrete_sequence=["#FF8C00"]), use_container_width=True);
with fig2:
    st.text("Low price visualization");
    st.plotly_chart(px.line(dataset, x='Date', y='Low', color_discrete_sequence=["#DC143C"]), use_container_width=True);
