#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 10:10:59 2022

@author: cuiyiyuan
"""

import pandas as pd
import numpy as np
import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px


stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

### pandas dataframe to html table
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app = dash.Dash(__name__, external_stylesheets=stylesheet)
server = app.server




#Dataframe
df = pd.read_excel("Master File.xlsx")
df[['Year','Month']] = df.Date.str.split('-',expand=True)

df_bar = df.groupby(['City','Bedrooms','Year'])['Total Rentals'].sum().round().reset_index()
#df_table = df.groupby(['City','Zip','Population','Median Household Income',\
#                      'Bedrooms','Year'])[['Avg_Rent']].mean().round().\
#                        reset_index().sort_values(by=['Avg_Rent'], ascending=False)
                        
                        
df_table = df.groupby(['City','Zip','Population','Median Household Income','Bedrooms','Year'])
df_table = df_table.agg(
    Avg_Rent=('Avg_Rent', np.mean),
    Min_Rent=('Min_Rent', np.min),
    Max_Rent=('Max_Rent', np.max)
    ).reset_index().sort_values(by=['Avg_Rent'], ascending=False)
df_table['Avg_Rent'] = df_table.Avg_Rent.round()                        
                        
df_line = df.sort_values(by='Date')





#Figure
fig1 = px.bar(df_bar, x="City", y="Total Rentals", color="Year",pattern_shape="Year",barmode="group")
fig2 = px.line(df_line, x="Date", y="Avg_Rent",color="City_Zip",line_group='Bedrooms',title="Line by Date in Avg Rents")
fig2.update_traces(mode="markers+lines")






#Layout
app.layout = html.Div(children=[
    html.H1(children='Rental Market of Selected Areas in Masschusetts',
            style={'textAlign' : 'center',
                   "color" : 'Navy',}),
    html.Br(),
    
    html.Div(children= 'Individual MA705 Project | Yiyuan Cui',
             style={
                 'textAlign': 'left',
                 "font-weight": "bold",
                 'font-size': 22,
                 }),
    
    html.Br(),
    
    
    
    
    
    html.Div(children=[
        html.H5(children="Introduction about this dashboard",
                style={
                    'textAlign': 'left',
                    "font-weight": "bold",
                    "color" : 'Navy',
                    'font-size': 18,
                    }),
        
        
        
        html.Div(html.P([
            "This dashboard covers the rental market of several selected areas (by zip code) in Massachusetts from April 2020 to Nov 2022.",
            html.Br(),
            "The users can look at different aspects of the rental market through three different filters:",
            html.Br(),
            "   -- Number of bedrooms – the number of bedrooms of the rental, only one number can be selected at a time",
            html.Br(),
            "   -- Year of the rental – the year of the rental market, multiple years can be selected at once",
            html.Br(),
            "   -- City of the rental – the city of the rental market in which only one zip code is associated with each city, and multiple cities can be selected at once",
            ],
        
                 
                 style={
                     'textAlign': 'left',
                     'font-size': 18,
                     'max-width': '90%'
                     }
                 )),
            ]),
    
    
    
    html.Br(),
    
    
    
    html.Div(children=[
        html.H5(children="How to use this dashboard?",
                style={
                    'textAlign': 'left',
                    "font-weight": "bold",
                    "color" : 'Navy',
                    'font-size': 18,
                    }),
        
        
        html.Div(html.P([
            "Please use the dropdown menu to select the number of bedrooms, and then the year and city of the rental market."
            "Matching results will be shown in a bar chart, scatter plot with lines and a table."
            "The bar chart shows the total rentals and the scatter plot with lines shows the average rental price in each month of the selected years."
            "The table shows the the average, minimum and maximum rental price of the selected cities, years and number of bedrooms, "
            "and it is sorted by the average rental price with the top ten average rental prices listed in the table."
            "Also, addition information includes zip code, population, and median household income of the corresponding cities." 
            ],
        
                 
                 style={
                     'textAlign': 'left',
                     'font-size': 18,
                     'max-width': '96%',
                     'display': 'inline-block',
                     
                     }
                 )),
            ]),
    
    
    
    
    html.Br(),
    
    
    #DCC
    html.Div(children=[
        html.Label('Select Number of Bedrooms', style={"font-weight": "bold",
        'font-size': 18,"color" : 'Navy',}),
        
        dcc.Dropdown([0, 1, 2, 3, 4, 5], 2,
                     placeholder="Select a Number of Bedroom",
                     style={'font-size': 18, 'width': '70%',},
                     id = 'dropdown'),
        
        
        html.Br(),
        
        html.Label('Select Year of the Rental', style={"font-weight": "bold",
        'font-size': 18,"color" : 'Navy',}),
        
        dcc.Checklist(
            options=[{'label':'2020','value':'2020'},
                     {'label':'2021','value':'2021'},
                     {'label':'2022','value':'2022'}],
            value=['2020','2021', '2022'],
            style={'font-size': 18},
            id='year')],
        style={'width': '35%', 'display': 'inline-block'}),
        
       
     #html.Br(), 
     
     html.Div(children=[   
        html.Label('Select City of the Rental', style={"font-weight": "bold",
        'font-size': 18,"color" : 'Navy',}),
        
        dcc.Checklist(
            options=[{'label':'Boston', 'value':'Boston'},
                     {'label':'Waltham', 'value':'Waltham'},
                     {'label':'Marlborough', 'value':'Marlborough'},
                     {'label':'Worcester', 'value':'Worcester'},
                     {'label':'Springfield','value':'Springfield'}],
            value=['Boston', 'Waltham', 'Marlborough', 'Worcester', 'Springfield'],
            style={'font-size': 18},
            id='checklist'),
        
        ]
         
         ,style={'width': '50%', 'display': 'inline-block',
                 #"verticalAlign": "top"
                     }),
                 
              
                 
                 
                 
    
   


    #total rentals in bar chart
    
    html.Br(),

    
    html.Div(children='''
        
   '''),
    
    dcc.Graph(
       id='bar_rentals',
       figure=fig1,
       
    ),
    
    
    
    #avg rent by line
    html.Div(children=
        ''),
    dcc.Graph(
        id='line_date',
        figure=fig2,
    ),
    
    
    
    html.Div(children= 'Top 10 Average Rental Price',
             style={
                 'textAlign': 'left',
                 "font-weight": "bold",
                 "color" : 'Navy',
                 'font-size': 18,
                 }),
   
    
    
    #top10 table
    html.Div(
        id='table'
        ),
        
        
   
    
])


             
             

#Call back


@app.callback(
    Output("table", "children"),
    Input("checklist", "value"),
    Input('dropdown', 'value'),
    Input('year','value')
)

def update_table(cities, bedroom, year):
    x = df_table[(df_table.City.isin(cities))&(df_table.Year.isin(year))&(df_table.Bedrooms==bedroom)]
    return generate_table(x)




@app.callback(
    Output('bar_rentals', "figure"),
    Input("checklist", "value"),
    Input('dropdown', 'value'),
    Input('year','value')
)

def update_bar(cities, bedroom, year):
    df2 = df_bar[(df_bar.City.isin(cities))&(df_bar.Year.isin(year))&(df_bar.Bedrooms==bedroom)]
    fig_bar = px.bar(df2, x="City", y="Total Rentals", color="Year",barmode="group",title="Total Rentals of Selected City, Year and Bedrooms")
    fig_bar.update_layout(legend=dict(orientation="h",
                                      yanchor="bottom",
                                      y=1.02,
                                      xanchor="right",
                                      x=1),
                          margin=dict(l=150, r=150)
                              )
    
    

                          
                          
    
    return fig_bar




@app.callback(
    Output("line_date", "figure"),
    Input("checklist", "value"),
    Input('dropdown', 'value'),
    Input('year','value')
)

def update_line(cities, bedroom, year):
    df3 = df_line[(df_line.City.isin(cities))&(df_line.Year.isin(year))&(df_line.Bedrooms==bedroom)]
    fig_line = px.line(df3, x="Date", y="Avg_Rent",color="City",line_group='Bedrooms',title="Average Rental Price by Month")
    fig_line.update_traces(mode="markers+lines")
    fig_line.update_layout(margin=dict(l=150, r=250)
        )
    
    return fig_line









if __name__ == '__main__':
    app.run_server(debug=True)






















