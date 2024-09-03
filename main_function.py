import streamlit as st
import datetime as dt
# --------------------------------------------------------------------------------------------------------------

def form_dataset():

  # My Form
  with st.form("my-form1"):
    cryptocurrency = st.selectbox(label="Choose a cryptocurrency", options=("BTC-USD", "ETH-USD"))
    start = st.date_input(label="Start Date", value=dt.date(2015,1,1))
    end = st.date_input(label="End Date", value=dt.date(2024,5,1))
    process = st.form_submit_button(label="Process", type="secondary", use_container_width=True)
  
  # return values
  return cryptocurrency, start, end, process
# --------------------------------------------------------------------------------------------------------------

def form_hyperparameter():

  # My Form
  with st.form("my-form2"):
    algorithms = st.selectbox(label="Choose a algorithms", options=("SBi-LSTM-RNN", "SBi-GRU-RNN"), index=0)
    optimizers = st.selectbox(label="Choose a optimizers", options=("adam", "adamax", "rmsprop"), index=1)
    batch_size = st.selectbox(label="Choose a batch size", options=(8, 16, 24, 32), index=1)
    epoch = st.selectbox(label="Choose a optimizers", options=(25, 50), index=1)
    submit = st.form_submit_button(label="Submit", type="secondary", use_container_width=True)
  
  # return values
  return algorithms, optimizers, batch_size, epoch, submit
# --------------------------------------------------------------------------------------------------------------

