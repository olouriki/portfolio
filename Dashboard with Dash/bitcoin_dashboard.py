# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 18:23:07 2021

@author: louri
"""

import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output


#-------------DATA PREPARATION-------------

external_stylesheets = [dbc.themes.CYBORG]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df_btc = pd.read_csv('C:/Users/louri/OneDrive/Documents/BTC.csv')
df_btc['Year'] = df_btc['Date'].str[:4].astype(int)

df_btc_vader = pd.read_csv('btc_sentiment_distilbert_vader_2018.csv')

def add_percentage(df,col1, col2):
    new_var = col1+'_%'
    df[new_var] = (df[col1]/(df[col1]+df[col2]))*100
    return df

df_btc_vader = add_percentage(df_btc_vader, 'vader_res_neg', 'vader_res_neg')
df_btc_vader = add_percentage(df_btc_vader, 'vader_res_pos', 'vader_res_neg')
df_btc_vader['Year'] = df_btc_vader['date'].str[:4].astype(int)

fig_vader = make_subplots(specs=[[{'secondary_y':True}]])
fig_vader.add_trace(go.Scatter(x=df_btc_vader['date'], y = df_btc_vader['Low'], name="Low"), secondary_y=False)
fig_vader.add_trace(go.Scatter(x=df_btc_vader['date'], y = df_btc_vader['vader_res_neg'], name="vader_neg"), secondary_y=True)
fig_vader.add_trace(go.Scatter(x=df_btc_vader['date'], y = df_btc_vader['vader_res_pos'], name="vader_pos"), secondary_y=True)

fig_vader.update_layout(title='Prediction results', template="plotly_dark")
fig_vader.update_yaxes(title_text="Low", secondary_y=False)
fig_vader.update_yaxes(title_text="vader", secondary_y=True)

#-------------APP LAYOUT-------------------

app.layout = dbc.Fade(html.Div([
    
    
    dbc.Row(dbc.Col(html.H1('Bitcoin dashboard', style={'text-align':'center', 'background-color':'#073763', 'color':'white'}))),
    
    html.Br(),
    
    dbc.Row(
            [
                dbc.Col([dcc.Graph(id='interactive_scatter_plot'), 
                         dcc.Slider(id = 'Year_slider',
                            min = df_btc['Year'].min(),
                            max = df_btc['Year'].max(),
                            value = df_btc['Year'].min(),
                            marks = {str(year) : str(year) for year in df_btc['Year'].unique()},
                            step = None)], width=6),
            
                dbc.Col([dcc.Graph(id='graph_en_attente', figure=fig_vader)], width=6),    
            ]
            ),
    
    html.Br(),
    html.Br(),
    html.Br(),
    
    dbc.Row(dbc.Col(dcc.Dropdown(id='dropdown-session', className='btn-sm m-0 p-0 pl-0 pr-0',
                                           options=[{'label': i, 'value': i} for i in df_btc.columns[1:7]],
                                           value='High',
                                           style = {'color':'#111111','width': '40%', 'margin': 'auto', 'align-items': 'center', 'justify-content': 'center'}))),

    dbc.Row(dbc.Col(dcc.Graph(id='interactive_line_graph')))
    
    ] , style={'background-color':'#111111'}),timeout=1200)

#-------------APP CALLBACK-----------------

@app.callback(
    Output('interactive_scatter_plot', 'figure'),
    Input('Year_slider', 'value'))  
def update_figure(year):
    
    filtered_df = df_btc[df_btc['Year'] == year]
    filtered_df.dropna(inplace=True)
    
    fig = px.scatter(filtered_df, x = 'Open',
                     y = 'Close',
                     size='Volume',
                     color='High',
                     log_x=True)
    
    fig.update_layout(transition_duration=500, template="plotly_dark", title='Link between Bitcoin value at the begining and at the end of the day')
    return fig


@app.callback(
    Output('interactive_line_graph', 'figure'),
    Input('dropdown-session', 'value'))  
def update_figure(val):

    fig = go.Figure()
    fig = fig.add_trace(go.Scatter(x = df_btc['Date'],
                     y = df_btc[val],
                     ))
    fig.update_layout(title=val+' value evolution', template="plotly_dark")
    
    fig.update_layout(xaxis=dict(rangeselector=dict(
                        buttons=list([
                                dict(count=1,
                                     label="1m",
                                     step="month",
                                     stepmode="backward",
                                     templateitemname='ggplot2',
                                     visible=False),
                                dict(count=6,
                                     label="6m",
                                     step="month",
                                     stepmode="backward",
                                     visible=False),
                                dict(count=1,
                                     label="YTD",
                                     step="year",
                                     stepmode="todate",
                                     visible=False),
                                dict(count=1,
                                     label="1y",
                                     step="year",
                                     stepmode="backward",
                                     visible=False),
                                dict(step="all", visible=False)
                            ])
                        ),rangeslider=dict(visible=True), type="date"))
    
    return fig


#-------------Launch server-----------------

if __name__=='__main__':
    
    app.run_server(debug=True)
