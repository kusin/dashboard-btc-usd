# declaration of library
import pandas as pd;
import numpy as np;
import plotly.express as px;
import plotly.graph_objects as go;
from matplotlib import pyplot as plt


# define class visualization
class visualization:

    # property visualization
    x = "";
    y = "";

    def time_series1(dataX, dataY, title, color):
        
        # define a new figure
        fig = go.Figure();

        # add plot time series
        fig.add_trace(
            go.Scatter(
                x=dataX, y=dataY, mode='lines', line_color=color,
            )
        );

        # update plot
        fig.update_layout(title_text=title);

        # return values
        return fig;

    def time_series2(dataX, dataY, color):
        
        # define a new figure
        fig = plt.figure(figsize=(20,6));

        # make a time series plot
        plt.plot(dataX, dataY, color=color, label="label", linewidth=2);

        # make are labels
        plt.legend(loc="best");
        plt.grid(True);

        # return values
        return fig;
    