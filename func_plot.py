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
def plot_multiple_line(data, list):
    
    # define a new figure
    fig = go.Figure();

    # add plot with loop
    for y in list:
        fig.add_trace(
            go.Scatter(
                x=data.index, y=data[y], name=y, mode="lines"
            )
        );

    # update plot
    fig.update_layout(
        xaxis_title="Year", yaxis_title="Price USD",
        legend=dict(
            title=None,
            orientation="h",
            x=0.5, xanchor="center",
            y=1, yanchor="bottom"
        )
    );
    
    # return value
    return fig;

# func plot grouped bar with plotly graph objects
def plot_grouped_bar(data, list):

    # define a new figure
    fig = go.Figure();

    # add plot with loop
    for y in list:
        fig.add_trace(
            go.Bar(
                x=data.index, y=data[y], name=y, text=data[y], textposition='auto'
            )
        );
    
    # update plot
    fig.update_layout(barmode='group');

    # return value
    return fig;

def func_agg_year(data, nm_start, nm_end):

    data = data.iloc[(data.index >= nm_start) & (data.index <= nm_end)];
    data = data.resample("M").sum();

    # return value
    return data;