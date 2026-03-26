import dash
import pandas as pd
import dash_bootstrap_components as dbc
from dash import html, dcc, register_page
import plotly.express as px

register_page(__name__, path="/", name="Comparaison")

df = pd.read_csv("datas/avocado.csv")

regions_fixes = ["MidSouth", "Northeast", "SouthCentral", "Southeast", "TotalUS", "West"]
toutes_regions = sorted(df["region"].unique())

fig_fixe = px.line(
    df[df["region"].isin(regions_fixes)],
    x="Date", y="Total Volume",
    color="region",
    title="Quantités vendues - Régions principales"
)

layout = dbc.Container([
    dbc.Card([
        dbc.CardHeader(html.H4("Quantités vendues (Total Volume)")),
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id="graph-fixe", figure=fig_fixe)
                ], md=6),
                dbc.Col([
                    dbc.Badge("Sélectionnez une région :", color="primary", className="mb-2"),
                    dcc.Dropdown(
                        id="dropdown-region",
                        options=[{"label": r, "value": r} for r in toutes_regions],
                        value=toutes_regions[0],
                        clearable=False
                    ),
                    dcc.Graph(id="graph-region")
                ], md=6)
            ])
        ])
    ])
], fluid=True, style={
    "backgroundImage": "url('/assets/BG.jpg')",
    "backgroundSize": "cover",
    "backgroundPosition": "center",
    "minHeight": "100vh",
    "padding": "20px"
})