from dash import Dash, dcc
import dash_bootstrap_components as dbc
from components import table, search_button
from collapse_components import (
    acessories_collapse,
    class_collapse,
)
from callbacks import LayoutCallBack
from dropdown_menu_items import df

theme = dbc.themes.MORPH
style_sheet = ["assets/style"]
icons = "https://use.fontawesome.com/releases/v5.15.3/css/all.css"

app = Dash(
    "Engravings",
    suppress_callback_exceptions=False,
    external_stylesheets=[icons, theme, style_sheet],
    title="Engraving Search",
)

server = app.server

table_component = table(df)

table_length = 8
component_length = 12 - table_length

app.layout = dbc.Row(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardGroup(
                        [
                            dbc.Col(
                                table_component,
                                style={"overflow": "hidden", "height": "100vh"},
                                id="table_component_col"
                            ),
                            dcc.Store(
                                id="dataframe",
                                data=df.to_dict("records")
                            )
                        ],
                    ),
                    width=table_length,
                ),
                dbc.Col(
                    [
                        dbc.Row(acessories_collapse),
                        dbc.Row(class_collapse),
                        dbc.Col(search_button),
                    ],
                    width=component_length
                )
            ],
        ),
    ],
)

if __name__ == "__main__":
    LayoutCallBack()
    app.run(debug=True)
