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
        add_pages = st.selectbox(label="", options=("Dashboard", "Exploratory Data Analysis", "Model Predictions"), label_visibility="collapsed");
    
    # --------------------------------------------------------------- #
    # -- container-wrapper ------------------------------------------ #
    # --------------------------------------------------------------- #
    with st.container():

        # container-header
        with st.container():
            st.header("Stock price predictions with algorithm LSTM and GRU");

