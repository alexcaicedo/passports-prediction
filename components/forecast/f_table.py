# Import libraries
from dash import html , dcc
import dash_bootstrap_components as dbc
from dash import dash_table
# Import the codebase components
from codebase.prophet_predictions import predict_prophet
from codebase.preprocessing import pre_process_paquete

# Call the codebase components
f_paquete, paquete, entrega = pre_process_paquete("data/ps_paquete.csv", "data/ps_entregapasaporte.csv")
_, _, f_table, _ = predict_prophet(f_paquete, start_date="2021-10-01", forecast_end="2022-12")

class forecast_table:
    """A class to plot the forecast table"""
          
    def __init__(self,table_title:str,ID:str):
        
        """__init__
        Construc all the attributes for the table

        Args: 
            table_title (str): _Title of the table_
            ID (str): _div id to specify unique #id
        
        Methods:

        display()
            Function to display a sample map with no arguments, uses plotly express data.
            
            Arguments:
                None

            Returns:
                html.Div : A Div container with a dash_table DataTable inside
        """

        self.table_title = table_title
        self.id = ID

    def display(self):
       
        layout = html.Div(
            [
                html.H4([self.table_title]),
                html.P(),
    
                html.Div([
                    dash_table.DataTable(
                        f_table.to_dict('records'),
                        page_size=12,
                        style_cell={'textAlign': 'left'},
                        style_as_list_view=True,
                        style_header={'fontWeight': 'bold'},
                        
                    )
                ])                
            ],id=self.id
        )
        return layout