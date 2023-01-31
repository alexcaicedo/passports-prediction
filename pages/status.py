#libraries
from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

# Import the codebase components
from components.status.s_plot_expiry import status_plot_expiry
from components.status.s_plot_unclaimed import status_plot_unclaimed

# Register page for app.py call, menu name and route 
register_page(__name__,path="/status")

# Call the codebase components for the plots 
p_status_expiry = status_plot_expiry('Expiry', 'id_expiry')
p_status_unclaimed = status_plot_unclaimed('Unclaimed', 'id_unclaimed')

# specific layout for this page
layout = dbc.Container(
    children=[
        dbc.Row([
            dbc.Col([
                p_status_expiry.display()
            ], xs=12, className='card')]),

        html.P(),

        dbc.Row([
            dbc.Col([
                p_status_unclaimed.display()
            ], xs=12, className='card')]),
        
        html.P()
        
       ])