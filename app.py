import dash
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)
app.title = "Avocado Dashboard"

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Comparaison entre région", href="/compare")),
        dbc.NavItem(dbc.NavLink("Affichage des données", href="/table")),
        dbc.NavItem(dbc.NavLink("Aide en ligne", href="/markdown")),
    ],
    brand="Application des M1 MECEN",
    brand_href="/",
    color="primary",
    dark=True,
    fluid=True
)

app.layout = html.Div([
    navbar,
    dash.page_container
])

import pages.page1_cb
import pages.page2_cb 

if __name__ == "__main__":
    app.run(debug=True) 
