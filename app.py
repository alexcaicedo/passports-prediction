#Import libraries
from datetime import date
import dash
import dash_labs as dl
import dash_bootstrap_components as dbc
from dash import html
    
# Dash instance declaration
app = dash.Dash(__name__, plugins=[dl.plugins.pages], external_stylesheets=[dbc.themes.BOOTSTRAP])
#Top menu, items get from all pages registered with plugin.pages

#Pre-built NavbarSimple with brand on the left.
navbar = dbc.NavbarSimple([

    #DropdownMenu for select page
    dbc.DropdownMenu(
        [
            #Items in the DropdownMenu
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
        nav=True,
        label="Pages",

    )],
    brand="DS4A Project - Team 10",
    color="#f8f9fa",
    className="mb-2",
)

content = html.Div(id="page-content")

#Main layout
app.layout = dbc.Container(
    [
        navbar,
        dl.plugins.page_container,
        html.Div(id='output-container-date-picker-range'),
    ],
    className="dbc",
    fluid=True,
)


# Testing server, don't use in production, host
if __name__ == "__main__":
    app.run_server(debug=True)