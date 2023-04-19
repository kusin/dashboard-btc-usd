# library ui-dashboard
import streamlit as st;
from streamlit_extras import add_vertical_space as avs

# library manipulation dataset
import pandas as pd;
import numpy as np;

# library data visualization
import plotly.express as px;
import plotly.graph_objects as go;

# call method from other file
from class_dataset import *;
from class_visualization import *;
from visualization import *;


# --------------------------------------------------------------- #
# -- Main Function ---------------------------------------------- #
# --------------------------------------------------------------- #
if __name__ == "__main__":

    # --------------------------------------------------------------- #
    # -- setting configuration -------------------------------------- #
    # --------------------------------------------------------------- #
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
    # -- container-sidebar ------------------------------------------ #
    # --------------------------------------------------------------- #
    with st.sidebar:
        st.info("Main Menu");
        pages = st.selectbox(label="", options=("Dashboard", "Exploratory Data Analysis", "Model Predictions"), label_visibility="collapsed");
    
        avs.add_vertical_space(3);
        st.success("Sponsorship");
        st.markdown("- UIN Syarif Hidayatullah Jakarta");
        st.markdown("- Institut Pertanian Bogor");
        
    # --------------------------------------------------------------- #
    # -- container-wrapper ------------------------------------------ #
    # --------------------------------------------------------------- #
    with st.container():

        # load dataset
        dataset = dataset.get_dataset();
        
        # container-header
        with st.container():
            st.markdown("<h1 style='color:#9AC66C;'>Stock price predictions with algorithm LSTM and GRU</h1>",unsafe_allow_html=True);
        
        # container-OHLC
        with st.container():
            
            # define columns with col-4 row-1
            col1, col2, col3, col4 = st.columns(4);
            col1.metric(label="Open Price", value="$"+"{:,.2f}".format(dataset["Open"].iloc[-1]), delta="0,00%");
            col2.metric(label="High price", value="$"+"{:,.2f}".format(dataset["High"].iloc[-1]), delta="0,00%");
            col3.metric(label="Low price", value="$"+"{:,.2f}".format(dataset["Low"].iloc[-1]), delta="0,00%");
            col4.metric(label="Close price", value="$"+"{:,.2f}".format(dataset["Close"].iloc[-1]), delta="0,00%");

            # description dataset
            st.text("* Update dataset 2022-11-30");

        # container-dataframe
        with st.container():
            st.dataframe(data= dataset.sort_values('Date', ascending=False), use_container_width=True);

        # container-visualization
        with st.container():

            # define columns with col-2 row-1
            col1, col2= st.columns(2);
            col1.plotly_chart(
                visualization.time_series(
                    dataset["Date"],
                    dataset["Open"],
                    "Open Price",
                    "blue"
                ),
                use_container_width=True
            );
            col2.plotly_chart(
                visualization.time_series(
                    dataset["Date"],
                    dataset["Close"],
                    "Close Price",
                    "green"
                ),
                use_container_width=True
            );
            col1.plotly_chart(
                visualization.time_series(
                    dataset["Date"],
                    dataset["High"],
                    "High Price",
                    "orange"
                ),
                use_container_width=True
            );
            col2.plotly_chart(
                visualization.time_series(
                    dataset["Date"],
                    dataset["Low"],
                    "Low Price",
                    "red"
                ),
                use_container_width=True
            );
