# set library
import streamlit as st

# import from other file
from C01_data_collection import *
from C02_visualization import *
from main_function import *
# --------------------------------------------------------------------------------------------------------------

# set random number
import random as rm
rm.seed(1234)

# set random number
import numpy as np
np.random.seed(1234)

# set random number
import tensorflow as tf
tf.random.set_seed(1234)
# --------------------------------------------------------------------------------------------------------------

# config web streamlit
st.set_page_config(page_title="My Dasboard",layout="wide")

# container-header
st.markdown("## Prediction of cryptocurrency and stock price using neural network")

# split three columns
col1, col2, col3 = st.columns([0.25, 0.25, 0.5], gap="small")

# columns form dataset
with col1:
  st.info("Config Dataset")
  cryptocurrency, start, end, process = form_dataset()
# --------------------------------------------------------------------------------------------------------------

# columns - information crypto
with col2:
  st.info("Top Five Cryptocurrency on Market")
  st.write("1. Bitcoin (BTC)")
  st.write("2. Ethereum (EHT)")
  st.write("3. Tether (USDT)")
  st.write("4. Binance Coin (BNB)")
  st.write("5. Solana (SOL)")
# --------------------------------------------------------------------------------------------------------------

# columns - results dataset
with col3:
  st.info("Exploratory Data Analysis")
  if process:
    ticker      = cryptocurrency
    startDate   = start
    endDate     = end
  else:
    ticker      = "BTC-USD"
    startDate   = "2015-01-01"
    endDate     = "2024-05-01"
  dataset = getData(ticker, startDate, endDate)

  # split two tab-index
  tab1, tab2 = st.tabs(["Visualization Data", "Historical Data"])
  tab1.plotly_chart(timeseries_plot(dataset), use_container_width=True)
  tab2.dataframe(dataset, use_container_width=True)
# --------------------------------------------------------------------------------------------------------------

# # split three columns
# col1, col2, col3 = st.columns([0.25, 0.25, 0.5], gap="small")

# columns - form hyperparameter
with col1:
  st.info("Hyperparameter Tuning")
  algorithms, optimizers, batch_size, epoch, submit = form_hyperparameter()
# --------------------------------------------------------------------------------------------------------------

# columns - evaluation models
with col2:
  st.info("Evaluation Models")
  if submit:
    process_prediction()
# --------------------------------------------------------------------------------------------------------------

# columns - results prediction
with col3:
  st.info("Results Prediction")
  if submit:

  #   # results prediction
  #   results = pd.concat([
  #     pd.DataFrame(np.array(dataset[["Date"]].iloc[len(y_train)+120:]), columns=["Date"]),
  #     pd.DataFrame(np.array(inverse(scaler=scaler,scaled=y_test)), columns=["Actual"]),
  #     pd.DataFrame(np.array(inverse(scaler=scaler,scaled=predictions)), columns=["Predictions"])
  #   ],axis=1)

    # split two tab-index
    tab1, tab2 = st.tabs(["Visualization Data", "Historical Data"])
    tab1.plotly_chart(timeseries_plot(dataset), use_container_width=True)
    tab2.dataframe(dataset, use_container_width=True)
# --------------------------------------------------------------------------------------------------------------