import dash_ag_grid as dag
import dash_bootstrap_components as dbc
from lang import en_US

def table(df):
    return dag.AgGrid(
        id="engraving-table",
        rowData=df.to_dict("records"),
        columnDefs=[{"field": i} for i in df.columns],
        defaultColDef={"resizable": True, "sortable": True, "filter": True, "minWidth": 115},
        columnSize="sizeToFit",
        dashGridOptions={"pagination": False},
        className="ag-theme-alpine-dark",
        style={"overflow": "hidden", "height": "100vh"},
    )

