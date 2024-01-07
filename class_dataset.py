# library ui-dashboard
import streamlit as st;

# library manipulation dataset
import pandas as pd;

# library manipulation array
import numpy as np;

# define class dataset
class dataset:
    
    # method read dataset
    @staticmethod
    def get_dataset():
        df = pd.read_csv("dataset/BTC-USD.csv")
        return df