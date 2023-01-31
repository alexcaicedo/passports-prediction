# Import libraries
from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

# Register page for app.py, menu name and route 
register_page(__name__)

# Import the codebase components
from components.forecast.f_components import forecast_components
from components.forecast.f_plot import forecast_plot
from components.forecast.f_table import forecast_table
from components.forecast.f_yoy import forecast_yoy

# Call the codebase components for the plots
f_components = forecast_components('Components', 'id_components')
grafica_forecast = forecast_plot('Forecast', 'id_forecast',"2021-10-01","2022-12")
table_forecast = forecast_table('Table Forecast', 'id_table_forecast')
f_yoy = forecast_yoy('Year on Year', 'id_yoy')

# specific layout for this page
layout=  dbc.Container(
    className="complete_content",
    children=[

        dbc.Row([
            dbc.Col([
                grafica_forecast.display()
            ], xs=12, md=12, className='card'),
        ]),

        html.P(),

        dbc.Row([

            dbc.Col([
                table_forecast.display()
            ], xs=12, md=3, className='card'),

            dbc.Col([]),

            dbc.Col([
                f_components.display()
            ], xs=12, md=8, className='card')
            
        ]),

        html.P(),

        dbc.Row([

            dbc.Col([
                f_yoy.display()
            ], xs=12, md=12, className='card')
            
        ]),

        html.P(),
    ])