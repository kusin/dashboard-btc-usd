# library ui-dashboard
import streamlit as st;
from streamlit_extras import add_vertical_space as avs

# library manipulation dataset
import pandas as pd;
import numpy as np;

# library data visualization
import plotly.express as px;
import plotly.graph_objects as go;
from matplotlib import pyplot
from matplotlib import pyplot as plt

# call method from other file
from class_dataset import *;
from class_visualization import *;
from class_pre_processing import *;


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
    # with st.sidebar:
    #     st.info("Main Menu");
    #     pages = st.selectbox(label="Choose Pages", options=("Dashboard", "Exploratory Data Analysis", "Model Predictions"), label_visibility="collapsed");
    
    #     avs.add_vertical_space(3);
    #     st.success("About US");
    #     st.markdown("- Copyright by Aryajaya Alamsyah, S.Kom");
        
        
    # --------------------------------------------------------------- #
    # -- container-wrapper ------------------------------------------ #
    # --------------------------------------------------------------- #
    with st.container():

        # load dataset
        dataset = dataset.get_dataset();
        
        # container-header
        with st.container():
            st.markdown("<h1 style='color:#9AC66C; text-align:center;'>Stock price predictions with algorithm LSTM and GRU</h1>",unsafe_allow_html=True);
        
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
            avs.add_vertical_space(2);

        # container-visualization
        with st.container():

            # header container
            st.success("Exploratory Data Analysis");

            # define columns with col-2 row-1
            col1, col2= st.columns(2);
            col1.plotly_chart(
                visualization.time_series1(
                    dataset.index.values,
                    dataset["Open"],
                    "Open Price",
                    "blue"
                ),
                use_container_width=True
            );
            col2.plotly_chart(
                visualization.time_series1(
                    dataset.index.values,
                    dataset["Close"],
                    "Close Price",
                    "green"
                ),
                use_container_width=True
            );
            col1.plotly_chart(
                visualization.time_series1(
                    dataset.index.values,
                    dataset["High"],
                    "High Price",
                    "orange"
                ),
                use_container_width=True
            );
            col2.plotly_chart(
                visualization.time_series1(
                    dataset.index.values,
                    dataset["Low"],
                    "Low Price",
                    "red"
                ),
                use_container_width=True
            );

        # container-pre-processing
        with st.container():

            # header container
            st.success("Data Pre-processing");
            
            # form pre-processing
            with st.form("my_form"):
                cb_featured = st.selectbox("Choose a feature",("--", "Open", "High", "Low", "Close"));
                cb_normalized = st.selectbox("Choose method of normalized data", ('--', 'Min-Max'));
                cb_splitted = st.selectbox("Choose percentage of splitted data", ('--', '80-20'));
                cb_look_back = st.selectbox("Choose period look back", ('--', '60'));
                btn_process = st.form_submit_button("Submit");

            if btn_process:
                
                # 1. feature selection
                dataset = dataset.filter([cb_featured]);
                data = dataset.values;

                # 2. normalized data
                scaled_data = PreProcessing.normalization(data);

                # 3. splitted data
                train_data, test_data = PreProcessing.splitting(scaled_data, 0.80, 0.20);

                # 4. supervised learning
                look_back = 60;
                x_train, y_train = PreProcessing.create_dataset(look_back, train_data);
                x_test, y_test = PreProcessing.create_dataset(look_back, test_data);

                #. 5. reshape input to be [samples, time steps, features]
                x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1));
                x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1));

                st.write(x_train.shape, x_test.shape)

                st.pyplot(
                    visualization.time_series2(dataset.index.values, scaled_data, "red"), use_container_width=True
                );