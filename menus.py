from dash import html, dcc
import dash_bootstrap_components as dbc

class dropdownMenu:
    def __init__(
        self,
        lang,
        label,
        options,
        id_prefix: str,
        is_multi_options: bool = False,
    ):
        self.options = options
        self.label_name = lang[label]
        self.id_prefix = id_prefix
        self.is_multi_options = is_multi_options

    @property
    def dropdown_components(self):
        return dbc.Row(
            [
                dbc.Col(
                    dbc.Label(self.label_name),
                    width=45,
                    style={"margin-top": "10px"},
                ),
                dbc.Col(
                    dcc.Dropdown(
                        self.options,
                        id=f"{self.id_prefix}_dropdown",
                        multi=self.is_multi_options,
                    ),
                    width=45,
                ),
            ]
        )

class MenuCollapse:
    def __init__(self, lang, label, component, id_prefix):
        self.label_name = lang[label]
        self.component = component
        self.id_prefix = id_prefix

    @property
    def components(self):
        button = dbc.Button(
            [
                self.label_name,
                html.I(
                    className="fa fa-chevron-down ml-2",
                    id=f"{self.id_prefix}_icon",
                    style={"transformY": "2px"},
                ),
            ],
            id=f"{self.id_prefix}_button",
            className="d-grid gap-2 col-6 mx-auto w-100",
            outline=True,
            color="secondary",
        )

        collapse = dbc.Collapse(
            dbc.Card(
                dbc.CardBody(
                    self.component,
                )
            ),
            id=f"{self.id_prefix}_collapse",
            is_open=True,
        )
        component = dbc.Col([button, collapse])


        return component