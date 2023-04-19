# library ui-dashboard
import streamlit as st;
from streamlit_option_menu import option_menu

# library manipulation dataset
import pandas as pd;

# library manipulation array
import numpy as np;

# library data visualization
import plotly.express as px;
import plotly.graph_objects as go;

from Model import *;


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
        add_pages = st.selectbox("Choose Pages ", ("Dashboard", "Exploratory Data Analysis", "Model Predictions"));
        add_algorithm = st.selectbox("Choose Algorithm ", ("LSTM-RNN", "GRU-RNN"));
    
    # --------------------------------------------------------------- #
    # -- container-wrapper ------------------------------------------ #
    # --------------------------------------------------------------- #
    with st.container():

        # container-header
        with st.container():
            st.header("Prediction stock price with algorithm LSTM and GRU");

        # container-content
        with st.container():
            if add_pages == "Dashboard":
                Dashboard();
            elif add_pages == "Exploratory Data Analysis":
                EDA();
            else:
                Model();