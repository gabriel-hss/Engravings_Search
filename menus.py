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
