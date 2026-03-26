from dash import Input, Output, callback
import pandas as pd

df = pd.read_csv("datas/avocado.csv")

COLS_SUPPR = ["Unnamed: 0", "4046", "4225", "4770", "Small Bags", "Large Bags", "XLarge Bags"]
df = df.drop(columns=[c for c in COLS_SUPPR if c in df.columns])

@callback(
    Output("table-datatable", "data"),
    Output("table-badge-count", "children"),
    Input("table-dropdown-region", "value"),
    Input("table-radio-type", "value")
)
def update_table(region, type_avocat):
    filtre = df.copy()

    if region:
        filtre = filtre[filtre["region"] == region]

    if type_avocat and type_avocat != "Tous":
        filtre = filtre[filtre["type"] == type_avocat]

    nb_lignes = f"Lignes : {len(filtre)}"

    return filtre.to_dict("records"), nb_lignes 