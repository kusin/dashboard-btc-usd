# library ui-dashboard
import streamlit as st
from streamlit_extras import add_vertical_space as avs

# library manipulation dataset
import pandas as pd

# library manipulation array
import numpy as np

# library data visualization
import plotly.express as px

# call method from other file
from class_dataset import dataset
from class_visualization import visualization

# set config ui-dasboard streamlit
st.set_page_config(
    page_title="My Dasboard",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.github.com/kusin",
        "Report a bug": "https://www.github.com/kusin",
        "About": "### Copyright 2023 all rights reserved by Aryajaya Alamsyah"
    })
# --------------------------------------------------------------------------------------------------------------------------------

# container-header
with st.container():
    st.markdown("## Model Predictions of Cryptocurrency Using Neural Network Algorithms")
    st.text("Created by Aryajaya Alamsyah, December 2023")
    avs.add_vertical_space(2)
# --------------------------------------------------------------------------------------------------------------------------------

# container-dataset
with st.container():
    # labels resume-sales
    st.info("")

    # get dataset btc-usd
    df = dataset().get_dataset()
    df = df[["Date", "Open", "High", "Low", "Close"]]

    # set two columns
    col1, col2 = st.columns([0.4,0.6], gap="medium")
    with col1:
        st.dataframe(df,use_container_width=True)
    with col2:
        st.plotly_chart(visualization.line_plot(df),use_container_width=True)
    #avs.add_vertical_space(2)
# --------------------------------------------------------------------------------------------------------------------------------

# container-models
with st.container():
    # labels resume-sales
    st.info("")
    
    # set two columns
    col1, col2 = st.columns([0.3,0.7], gap="small")
    with col1:
        with st.form("my_form"):
            st.write("Setting your model predictions")
            algorithms = st.selectbox("Choose an algorithm", ("SB LSTM-RNN", "SB GRU-RNN"), placeholder="Choose an algorithm", index=None)
            models = st.selectbox("Choose a models ", ("Univariate", "Multivariate"), placeholder="Choose an algorithm",index=None)
            submitted = st.form_submit_button("Submit", type="primary")
    with col2:
        st.text("Results")