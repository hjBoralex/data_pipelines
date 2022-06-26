# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 17:52:09 2022

@author: hermann.ngayap
"""


import plotly.graph_objs as go
import dash
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

from colors import colors
import dis_warning
from dash import dcc, html
import sql_queries
from sql_queries import (query_results_1, query_results_2, query_results_3, 
                         query_results_4, query_results_5, query_results_6, 
                         query_results_7, query_results_8, query_results_9,
                         query_results_10, query_results_11, query_results_12, 
                         query_results_13, query_results_14, query_results_15,
                         query_results_16)

years = ['2022',' 2023', '2024', '2025', '2026', '2027', '2028']
BAR_H_WIDTH = 2 
PLOTS_FONT_SIZE = 11
PLOTS_HEIGHT = 340  # For main graphs
SMALL_PLOTS_HEIGHT = 290  # For secondary graphs

ppa_fixed_exp_layout=html.Div(
    children=[
            html.Div(
            className="central-panel1-title",
            children=["Exposition Hedged vs PPA Fixed"],
            ),
            
            html.Div(
           className="central-panel1",
           children=[
               html.Div(
                   children=[
                       html.Div(
                           style={
                               "display": "inline-block",
                               "vertical-align": "top",
                               "width": "70%",
                           },
                           children=[
                               dcc.Graph(id="ppa_fixed_exp",
                                         figure = {'data':[
                    
                                             # go.Bar(
                                             #     name='ppacr', 
                                             #     x=years, 
                                             #     y=query_results_7['HCR_per_year'],
                                             #     opacity=1,
                                             #     marker=dict(color=colors['white']),
                                             #     marker_line=dict(width= BAR_H_WIDTH, color=colors['bar_h_color']),
                                             #     textposition='outside',
                                             #     textfont = dict(family="Times", size= 10, color= colors["white"]),
                                             #     ),
                                             go.Bar(
                                                 name='PPA', 
                                                 x=years, 
                                                 y=query_results_16['ppa_fixed'],
                                                 opacity=0.2,
                                                 marker=dict(color=colors['ppa']),
                                                 marker_line=dict(width= BAR_H_WIDTH, color=colors['bar_h_color'])
                                                 ),
                                            go.Bar(
                                                name='Exposition', 
                                                x=years, 
                                                y=query_results_1['yearly_exposition'],
                                                opacity=0.4,
                                                marker=dict(color=colors['e_white']),                             
                                                marker_line=dict(width= BAR_H_WIDTH, color=colors['bar_h_color']) 
                                                ), 
                                            ], 
                                             'layout':go.Layout(title='PPA hedge/year',
                                                                # annotations=[dict(x=years[0], y=(query_results_10.iloc[0, 1])+20, text=query_results_7.iloc[0, 1], showarrow=False, align='center', 
                                                                #                   font=dict(size=8)), 
                                                                #              dict(x=years[1], y=(query_results_10.iloc[1, 1])+20,text=query_results_7.iloc[1, 1], showarrow=False, align='center', font=dict(size=8)),
                                                                #              dict(x=years[2], y=(query_results_10.iloc[2, 1])+20,text=query_results_7.iloc[2, 1], showarrow=False, align='center', font=dict(size=8)),
                                                                #              dict(x=years[3], y=(query_results_10.iloc[3, 1])+20,text=query_results_7.iloc[3, 1], showarrow=False, align='center', font=dict(size=8)),
                                                                #              dict(x=years[4], y=(query_results_10.iloc[4, 1])+20,text=query_results_7.iloc[4, 1], showarrow=False, align='center', font=dict(size=8)),
                                                                #              dict(x=years[5], y=(query_results_10.iloc[5, 1])+20,text=query_results_7.iloc[5, 1], showarrow=False, align='center', font=dict(size=8)),
                                                                #              dict(x=years[6], y=(query_results_10.iloc[6, 1])+20,text=query_results_7.iloc[6, 1], showarrow=False, align='center', font=dict(size=8))],
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
                               ]),
                           ],
                       ),
                       # html.Div(
                       #     style={
                       #         "display": "inline-block",
                       #         "margin-top": "20px",
                       #         "width": "25%"
                       #         },
                       #     children=[
                       #         dcc.Graph()
                       #         ],
                       #     ),
                       ],
           ),],
    )