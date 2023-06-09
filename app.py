from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px

df = pd.read_csv("engraving.csv", index_col=0)

table = dag.AgGrid(
    id="engraving-table",
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i} for i in df.columns],
    defaultColDef={"resizable": True, "sortable": True, "filter": True, "minWidth": 115},
    columnSize="sizeToFit",
    dashGridOptions={"pagination": False},
    className="ag-theme-alpine-dark",
    style={"overflow": "hidden", "height": "100vh"},
)

theme = dbc.themes.MORPH
style_sheet = ["assets/style"]
icons = "https://use.fontawesome.com/releases/v5.15.3/css/all.css"

app = Dash(
    "Engravings",
    suppress_callback_exceptions=True,
    external_stylesheets=[icons, theme, style_sheet],
    title="Inventory Retracement Bar",
)

app.layout = dbc.Col(
    html.Div(table, style={"overflow": "hidden", "height": "100vh"}),
)

if __name__ == "__main__":
    app.run(debug=True)
