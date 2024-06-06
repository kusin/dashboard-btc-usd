# library manipulation dataset
import pandas as pd
import numpy as np

# import library streamlit
import streamlit as st
from streamlit_extras import add_vertical_space as avs 

# library data visualization
import plotly.express as px
import plotly.graph_objects as go

# library data preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# lib neural network algorithms
import tensorflow as tf
from keras.layers import LSTM
from keras.layers import GRU

# library evaluations model
from math import sqrt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error
import scipy.stats as sc

# config web streamlit
st.set_page_config(
  page_title="My Dasboard - BTC-USD",
  page_icon="",
  layout="wide",
  initial_sidebar_state="auto",
  menu_items={
    "Get Help": "https://www.github.com/kusin",
    "Report a bug": "https://www.github.com/kusin",
    "About": "### Copyright 2022 all rights reserved by Aryajaya Alamsyah"
  }
)

# --------------------------------------------------------------------------------------- #
# data visualization -------------------------------------------------------------------- #
# --------------------------------------------------------------------------------------- #
def line_plot(df, title):

  # add lineplot with graph object
  fig = go.Figure()
  for column in df.columns[1:]:
    fig.add_trace(
      go.Scatter(x=df["Date"],y=df[column], mode='lines', name=column)
    )

  # update layout lineplot
  fig.update_layout(
    title = title,
    xaxis_title = "",
    yaxis_title = "",
    xaxis=dict(tickangle=0),
    yaxis=dict(tickangle=0),
    legend=dict(title='', orientation='h', yanchor='top', y=1, xanchor='center', x=0.5),
  )

  # return values
  return fig
# --------------------------------------------------------------------------------------- #

# function for supervised learning
def create_dataset(look_back, dataset):    
  # declare variable X and Y
  dataX = []
  dataY = []
    
  # for loop for create supervised learning
  for i in range(look_back, len(dataset)):
    dataX.append(dataset[i-look_back:i, 0])
    dataY.append(dataset[i, 0])
        
  # return value X and Y
  return np.array(dataX), np.array(dataY)
# --------------------------------------------------------------------------------------- #

# container-header
with st.container():
  st.markdown("## Predictions of BTC-USD Price using SBi-LSTM and SBi-GRU")
  avs.add_vertical_space(2)
# --------------------------------------------------------------------------------------- #

# load dataset
dataset = pd.read_csv("dataset/BTC-USD.csv")
dataset = dataset[["Date", "Open", "High", "Low", "Close"]]
dataset = np.round(dataset,2)

# container dataset and visualization
col1, col2 = st.columns([0.4,0.6], gap="small")
with col1:
  st.info("Dataset of BTC-USD")
  st.dataframe(dataset, use_container_width=True)
with col2:
  st.info("Data Visualization")
  st.plotly_chart(
    line_plot(
      df=dataset, title="TimeSeries plot of BTC-USD Price",
    ), use_container_width=True
  )
  
# --------------------------------------------------------------------------------------- #

# split three columns
col1, col2, col3 = st.columns([0.2,0.2,0.6], gap="small")

# column of predictions of BTC-USD
with col1:
  st.info("Predictions of BTC-USD Price")
  form = st.form("my-form");
  algorithms = form.selectbox("Choose an algorithm", ("SBi-LSTM", "SBi-GRU"), index=None)
  submitted = form.form_submit_button(label="Submit", type="primary", use_container_width=False)

# column of evaluation models
with col2:
  st.info("Evaluation Model")
  st.caption("Execution time is about 5 minutes")
  
  # process prediction with 7 step
  # step 1 - choose a features 
  # step 2 - normalized min-max
  # step 3 - splitting data
  # step 4 - supervised learning
  # step 5 - model predictions
  # step 6 - denormalize dataset
  # step 7 - evaluation models
  if algorithms and submitted:
    # step 1 - choose a features
    data = dataset.filter(['Close'])
    data = data.values
    # ------------------------------------------------------------------------------------------------------------- #

    # step 2 - normalized min-max
    # normalize features
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled = scaler.fit_transform(np.array(data))
    # ------------------------------------------------------------------------------------------------------------- #

    # step 3 - splitting data
    train_data, test_data = train_test_split(scaled, train_size=0.80, test_size=0.20, shuffle=False)
    # ------------------------------------------------------------------------------------------------------------- #

    # step 4 - supervised learning
    look_back = 60
    x_train, y_train = create_dataset(look_back, train_data)
    x_test, y_test = create_dataset(look_back, test_data)

    # reshape input to be [samples, time steps, features]
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    # ------------------------------------------------------------------------------------------------------------- #

    # step 5 - model predictions
    # The LSTM architecture
    if algorithms == "SBi-LSTM":
      tf.keras.backend.clear_session()
      model = tf.keras.Sequential([
        tf.keras.layers.Bidirectional(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1))),
        tf.keras.layers.Dropout(0.05),
        tf.keras.layers.Bidirectional(LSTM(units=50, return_sequences=False)),
        tf.keras.layers.Dropout(0.05),
        tf.keras.layers.Dense(1)
      ])
    
    # The GRU-RNN architecture
    if algorithms == "SBi-GRU":
      tf.keras.backend.clear_session()
      model = tf.keras.Sequential([
        tf.keras.layers.Bidirectional(GRU(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1))),
        tf.keras.layers.Dropout(0.05),
        tf.keras.layers.Bidirectional(GRU(units=50, return_sequences=False)),
        tf.keras.layers.Dropout(0.05),
        tf.keras.layers.Dense(1)
      ])
    
    # compile models
    model.compile(optimizer='adamax', loss='mean_squared_error')
    
    # fit network
    with st.spinner('Training the model...'):
      history = model.fit(
        x_train, y_train,
        batch_size=16, epochs=50, verbose="auto", 
        validation_data=(x_test, y_test),
        use_multiprocessing=True, shuffle=False
      )
    
    # process predictions
    predictions = model.predict(x_test)
    # ------------------------------------------------------------------------------------------------------------- #

    # step 6 - denormalize dataset
    # inverse value test predictions
    y_close = scaler.inverse_transform(scaled)
    y_test = scaler.inverse_transform(y_test.reshape(-1, 1))
    predictions = scaler.inverse_transform(predictions.reshape(-1, 1))

    # shift y_test
    y_test_inv = np.empty_like(scaled)
    y_test_inv[:, :] = np.nan
    y_test_inv[(len(dataset) - y_test.shape[0]):len(dataset), :] = y_test

    # shift predictions
    predictions_inv = np.empty_like(scaled)
    predictions_inv[:, :] = np.nan
    predictions_inv[(len(dataset) - predictions.shape[0]):len(dataset), :] = predictions

    # concate date, close, y_test, y_pred
    date = dataset[["Date"]]
    y_close = pd.DataFrame(y_close, columns=["Close Price"])
    y_test_inv = pd.DataFrame(y_test_inv, columns=["Testing data"])
    predictions_inv = pd.DataFrame(predictions_inv, columns=["Prediction"])
    results = pd.concat([date, y_close, y_test_inv, predictions_inv], axis=1)
    # ------------------------------------------------------------------------------------------------------------- #

    # step 8 - evaluation models
    r = np.round(sc.mstats.pearsonr(y_test, predictions)[0],4)
    mape = np.round(mean_absolute_percentage_error(y_test, predictions)*100, 4)
    # ------------------------------------------------------------------------------------------------------------- #
    st.text(f"R    : {r}")
    st.text(f"MAPE : {mape}")

# column of results predictions
with col3:
  st.info("Results of Prediction BTC-USD")
  if algorithms and submitted:
    st.plotly_chart(
      line_plot(
        df=results, title="Results of Prediction Using "+str(algorithms)+" Algorithms",
      ),use_container_width=True
    )

    