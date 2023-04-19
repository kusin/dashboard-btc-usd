# --------------------------------------------------------------- #
# -- List library ----------------------------------------------- #
# --------------------------------------------------------------- #

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
from other.func_plot import *;


# --------------------------------------------------------------- #
# -- setting configuration -------------------------------------- #
# --------------------------------------------------------------- #

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


# --------------------------------------------------------------- #
# -- data acquisition ------------------------------------------- #
# --------------------------------------------------------------- #

# load dataset
dataset = pd.read_csv("../dataset/btc-usd.csv", parse_dates=["Date"]);

# set index date
dataset = dataset.set_index("Date");


# --------------------------------------------------------------- #
# -- container-sidebar ------------------------------------------ #
# --------------------------------------------------------------- #
with st.sidebar:
    add_pages = st.selectbox(
        "Choose Pages ",
        ("Dashboard", "Exploratory Data Analysis", "Model Predictions")
    );
    add_algorithm = st.selectbox(
        "Choose Algorithm ",
        ("LSTM-RNN", "GRU-RNN")
    );


# container-header
with st.container():
    st.header("Prediction stock price with algorithm LSTM and GRU");

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
        delta="0,00%"
    );

    # columns-3 low price
    col3.metric(
        label="Low price",
        value="$"+"{:,.2f}".format(dataset["Low"].iloc[-1]),
        delta="0,00%"
    );

    # columns-4 close price
    col4.metric(
        label="Close price",
        value="$"+"{:,.2f}".format(dataset["Close"].iloc[-1]),
        delta="0,00%"
    );

    # description dataset
    st.text("* Update dataset 2022-11-30");

# container-plot-dataset
with st.container():

    # description sub-header
    st.subheader("Data visualization line-plot OHLC");
    
    # line-plot OHLC
    st.plotly_chart(
        plot_multiple_line(dataset, ["Open", "High", "Low", "Close"]), use_container_width=True
    );

# cointainer-eda
with st.container():

    # description sub-header
    st.subheader("Exploratory data analysis");

    # set year dataset
    set_year = st.selectbox("Choose year", tuple(str(x) for x in range(2015, 2022, 1)));

    # set start year and end year
    start_date = str(set_year)+"-01-01";
    end_date = str(set_year)+"-12-31";
    
    # set dataset with specific year
    df_year = func_agg_year(dataset, start_date, end_date);
    
    # define tab-index
    tab1, tab2 = st.tabs(["Line plot", "Bar-plot"]);

    # tab-index1 line-plot
    with tab1:

        # line-plot OHLC with specific year
        st.plotly_chart(
            plot_multiple_line(df_year, ["Open", "High", "Low", "Close"]), use_container_width=True
        );
    
    # tab-index2 bar-plot
    with tab2:

        # bar-plot OHLC with specific year
        st.plotly_chart(
            plot_grouped_bar(df_year, ["Open", "High", "Low", "Close"]), use_container_width=True
        );
    