from dash import Input, Output, callback
import pandas as pd
import plotly.express as px

df = pd.read_csv("datas/avocado.csv")

@callback(
    Output("graph-region", "figure"),
    Input("dropdown-region", "value")
)
def update_graph(region):
    df_filtre = df[df["region"] == region]
    fig = px.line(
        df_filtre,
        x="Date", y="Total Volume",
        title=f"Quantités vendues - {region}"
    )
    return fig   
