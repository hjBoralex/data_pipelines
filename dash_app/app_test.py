# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 14:07:56 2022

@author: hermann.ngayap
"""
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
import dash
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.io as pio
pio.renderers.default='browser'
from colors import colors
import dis_warning
import sql_queries
from SetCatColor import SetCatColor
from sql_queries import (query_results_1, query_results_2, query_results_3, 
                         query_results_4, query_results_5, query_results_6, 
                         query_results_7, query_results_8, query_results_9, 
                         query_results_10, query_results_11, query_results_12)

#================ Dash App 
 
PLOTS_FONT_SIZE = 11
PLOTS_HEIGHT = 340  # For main graphs
SMALL_PLOTS_HEIGHT = 290  # For secondary graphs


#====Start
app = dash.Dash()

year_count = []
for year in query_results_3['année'].unique():
    year_count.append({'label':str(year),'value':year})
    
#Define tab_selected_style. Unfortunately cannot be defined in .css files
tab_height = 40
tab_style = {"height": tab_height, "line-height": tab_height, "padding": 0}
tab_selected_style = {
    "backgroundColor": colors["background3"],
    "color": colors["white"],
    "height": tab_height,
    "line-height": tab_height,
    "padding": 0,
    "font-weight": "bold",
}

app.layout = html.Div(
    className="screen-filler",
    children=[
        html.Div(
            style={
                "border-color": colors["darkgrey"],
                "border-style": "none none solid none",
                "border-width": "1px",
                "padding-bottom": "0.2%",
                "padding-left": "1.75%",
                "padding-top": "0.1%",
                },
            children=[
                html.H1(
                    children="BORALEX'S PORTFOLIO", style={"font-size": 18}
                        ),
                html.H2(
                    children='Real Time Market Exposure',  style={"font-size": 16}
                    )
                ]
            ), 
        html.Div( 
            style={ 
                "padding-top": "5px"
                },
            children=[
                html.Div(
                    children=[
                        html.Div(
                           # Central panel with metrics and graphs
                           className="central-panel0",
                           children=[
                               html.Div(
                                   # Period selection title panel
                                   className="central-panel1-title",
                                   children=["PORTFOLIO"],
                               ),
                               html.Div(
                                   # Date selection panel
                                   className="central-panel1",
                                   style={
                                       "marginBottom": 10,
                                   },#To separate Period selection and displayed tab
                                   
                                   ),
                               
                               #To start ploting GRAPHS
                               #Exposition per year
                               dcc.Graph(id='exposition_y',
                                         figure = {'data':[
                                         go.Bar(
                                         x=query_results_1['année'],
                                         y=query_results_1['yearly_exposition'],
                                         )], 
                                             'layout':go.Layout(dict(title='Exposition per year', 
                                                                xaxis = dict(gridcolor=colors['grid'], title='year'), 
                                                                yaxis = dict(gridcolor=colors['grid'], title='Production(MW/h)'),
                                                                paper_bgcolor = colors["background1"],
                                                                plot_bgcolor= colors["background1"],
                                                                font=dict(color=colors["text"], size=PLOTS_FONT_SIZE),
                                                                ))
                                             },
                                         style={'width': '40%', 'display': 'block', 'vertical-align': 'top'},
                                         ),
                               
                               dcc.Dropdown(id='drop_year_q',options=year_count,value=query_results_2['année'].min(),
                                            style=dict(width='30%',verticalAlign="left", display='block', )),
                               #Exposition per quarter
                               dcc.Graph(id='exposition_q', 
                                         figure = {'data':[
                                         go.Bar(
                                         x=query_results_2['quarters'],
                                         y=query_results_2['quarterly_exposition']
                                         )], 
                                             'layout':go.Layout(title='Exposition per quarter per year', 
                                                                xaxis = dict(gridcolor=colors['grid'], title='quarter'), 
                                                                yaxis = dict(gridcolor=colors['grid'], title='Production(MW/h)'),
                                                                paper_bgcolor = colors["background1"],
                                                                plot_bgcolor= colors["background1"],
                                                                font=dict(color=colors["text"], size=PLOTS_FONT_SIZE),
                                                                )
                                             },
                                         style={'width': '40%', 'display': 'block', 'vertical-align': 'top'} 
                                         ),
                               dcc.Dropdown(id='drop_year_m',options=year_count,value=query_results_3['année'].min(), 
                                            style=dict(width='30%', verticalAlign="right", display='block')),
                               #Exposition per month
                               dcc.Graph(id='exposition_m',
                                         figure = {'data':[
                                         go.Bar(
                                         x=query_results_3['months'],
                                         y=query_results_3['monthly_exposition']
                                         )], 
                                             'layout':go.Layout(title='Exposition per month per year', 
                                                                xaxis = dict(gridcolor=colors['grid'], title='months'), 
                                                                yaxis=dict(gridcolor=colors['grid'], title='Production(MW/h)'),
                                                                paper_bgcolor = colors["background1"],
                                                                plot_bgcolor= colors["background1"],
                                                                font=dict(color=colors["text"], size=PLOTS_FONT_SIZE),
                                                                )
                                             },
                                         style={'width': '40%', 'display': 'block', 'vertical-align': 'left'},
                                         ),
                               #Hedge per year
                               dcc.Graph(id='hedge_type_y',
                                         figure = {'data':[
                                         go.Bar(
                                         x=query_results_4['année'],
                                         y=query_results_4['hedge'],
                                         marker=dict(color=list(map(SetCatColor, query_results_4['type_contract'])))
                                         )], 
                                             'layout':go.Layout(title='hedge per type of contract per year', 
                                                                xaxis=dict(gridcolor=colors['grid'], title='year'), 
                                                                yaxis=dict(gridcolor=colors['grid'], title='Production(MW/h)'),
                                                                barmode='stack',
                                                                paper_bgcolor = colors["background1"],
                                                                plot_bgcolor= colors["background1"],
                                                                font=dict(color=colors["text"], size=PLOTS_FONT_SIZE),
                                                                showlegend=True,
                                                                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                                                                hovermode="closest")
                                             },
                                         style={'width': '40%', 'display': 'block', 'vertical-align': 'left'},
                                       ),
                               #Dropdown Hedge per quarter
                               dcc.Dropdown(id='drop_year_h_q',options=year_count,value=query_results_5['année'].min(), 
                                            style=dict(width='30%', verticalAlign="right", display='block')),
                               #Hedge per quarter
                               dcc.Graph(id='hedge_type_q',
                                         figure = {'data':[
                                         go.Bar(
                                         x=query_results_5['quarters'],
                                         y=query_results_5['hedge'],
                                         marker=dict(color=list(map(SetCatColor, query_results_5['type_contract'])))
                                         )], 
                                             'layout':go.Layout(title='hedge per type of contract per quarter', 
                                                                xaxis = dict(gridcolor=colors['grid'], title='year'), 
                                                                yaxis=dict(gridcolor=colors['grid'], title ='Production(MW/h)'),
                                                                barmode='stack',
                                                                paper_bgcolor = colors["background1"],
                                                                plot_bgcolor= colors["background1"],
                                                                font=dict(color=colors["text"], size=PLOTS_FONT_SIZE)
                                                                )},
                                         style={'width': '40%', 'display': 'block', 'vertical-align': 'left'},
                                         ),
                               #Dropdown Hedge per month
                               dcc.Dropdown(id='drop_year_h_m',options=year_count,value=query_results_6['année'].min(), 
                                            style=dict(width='30%', verticalAlign="right", display='block')),
                               #Hedge per month
                               dcc.Graph(id='hedge_type_m',
                                         figure = {'data':[
                                         go.Bar(
                                         x=query_results_6['months'],
                                         y=query_results_6['hedge'],
                                         marker=dict(color=list(map(SetCatColor, query_results_4['type_contract'])))
                                         )], 
                                             'layout':go.Layout(title='hedge per type of contract per month', 
                                                                xaxis = dict(gridcolor=colors['grid'], title='year', dtick=1), 
                                                                yaxis= dict(gridcolor=colors['grid'], title= 'Production(MW/h)'),
                                                                barmode='stack',
                                                                paper_bgcolor = colors["background1"],
                                                                plot_bgcolor= colors["background1"],
                                                                font=dict(color=colors["text"], size=PLOTS_FONT_SIZE)
                                                                )},
                                         style={'width': '40%', 'display': 'block', 'vertical-align': 'left'}
                                         ),
                               
                               #End of GRAPHS
                               ],
                           ),
                        ],
                    ),
                ],
            ),
       ],
    )

#=====Exposition per quarter callback
@app.callback(Output('exposition_q', 'figure'),
              [Input('drop_year_q', 'value')])

def update_figure_q(selected_year_q):
    filtered_df_q = query_results_2[query_results_2['année'] == selected_year_q]
    qtr = []
    for quarter in filtered_df_q['quarters'].unique():
        df_by_quarter = filtered_df_q[filtered_df_q['quarters'] == quarter]
        qtr.append(go.Bar(
            x=df_by_quarter['quarters'],
            y=df_by_quarter['quarterly_exposition']   
        ))

    return {
        'data': qtr,
        'layout': go.Layout(
            xaxis=dict(gridcolor=colors['grid'], title='quarter', dtick=1),
            yaxis=dict(gridcolor=colors['grid'], title='Production(MW/h)'),
            showlegend = False,
            paper_bgcolor = colors["background1"],
            plot_bgcolor= colors["background1"],
            font=dict(color=colors["text"], size=PLOTS_FONT_SIZE)
        )
    }

#=====Exposition per month callback
@app.callback(Output('exposition_m', 'figure'),
              [Input('drop_year_m', 'value')])

def update_figure_m(selected_year_m):
    filtered_df_m = query_results_3[query_results_3['année'] == selected_year_m]
    mth = []
    for month in filtered_df_m['months'].unique():
        df_by_month = filtered_df_m[filtered_df_m['months'] == month]
        mth.append(go.Bar(
            x=df_by_month['months'],
            y=df_by_month['monthly_exposition'],
               
        ))

    return {
        'data': mth,
        'layout': go.Layout(title='Exposition per month per year',
            xaxis=dict(gridcolor=colors['grid'], title='months', dtick=1),
            yaxis=dict(gridcolor=colors['grid'], title= 'Production(MW/h)'),
            showlegend = False,
            paper_bgcolor = colors["background1"],
            plot_bgcolor= colors["background1"],
            font=dict(color=colors["text"], size=PLOTS_FONT_SIZE)  
            
        )
    }
#=====Hedge per quarter callback
@app.callback(Output('hedge_type_q', 'figure'),
              [Input('drop_year_h_q', 'value')])

def update_figure_h_q(selected_year_h_q):
    filtered_df_h_q = query_results_5[query_results_5['année'] == selected_year_h_q]
    qtr_h = []
    for quarter in filtered_df_h_q['quarters'].unique():
        df_h_by_quarter = filtered_df_h_q[filtered_df_h_q['quarters'] == quarter]
        qtr_h.append(go.Bar(
            x=df_h_by_quarter['quarters'],
            y=df_h_by_quarter['hedge']
            
        ))

    return {
        'data': qtr_h,
        'layout': go.Layout(title='hedge per contract type per quarter',
            xaxis=dict(gridcolor=colors['grid'], title='quarter', dtick=1),
            yaxis=dict(gridcolor=colors['grid'], title= 'Production(MW/h)'),
            showlegend = True,
            barmode = "stack",
            paper_bgcolor = colors["background1"],
            plot_bgcolor= colors["background1"],
            font=dict(color=colors["text"], size=PLOTS_FONT_SIZE)
        )
    }

#=====Hedge per month callback
@app.callback(Output('hedge_type_m', 'figure'),
              [Input('drop_year_h_m', 'value')])

def update_figure_h_m(selected_year_h_m):
    filtered_df_h_m = query_results_6[query_results_6['année'] == selected_year_h_m]
    mth_h = []
    for month in filtered_df_h_m['months'].unique():
        df_h_by_month = filtered_df_h_m[filtered_df_h_m['months'] == month]
        mth_h.append(go.Bar(
            x=df_h_by_month['months'],
            y=df_h_by_month['hedge']
            
        ))

    return {
        'data': mth_h,
        'layout': go.Layout(title='hedge per contract type per month',
            xaxis=dict(gridcolor=colors['grid'], title='months', dtick=1),
            yaxis=dict(gridcolor=colors['grid'], title= 'Production(MW/h)'),
            showlegend = True,
            barmode = "stack",
            paper_bgcolor = colors["background1"],
            plot_bgcolor= colors["background1"],
            font=dict(color=colors["text"], size=PLOTS_FONT_SIZE)
        )
    }


if __name__ == '__main__':
    app.run_server()
#End