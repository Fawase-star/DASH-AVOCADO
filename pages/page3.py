import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, register_page

register_page(__name__, path="/markdown", name="Aide en ligne")

# Lecture des fichiers markdown
with open("expli1.md", "r", encoding="utf-8") as f:
    contenu1 = f.read()

with open("expli2.md", "r", encoding="utf-8") as f:
    contenu2 = f.read()

with open("expli3.md", "r", encoding="utf-8") as f:
    contenu3 = f.read()

layout = dbc.Container([
    dbc.Card([
        dbc.CardHeader(html.H4("Présentation de Dash")),
        dbc.CardBody([
            dbc.Accordion([
                dbc.AccordionItem([
                    dcc.Markdown(contenu1)
                ], title="La Page"),

                dbc.AccordionItem([
                    dcc.Markdown(contenu2)
                ], title="Layout en Dash"),

                dbc.AccordionItem([
                    dcc.Markdown(contenu3)
                ], title="Callback en Dash"),
            ], start_collapsed=True)
        ])
    ], className="mt-4")
], fluid=True, className="mt-3")
