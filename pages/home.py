# Import libraries
from dash import html
from dash_labs.plugins import register_page
import dash_bootstrap_components as dbc


# Register page for app.py call, menu name and route 
register_page(__name__,path="/")

# specific layout for this page
layout = dbc.Container(
            className="complete_content",
            children=[
                dbc.Row([
                        dbc.Carousel(
                        items=[
                            {"key": "1", "src": "institution-website.png", "img_style":{"height":"50px","max-width":"300px"}},
                            {"key": "2", "src": "logo2.png", "img_style":{"height":"50px","max-width":"200px"} }
                        ],
                        controls=False,
                        indicators=False,
                        interval=5000,
                        ride="carousel",
                        )
                ], justify="end"),
                
                html.P(),

                html.Div(
                    children=[
                        html.Div(
                            children=[

                                dbc.Row([

                                    dbc.Col([
                                    html.H2('Name of Institutions'),
                                    html.H6('Submitting an application for a passport request in Colombia was a relatively easy process. However, in 2021, the Colombian Ministry of Foreign Affairs acknowledged the backlog in passport procedures and reported that this is due to the high demand for passports due to the pandemic where the issuance process was suspended.'),
                                    html.H6('Among the variety of reasons why Colombians approach governmental entities to request for a passport there are: Expired passports to be renewed, lost passports to be reissued, people seeking to obtain their passport for the first time and there has also been an increasing number of migrants who have been granted Colombian nationality.'),
                                    html.H6('The problem to be solved is important in order to offer an acceptable service to the citizen and to reach a point of stability adequate to the institutional capacity to supply the actions in correspondence to the estimated demand for passport processing. demand for passport processing.')
                                    ])

                                ]),

                                html.P(),

                                dbc.Row([
                                    dbc.Col([
                                    html.H3('Forecasts & Trends'),
                                    html.H6("""This view displays a weekly forecast of passport requests for the next three months along with year-on-year view to compare current year volume with the last year. 
                                    Both views come a slider object to zoom in/out certain periods. Below there are two panes: a table with the forecast values (left) and the time series decomposed into it's main patterns. 
                                    Finally on the bottom, the year on year behavior of passport requests, comparing the current year with the previous year.""", className="d-flex justify-content-start"),
                                    ]),
                                    dbc.Col([
                                    html.H3('Status'),
                                    html.H6("""This view displays the number of unclaimed passports within the past 12-months and the number of passports that were issued by the entity and that will expire within the next 12-month window (bottom).""")
                                    ]),
                                ])
                            ]
                        ),
                    ]
                )

])