# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 15:06:59 2022
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
                         query_results_10, query_results_11, query_results_12, 
                         query_results_13, query_results_14, query_results_15)

from tabs.MtM_tab import MtM_layout
from images.images import boralex_logo
from tabs.ppa_fixed_exp_tab import ppa_fixed_exp_layout
#================ Dash App
BAR_H_WIDTH = 2 
PLOTS_FONT_SIZE = 11
PLOTS_HEIGHT = 340  # For main graphs
SMALL_PLOTS_HEIGHT = 290  # For secondary graphs
#====Start
app = dash.Dash()

years = ['2022',' 2023', '2024', '2025', '2026', '2027', '2028']
quarters = ['Q1', 'Q2', 'Q13', 'Q4']
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug',' sep', 'oct', 'nov', 'dec']

year_count = []
for year in query_results_3['année'].unique():
    year_count.append({'label':str(year),'value':year})
    
# Define tab_selected_style. Unfortunately cannot be defined in .css files
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
                "padding-left": "1.75%",#1.75%
                "padding-top": "0.1%",
                },
            children=[
                html.H1(
                    children="BORALEX'S PORTFOLIO", style={"font-size": 18, 'textAlign': 'center', 'color': colors['blue_blx']}
                        ),
                html.H2(
                    children='Real Time Market Exposure',  style={"font-size": 16, 'textAlign': 'center', 'color': colors['blue_blx']},
                    ),
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
                          
                           className="central-panel0",
                           children=[
                               html.Div(
                                  
                                   className="central-panel1-title",
                                   children=["PORTFOLIO MANAGEMENT STRATEGIES"]   
                               ),
                               
                               html.Div(
                                   className="central-panel1",
                                   children=[
                                       #
                                       dcc.Loading(
                                           children=[
                                               dcc.Tabs(
                                               id="tabsID",
                                               className="custom-tabs",
                                                colors={
                                                    "background": "#234253",
                                                    "border": "#3C3F47",
                                                    "primary": colors[
                                                        "solar_blx"
                                                    ],
                                                },
                                                style={
                                                    "font-size": 12,
                                                    "height": 50,
                                                },
                                                #
                                                children=[
                                                    dcc.Tab(
                                                        html.Div(
                                                            children=[
                                                                html.Div(
                                                                    style={
                                                                        "display": "inline-block",
                                                                        "vertical-align": "top",
                                                                        "width": "33%",
                                                                        },
                                                                    children=[
                                                                        html.H2(
                                                                            children="Production",
                                                                            style={
                                                                                "font-size": 14,
                                                                                "margin-bottom": "0em",
                                                                                "margin-top": "1em",
                                                                                },
                                                                            ),
                                                                        #prod per year
                                                                        dcc.Graph(id='prod_y',
                                                                                  figure = {'data':[
                                                                                      go.Bar(
                                                                                          x=query_results_10['année'],
                                                                                          y=query_results_10['prod_per_year'],
                                                                                          marker=dict(color=colors['l_green']),
                                                                                          )], 
                                                                                      'layout':go.Layout(dict(title='Prod/year', 
                                                                                                              xaxis = dict(gridcolor=colors['grid'], title='year', dtick=1, tickangle = 45), 
                                                                                                              yaxis = dict(gridcolor=colors['grid'], title='GWh'),
                                                                                                              paper_bgcolor = colors["background1"],
                                                                                                              plot_bgcolor= colors["background1"],
                                                                                                              font=dict(color=colors["text"], size=PLOTS_FONT_SIZE),
                                                                                                              showlegend=False,
                                                                                                              legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                                                                                                              hovermode="x unified"
                                                                                                              ))
                                                                                      },
                                                                                  style={'width': '100%', 'display': 'inline-block', 'vertical-align': 'top'},
                                                                                  ),
                                                                        #Dropdown prod per quarter 
                                                                        dcc.Dropdown(id='drop_year_p_q',options=year_count,value=query_results_10['année'].min(),
                                                                                     style=dict(width='40%',verticalAlign="left", display='inline-block')),
                                                                        #prod per quarter
                                                                        dcc.Graph(id='prod_q', 
                                                                                  figure = {'data':[
                                                                                      go.Bar(
                                                                                          x=query_results_11['quarters'], #quarters
                                                                                          y=query_results_11['prod_per_quarter'],
                                                                                          marker=dict(color=colors['l_green']),
                                                                                          )], 
                                                                                      'layout':go.Layout(title='Prod/quarter/year', 
                                                                                                         xaxis = dict(gridcolor=colors['grid'], title='quarter'), 
                                                                                                         yaxis = dict(gridcolor=colors['grid'], title='GWh'),
                                                                                                         paper_bgcolor = colors["background1"],
                                                                                                         plot_bgcolor= colors["background1"],
                                                                                                         font=dict(color=colors["text"], size=PLOTS_FONT_SIZE),
                                                                                                         showlegend=False,
                                                                                                         legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                                                                                                         hovermode="x unified",
                                                                                                         )
                                                                                      },
                                                                                  style={'width': '100%', 'display': 'block', 'vertical-align': 'top'} 
                                                                                  ),
                                                                        #Dropdown prod per month
                                                                        dcc.Dropdown(id='drop_year_p_m',options=year_count,value=query_results_3['année'].min(), 
                                                                                     style=dict(width='40%', verticalAlign="left", display='inline-block')),
                                                                        #Prod per month
                                                                        dcc.Graph(id='prod_m',
                                                                                  figure = {'data':[
                                                                                      go.Bar(
                                                                                          x=query_results_12['months'],
                                                                                          y=query_results_12['prod_per_month'],
                                                                                          marker=dict(color=colors['l_green']),
                                                                                          )], 
                                                                                      'layout':go.Layout(title='Prod/month/year', 
                                                                                                         xaxis = dict(gridcolor=colors['grid'], title='months', tickangle = 45), 
                                                                                                         yaxis=dict(gridcolor=colors['grid'], title='GWh'),
                                                                                                         paper_bgcolor = colors["background1"],
                                                                                                         plot_bgcolor= colors["background1"],
                                                                                                         font=dict(color=colors["text"], size=PLOTS_FONT_SIZE),
                                                                                                         showlegend=False,
                                                                                                         legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                                                                                                         hovermode="x unified"
                                                                                                         )
                                                                                      }, 
                                                                                  style={'width': '100%', 'display': 'inline-block', 'vertical-align': 'top'}
                                                                                  ),
                                                                        ],
                                                                    ),
                                                                html.Div(
                                                                    style={
                                                                        "display": "inline-block",
                                                                        "margin-top": "0px",
                                                                        "width": "33%",
                                                                        },
                                                                    children=[
                                                                        html.H2(
                                                                            children="Prod/Hedge/Exposition",
                                                                            style={
                                                                                "font-size": 14,
                                                                                "margin-bottom": "0em",
                                                                                "margin-top": "1em",
                                                                                },
                                                                            ),
                                                                        #Hedge per year
                                                                        dcc.Graph(id='hedge_type_y',
                                                                                  figure = {'data':[
                                                             
                                                                                      go.Bar(
                                                                                          name='HCR', 
                                                                                          x=years, 
                                                                                          y=query_results_7['HCR_per_year'],
                                                                                          opacity=1,
                                                                                          marker=dict(color=colors['white']),
                                                                                          marker_line=dict(width= BAR_H_WIDTH, color=colors['bar_h_color']),
                                                                                          #textposition='outside',
                                                                                          #textfont = dict(family="Times", size= 10, color= colors["white"]),
                                                                                          ),
                                                                                      go.Bar(
                                                                                          name='PPA', 
                                                                                          x=years, 
                                                                                          y=query_results_4.loc[query_results_4['type_contract'] == 'PPA', 'hedge'],
                                                                                          opacity=1,
                                                                                          marker=dict(color=colors['ppa']),
                                                                                          marker_line=dict(width= BAR_H_WIDTH, color=colors['bar_h_color'])
                                                                                          ),
                                                                                      go.Bar(
                                                                                          name='OA', 
                                                                                          x=years, 
                                                                                          y=query_results_4.loc[query_results_4['type_contract'] == 'OA', 'hedge'],
                                                                                          opacity=0.2,
                                                                                          marker=dict(color=colors['oa']),
                                                                                          marker_line=dict(width= BAR_H_WIDTH, color=colors['bar_h_color'])
                                                                                          ),
                                                                                      go.Bar(
                                                                                          name='CR', 
                                                                                          x=years, 
                                                                                          y=query_results_4.loc[query_results_4['type_contract'] == 'CR', 'hedge'],
                                                                                          opacity=0.4,
                                                                                          marker=dict(color=colors['cr']),
                                                                                          marker_line=dict(width= BAR_H_WIDTH, color=colors['bar_h_color'])
                                                                                          ),
                                                        
                                                                                     go.Bar(
                                                                                         name='Prod', 
                                                                                         x=years, 
                                                                                         y=query_results_10['prod_per_year'],
                                                                                         opacity=0.09,
                                                                                         marker=dict(color=colors['e_white']),                             
                                                                                         marker_line=dict(width= BAR_H_WIDTH, color=colors['bar_h_color']) 
                                                                                         ), 
                                                                                     ], 
                                                                                      'layout':go.Layout(title='',
                                                                                                         annotations=[dict(x=years[0], y=(query_results_10.iloc[0, 1])+20, text=query_results_7.iloc[0, 1], showarrow=False, align='center', 
                                                                                                                           font=dict(size=8)), 
                                                                                                                      dict(x=years[1], y=(query_results_10.iloc[1, 1])+20,text=query_results_7.iloc[1, 1], showarrow=False, align='center', font=dict(size=8)),
                                                                                                                      dict(x=years[2], y=(query_results_10.iloc[2, 1])+20,text=query_results_7.iloc[2, 1], showarrow=False, align='center', font=dict(size=8)),
                                                                                                                      dict(x=years[3], y=(query_results_10.iloc[3, 1])+20,text=query_results_7.iloc[3, 1], showarrow=False, align='center', font=dict(size=8)),
                                                                                                                      dict(x=years[4], y=(query_results_10.iloc[4, 1])+20,text=query_results_7.iloc[4, 1], showarrow=False, align='center', font=dict(size=8)),
                                                                                                                      dict(x=years[5], y=(query_results_10.iloc[5, 1])+20,text=query_results_7.iloc[5, 1], showarrow=False, align='center', font=dict(size=8)),
                                                                                                                      dict(x=years[6], y=(query_results_10.iloc[6, 1])+20,text=query_results_7.iloc[6, 1], showarrow=False, align='center', font=dict(size=8))],
                                                                                                         xaxis=dict(gridcolor=colors['grid'], title='year', dtick=1, tickangle = 45), 
                                                                                                         yaxis=dict(gridcolor=colors['grid'], title='GWh', side='left'),
                                                                                                         yaxis2=dict(gridcolor=colors['grid'], title='GWh', side='right', showline=True),
                                                                                                         barmode='overlay',
                                                                                                         paper_bgcolor = colors["background1"],
                                                                                                         plot_bgcolor= colors["background1"],
                                                                                                         font=dict(color=colors["text"], size=PLOTS_FONT_SIZE),
                                                                                                         showlegend=True,
                                                                                                         legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                                                                                                         hovermode="x unified")
                                                                                      },
                                                                                  style={'width': '100%', 'display': 'inline-block', 'vertical-align': 'top'},
                                                                                  ),
                                                                        #Dropdown Hedge per quarter
                                                                        dcc.Dropdown(id='drop_year_h_q', options=year_count, value=query_results_5['année'].min(), 
                                                                                     style=dict(width='40%', verticalAlign="left", display='inline-block')),
                                                                        #Hedge per quarter
                                                                        dcc.Graph(id='hedge_type_q',
                                                                                  figure = {'data':[
                                                             
                                                                                      go.Bar(
                                                                                          name='HCR', 
                                                                                          x=query_results_8['quarters'], 
                                                                                          y=query_results_8['HCR_per_quarter'],
                                                                                          opacity=1,
                                                                                          marker=dict(color=colors['white']),
                                                                                          marker_line=dict(width= BAR_H_WIDTH, color=colors['bar_h_color']),
                                                                                          textposition = "outside",
                                                                                          textfont = dict(family="Times", size= 10, color= colors["white"]),
                                                                                          ), 
                                                                                      go.Bar(
                                                                                          name='PPA',
                                                                                          x=query_results_5['quarters'],
                                                                                          y=query_results_5.loc[query_results_5['type_contract']=='PPA', 'hedge'],
                                                                                          opacity=1,
                                                                                          marker=dict(color=colors['ppa']),
                                                                                          marker_line=dict(width= BAR_H_WIDTH, color=colors['bar_h_color'])
                                                                                          ),
                                                                                      go.Bar(
                                                                                          name='OA',
                                                                                          x=query_results_5['quarters'],
                                                                                          y=query_results_5.loc[query_results_5['type_contract']=='OA', 'hedge'],
                                                                                          opacity=0.4,
                                                                                          marker=dict(color=colors['oa']),
                                                                                          marker_line=dict(width= BAR_H_WIDTH, color=colors['bar_h_color'])
                                                                                          ),
                                                                                      go.Bar(
                                                                                          name='CR',
                                                                                          x=query_results_5['quarters'],
                                                                                          y=query_results_5.loc[query_results_5['type_contract']=='CR', 'hedge'],
                                                                                          opacity=0.25,
                                                                                          marker=dict(color=colors['cr']),
                                                                                          marker_line=dict(width= BAR_H_WIDTH, color=colors['bar_h_color'])
                                                                                          ),
                                                         
                                                                                      go.Bar(
                                                                                          name='Prod', 
                                                                                          x=query_results_11['quarters'],
                                                                                          y=query_results_11['prod_per_quarter'],
                                                                                          opacity=0.1,
                                                                                          marker=dict(color=colors['e_white']),
                                                                                          marker_line=dict(width= BAR_H_WIDTH, color=colors['bar_h_color']),
                                                            
                                                                                         ),
                                                                                      ],
                                                         
                                                             
                                                                                      'layout':go.Layout(title='Hedge/contract type/quarter', 
                                                                                                         xaxis=dict(gridcolor=colors['grid'], title='year'), 
                                                                                                         yaxis=dict(gridcolor=colors['grid'], title ='GWh', side='left'),
                                                                                                         yaxis2=dict(gridcolor=colors['grid'], title ='GWh', side='right', showline=True),
                                                                                                         barmode='overlay',
                                                                                                         paper_bgcolor = colors["background1"],
                                                                                                         plot_bgcolor= colors["background1"],
                                                                                                         font=dict(color=colors["text"], size=PLOTS_FONT_SIZE),
                                                                                                         showlegend=True,
                                                                                                         legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                                                                                                         hovermode="x unified",
                                                                                                         ),
                                                                                      }, 
                                                                                  style={'width': '100%', 'display': 'inline-block', 'vertical-align': 'top'},
                                                                                  ),
                                                             
                                                                        #Dropdown Hedge per month
                                                                        dcc.Dropdown(id='drop_year_h_m',options=year_count,value=query_results_6['année'].min(), 
                                                                             style=dict(width='40%', verticalAlign="left", display='inline-block')),
                                                                        #Hedge per month
                                                                        dcc.Graph(id='hedge_type_m',
                                                                                  figure = {'data':[
                                                                                      go.Bar(
                                                                                          name="d1",   
                                                                                          x=query_results_6['months'],
                                                                                          y=query_results_6.loc[query_results_6['type_contract'] == 'OA']),
                                                                                      go.Bar(
                                                                                          name="d2",
                                                                                          x=query_results_6['months'],
                                                                                          y=query_results_6.loc[query_results_6['type_contract'] == 'CR']), 
                                                                                      go.Bar(
                                                                                          name="d2",
                                                                                          x=query_results_6['months'],
                                                                                          y=query_results_6.loc[query_results_6['type_contract'] == 'PPA']),
                                                                                      ],
                                                                                      
                                                                                      'layout':go.Layout(title='Hedge/contract type/month', 
                                                                                                         xaxis = dict(gridcolor=colors['grid'], title='year', dtick=1, tickangle = 45), 
                                                                                                         yaxis= dict(gridcolor=colors['grid'], title= 'GWh'),
                                                                                                         barmode='stack',
                                                                                                         paper_bgcolor = colors["background1"],
                                                                                                         plot_bgcolor= colors["background1"],
                                                                                                         font=dict(color=colors["text"], size=PLOTS_FONT_SIZE)
                                                                                                         )},
                                                                                  style={'width': '100%', 'display': 'block', 'vertical-align': 'top'}
                                                                                  ),
                                                                        ],   
                                                                    ),
                                                                html.Div(
                                                                    style={
                                                                        "display": "inline-block",
                                                                        "vertical-align": "top",
                                                                        "width": "33%",
                                                                        }, 
                                                                    children=[
                                                                        html.H2(
                                                                            children="Market Exposure",
                                                                            style={
                                                                                "font-size": 14,
                                                                                "margin-bottom": "0em",
                                                                                "margin-top": "1em",
                                                                                },
                                                                            ),
                                                                        #Exposition per year
                                                                        dcc.Graph(id='exposition_y',
                                                                                  figure = {'data':[
                                                                                      go.Bar(
                                                                                          x=query_results_1['année'],
                                                                                          y=query_results_1['yearly_exposition'],
                                                                                          marker=dict(color=colors['red']),
                                                                                          )], 
                                                                                      'layout':go.Layout(dict(title='Exposition/year', 
                                                                                                              xaxis = dict(gridcolor=colors['grid'], title='year', dtick=1, tickangle = 45), 
                                                                                                              yaxis = dict(gridcolor=colors['grid'], title='GWh'),
                                                                                                              paper_bgcolor = colors["background1"],
                                                                                                              plot_bgcolor= colors["background1"],
                                                                                                              font=dict(color=colors["text"], size=PLOTS_FONT_SIZE),
                                                                                                              showlegend=False,
                                                                                                              legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                                                                                                              hovermode="x unified"
                                                                                                              ))
                                                                                      },
                                                                                  style={'width': '100%', 'display': 'inline-block', 'vertical-align': 'top'},
                                                                                  ),
                                                                        dcc.Dropdown(id='drop_year_q',options=year_count,value=query_results_2['année'].min(),
                                                                                     style=dict(width='40%',verticalAlign="left", display='inline-block', )),
                                                                        #Exposition per quarter
                                                                        dcc.Graph(id='exposition_q', 
                                                                                  figure = {'data':[
                                                                                      go.Bar(
                                                                                          x=query_results_2['quarters'],
                                                                                          y=query_results_2['quarterly_exposition'],
                                                                                          #marker=dict(color=colors['red']),
                                                                                          )], 
                                                                                      'layout':go.Layout(title='Exposition/quarter/year', 
                                                                                                         xaxis = dict(gridcolor=colors['grid'], title='quarter'), 
                                                                                                         yaxis = dict(gridcolor=colors['grid'], title='GWh'),
                                                                                                         paper_bgcolor = colors["background1"],
                                                                                                         plot_bgcolor= colors["background1"],
                                                                                                         font=dict(color=colors["text"], size=PLOTS_FONT_SIZE),
                                                                                                         hovermode="x unified",
                                                                                                         showlegend=False,
                                                                                                         legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                                                                                                         )
                                                                                      },
                                                                                  style={'width': '100%', 'display': 'inline-block', 'vertical-align': 'top'} 
                                                                                  ),
                                                                        #Dropdown exposition per quarter
                                                                        dcc.Dropdown(id='drop_year_m',options=year_count,value=query_results_3['année'].min(), 
                                                                                     style=dict(width='40%', verticalAlign="right", display='inline-block')),
                                                                        #Exposition per month
                                                                        dcc.Graph(id='exposition_m',
                                                                                  figure = {'data':[
                                                                                      go.Bar(
                                                                                          x=query_results_3['months'],
                                                                                          y=query_results_3['monthly_exposition'],
                                                                                          #marker=dict(color=colors['red']),
                                                                                          )], 
                                                                                      'layout':go.Layout(title='Exposition/month/year', 
                                                                                                         xaxis = dict(gridcolor=colors['grid'], title='months', tickangle = 45), 
                                                                                                         yaxis=dict(gridcolor=colors['grid'], title='GWh'),
                                                                                                         paper_bgcolor = colors["background1"],
                                                                                                         plot_bgcolor= colors["background1"],
                                                                                                         font=dict(color=colors["text"], size=PLOTS_FONT_SIZE),
                                                                                                         hovermode="x unified",
                                                                                                         showlegend=False,
                                                                                                         legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                                                                                                         ),
                                                                                      }, 
                                                                                  style={'width': '100%', 'display': 'inline-block', 'vertical-align': 'top'}
                                                                                  ),
                                                                        ], 
                                                                    ),
                                                                ],
                                                            ),
                                                        className="custom-tab",
                                                        label="Prod & Exposure",
                                                        selected_style=tab_selected_style,
                                                        style=tab_style,
                                                        ),
                                                    
                                                    dcc.Tab(
                                                        children=[
                                                                ppa_fixed_exp_layout
                                                            ],
                                                        className="custom-tab",
                                                            label="PPA Hedge",
                                                            selected_style=tab_selected_style,
                                                            style=tab_style,
                                                        ),
                                                    
                                                    dcc.Tab(
                                                        children=[
                                                                MtM_layout
                                                            ],
                                                        className="custom-tab",
                                                            label="Mark to Market",
                                                            selected_style=tab_selected_style,
                                                            style=tab_style,
                                                        ),
                                                    
                                                   ],
                                                )
                                               
                                               ],
                                           )
                                       ],
                                   ),
                              ] 
                           ),
                        ]
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
            y=df_by_quarter['quarterly_exposition'],
            marker=dict(color=colors['red']),
        ))

    return {
        'data': qtr,
        'layout': go.Layout(
            title='Exposition/quarter/year',
            xaxis=dict(gridcolor=colors['grid'], title='quarter', dtick=1),
            yaxis=dict(gridcolor=colors['grid'], title='GWh'),
            showlegend = False,
            paper_bgcolor = colors["background1"],
            plot_bgcolor= colors["background1"],
            font=dict(color=colors["text"], size=PLOTS_FONT_SIZE),
            hovermode="x unified",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            
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
            marker=dict(color=colors['red']),
               
        ))

    return {
        'data': mth,
        'layout': go.Layout(title='Exposition/month/year',
            xaxis=dict(gridcolor=colors['grid'], title='months', dtick=1, tickangle = 45),
            yaxis=dict(gridcolor=colors['grid'], title= 'GWh'),
            showlegend = False,
            paper_bgcolor = colors["background1"],
            plot_bgcolor= colors["background1"],
            font=dict(color=colors["text"], size=PLOTS_FONT_SIZE),
            hovermode="x unified",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            
        )
    }

#=====Prod per quarter callback
@app.callback(Output('prod_q', 'figure'),
              [Input('drop_year_p_q', 'value')])

def update_figure_p_q(selected_year_p_q):
    filtered_df_p_q = query_results_11[query_results_11['année'] == selected_year_p_q]
    qtr_p = []
    for quarter in filtered_df_p_q['quarters'].unique():
        df_p_by_quarter = filtered_df_p_q[filtered_df_p_q['quarters'] == quarter]
        qtr_p.append(go.Bar(
            x=df_p_by_quarter['quarters'],
            y=df_p_by_quarter['prod_per_quarter'],
            marker=dict(color=colors['l_green'])
            
        ))

    return {
        'data': qtr_p,
        'layout': go.Layout(title='Prod/quarter/year',
            xaxis=dict(gridcolor=colors['grid'], title='quarter', dtick=1),
            yaxis=dict(gridcolor=colors['grid'], title= 'GWh'),
            showlegend = False,
            paper_bgcolor = colors["background1"],
            plot_bgcolor= colors["background1"],
            font=dict(color=colors["text"], size=PLOTS_FONT_SIZE),
            hovermode="x unified",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        )
    }
#=====Prod per month callback
@app.callback(Output('prod_m', 'figure'),
              [Input('drop_year_p_m', 'value')])

def update_figure_p_m(selected_year_p_m):
    filtered_df_p_m = query_results_12[query_results_12['année'] == selected_year_p_m]
    mth_p = []
    for month in filtered_df_p_m['months'].unique():
        df_p_by_month = filtered_df_p_m[filtered_df_p_m['months'] == month]
        mth_p.append(go.Bar(
            x=df_p_by_month['months'],
            y=df_p_by_month['prod_per_month'],
            marker=dict(color=colors['l_green']),
               
        ))

    return {
        'data': mth_p,
        'layout': go.Layout(title='Prod/month/year',
            xaxis=dict(gridcolor=colors['grid'], title='months', dtick=1, tickangle = 45),
            yaxis=dict(gridcolor=colors['grid'], title= 'GWh'),
            showlegend = False,
            paper_bgcolor = colors["background1"],
            plot_bgcolor= colors["background1"],
            font=dict(color=colors["text"], size=PLOTS_FONT_SIZE),
            hovermode="x unified",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            
        )
    }

#=====Hedge per quarter callback
@app.callback(Output('hedge_type_q', 'figure'),
              [Input('drop_year_h_q', 'value')])

def update_figure_h_q(selected_year_h_q):
    filtered_df_h_q = query_results_5[query_results_5['année'] == selected_year_h_q]
    filtered_df_p_q = query_results_11[query_results_11['année'] == selected_year_h_q]
    qtr_h_ppa = []
    qtr_h_oa = []
    qtr_h_cr = []
    for quarter in filtered_df_h_q['quarters'].unique():
        df_h_by_quarter = filtered_df_h_q[filtered_df_h_q['quarters'] == quarter]
        qtr_h_ppa.append(go.Bar(
            x=df_h_by_quarter['quarters'],
            y=df_h_by_quarter.loc[df_h_by_quarter['type_contract']=='PPA', 'hedge']),
            opacity=1,
            marker=dict(color=colors['ppa']),
            marker_line=dict(width= BAR_H_WIDTH, color=colors['bar_h_color'])
            ),
        qtr_h_oa.append(go.Bar(
            x=df_h_by_quarter['quarters'],
            y=df_h_by_quarter.loc[df_h_by_quarter['type_contract']=='OA', 'hedge']),
            opacity=1,
            marker=dict(color=colors['oa']),
            marker_line=dict(width= BAR_H_WIDTH, color=colors['bar_h_color'])
            ),
        qtr_h_cr.append(go.Bar(
            x=df_h_by_quarter['quarters'],
            y=df_h_by_quarter.loc[df_h_by_quarter['type_contract']=='CR', 'hedge']),
            opacity=1,
            marker=dict(color=colors['cr']),
            marker_line=dict(width= BAR_H_WIDTH, color=colors['bar_h_color'])
            ),
    for quarter in filtered_df_p_q['quarters'].unique():
        df_p_by_quarter = filtered_df_p_q[filtered_df_p_q['quarters'] == quarter]
        qtr_p = []
        qtr_p.append(go.Bar(
            x=df_p_by_quarter['quarters'],
            y=df_p_by_quarter['prod_per_quarter'],
            marker=dict(color=colors['l_green'])),)
            
    return {
        'data': (qtr_h_ppa, qtr_h_oa, qtr_h_cr, qtr_p),
        'layout': go.Layout(title='Hedge/contract type/quarter',
            xaxis=dict(gridcolor=colors['grid'], title='quarter', dtick=1),
            yaxis=dict(gridcolor=colors['grid'], title= 'GWh', side='left'),
            yaxis2=dict(gridcolor=colors['grid'], title= 'GWh', side='right', showline=True),
            showlegend = False,
            barmode = "overlay",
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
            y=df_h_by_month['hedge'],            
        ))

    return {
        'data': mth_h,
        'layout': go.Layout(title='Hedge/contract type/month',
            xaxis=dict(gridcolor=colors['grid'], title='months', dtick=1, tickangle = 45),
            yaxis=dict(gridcolor=colors['grid'], title= 'GWh'),
            showlegend = False,
            barmode = "stack",
            paper_bgcolor = colors["background1"],
            plot_bgcolor= colors["background1"],
            font=dict(color=colors["text"], size=PLOTS_FONT_SIZE)
        )
    }


if __name__ == '__main__':
    app.run_server()
