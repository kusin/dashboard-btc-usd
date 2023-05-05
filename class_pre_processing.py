# declaration of library
import pandas as pd;
import numpy as np;
from sklearn.model_selection import train_test_split;
from sklearn.preprocessing import MinMaxScaler;

# define class pre-processing
class PreProcessing():

    # property class
    x = "";
    y = "";

    # method normalized-data
    def normalization(data):

        # normalize features
        scaler = MinMaxScaler(feature_range=(0, 1));
        scaled_data = scaler.fit_transform(np.array(data).reshape(-1,1));
        
        # return values
        return scaled_data;


    # method splitting-data
    def splitting(scaled_data, train_size, test_size):
        
        # split data train and test
        train_data, test_data = train_test_split(scaled_data, train_size=train_size, test_size=test_size, shuffle=False);
        
        # reteurn values
        return train_data, test_data;


    # method supervised learning
    def create_dataset(look_back, data):

         # declare variable X and Y
        dataX = []
        dataY = []
        
        # for loop for create supervised learning
        for i in range(look_back, len(data)):
            
            # insert value X and Y 
            dataX.append(data[i-look_back:i, 0])
            dataY.append(data[i, 0])
            
        # return value X and Y
        return np.array(dataX), np.array(dataY)
