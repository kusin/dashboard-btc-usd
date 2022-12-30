# library ui-dashboard
import streamlit as st;

# library manipulation dataset
import pandas as pd;

# library manipulation array
import numpy as np;

# library data visualization
import plotly.express as px;
import plotly.graph_objects as go;

# func plot line with plotly graph objects
def plot_multiple_line(data, value_x, value_y):
    
    # define a new figure
    fig = go.Figure();

    # add plot with loop
    for list_y in value_y:
        fig.add_trace(
            go.Scatter(
                x=data[value_x], y=data[list_y], name=list_y, mode="lines"
            )
        );

    # update plot
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Price USD",
        legend=dict(
            title=None,
            orientation="h",
            x=0.5, xanchor="center",
            y=1, yanchor="bottom"
        )
    );
    
    # return value
    return fig;