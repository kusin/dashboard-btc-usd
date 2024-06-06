# library manipulation dataset
import pandas as pd

# library manipulation array
import numpy as np

# import library streamlit
import streamlit as st
from streamlit_extras import add_vertical_space as avs 

# library data visualization
import plotly.express as px
import plotly.graph_objects as go

# library data preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# library deep learning
import tensorflow as tf
from keras.utils import Sequence
from keras.models import Sequential
from keras.layers import SimpleRNN
from keras.layers import LSTM
from keras.layers import GRU
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import TimeDistributed
from keras.layers import Bidirectional
from keras.optimizers import Adam, Adamax, RMSprop, SGD

# library evaluations model
from math import sqrt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error

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
def line_plot(df):

  # create a plot
  fig = go.Figure()
        
  # add lineplot with graph object
  for column in df.columns[1:]:
    fig.add_trace(
      go.Scatter(x=df["Date"],y=df[column], mode='lines', name=column)
    )
        
  # # add colors on lineplot
  # colorscale = px.colors.diverging.Portland_r
  # for i, trace in enumerate(fig.data):
  #   trace.update(line=dict(color=colorscale[i]))

  # update layout lineplot
  fig.update_layout(
    title = "Time series plot of BTC-USD price",
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
        
    # insert value X and Y 
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
  st.plotly_chart(line_plot(dataset), use_container_width=True)