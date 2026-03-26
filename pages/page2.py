import dash
import pandas as pd
import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table, register_page

register_page(__name__, path="/table", name="Affichage des données")

df = pd.read_csv("datas/avocado.csv")

COLS_SUPPR = ["Unnamed: 0", "4046", "4225", "4770", "Small Bags", "Large Bags", "XLarge Bags"]
df = df.drop(columns=[c for c in COLS_SUPPR if c in df.columns])

regions = sorted(df["region"].unique())
types = sorted(df["type"].unique())

colonnes = [{"name": c, "id": c} for c in df.columns]

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.P("Sélectionner une région :", className="fw-bold mt-3"),
            dcc.Dropdown(
                id="table-dropdown-region",
                options=[{"label": r, "value": r} for r in regions],
                value=regions[0],
                clearable=False
            )
        ], xs=12, md=5),

        dbc.Col([
            html.P("Sélectionner un type :", className="fw-bold mt-3"),
            dcc.RadioItems(
                id="table-radio-type",
                options=[{"label": " Tous", "value": "Tous"}] +
                        [{"label": f" {t}", "value": t} for t in types],
                value="Tous",
                inline=True,
                inputStyle={"marginRight": "5px"},
                labelStyle={"marginRight": "15px"}
            )
        ], xs=12, md=5),

        dbc.Col([
            dbc.Badge(
                id="table-badge-count",
                color="warning",
                className="mt-4 p-2 fs-6"
            )
        ], xs=12, md=2, className="d-flex align-items-end justify-content-end")
    ], className="mb-3"),

    dash_table.DataTable(
        id="table-datatable",
        columns=colonnes,
        data=df.to_dict("records"),
        page_size=15,
        sort_action="native",
        style_table={"overflowX": "auto"},
        style_header={
            "backgroundColor": "#1b5e20",
            "color": "white",
            "fontWeight": "bold",
            "textAlign": "left"
        },
        style_cell={
            "textAlign": "left",
            "padding": "10px",
            "fontSize": "0.85rem"
        },
        style_data_conditional=[
            {"if": {"row_index": "odd"}, "backgroundColor": "#f5f9f5"}
        ]
    )
], fluid=True, className="mt-3") 