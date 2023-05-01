# declaration of library
import pandas as pd;
import numpy as np;


# define class dataset
class dataset:

    # method read dataset
    def get_dataset():
        
        # call dataset
        df = pd.read_csv("dataset/btc-usd.csv", parse_dates=["Date"]);

        # return values
        return df;