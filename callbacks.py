import dash
from dash import Input, Output, State, callback
import pandas as pd
from engraving_search import EngravingSearch
from components import table

class LayoutCallBack:
    @callback(
        Output("acessories_collapse", "is_open"),
        Output("acessories_icon", "className"),
        Input("acessories_button", "n_clicks"),
        State("acessories_collapse", "is_open"),
    )
    def toggle_acessories_collapse(n_clicks, is_open):
        if not n_clicks:
            raise dash.exceptions.PreventUpdate

        if is_open:
            return False, "fa fa-chevron-down ml-2"
        return True, "fa fa-chevron-up ml-2"

    @callback(
        Output("class_collapse", "is_open"),
        Output("class_icon", "className"),
        Input("class_button", "n_clicks"),
        State("class_collapse", "is_open"),
    )
    def class_collapse(n_clicks, is_open):
        if not n_clicks:
            raise dash.exceptions.PreventUpdate

        if is_open:
            return False, "fa fa-chevron-down ml-2"
        return True, "fa fa-chevron-up ml-2"

class TableCallback:
    @callback(
        Output("table_component_col", "children"),
        Input("search_button", "n_clicks"),
        State("dataframe", "data"),
        State("engravings1_dropdown", "value"),
        State("acessories_type_dropdown", "value"),
        State("acessories_stats_dropdown", "value"),
        State("class_dropdown", "value"),
        State("build_dropdown", "value"),
    )
    def update_table_component(
        search_button,
        dataframe,
        engravings,
        accessory_selected,
        status,
        class_selected,
        build_selected,
        ):
        ctx = dash.callback_context
        if not ctx.triggered:
            raise dash.exceptions.PreventUpdate

        if "search_button" in ctx.triggered[0]["prop_id"]:
            if engravings is None:
                engravings = []
            if accessory_selected is None or accessory_selected == []:
                accessory_selected = "all"
            if status is None:
                status = []
            if class_selected is None:
                class_selected = ""
            if build_selected is None:
                build_selected = ""

            dataframe = pd.DataFrame(dataframe)
            print(engravings)
            print(status)
            print(accessory_selected)
            search = EngravingSearch(dataframe)
            engraving_search = search.aggregate_search(
                status_list=status,
                accessory=accessory_selected,
                engraving_list=engravings,
                class_selected=class_selected,
                build_selected=build_selected,
            )

            # print(engraving_search)

            table_component = table(engraving_search)
            return table_component