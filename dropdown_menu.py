import dash_bootstrap_components as dbc
from menus import dropdownMenu
from lang import en_US
from dropdown_menu_items import (
    all_acessories_type,
    all_builds,
    all_classes,
    all_acessories_stats_items,
    all_engravings_list
)


acessories_type_dropdown = dropdownMenu(
    lang=en_US,
    label="ACESSORIES_TYPE",
    options=all_acessories_type,
    id_prefix="acessories_type"
).dropdown_components

acessories_stats_dropdown = dropdownMenu(
    lang=en_US,
    label="ACESSORIES_STATS",
    options=all_acessories_stats_items,
    id_prefix="acessories_stats",
    is_multi_options=True,
).dropdown_components

acessories_eng1_dropdown = dropdownMenu(
    lang=en_US,
    label="ENGRAVING1",
    options=all_engravings_list,
    id_prefix="engravings1",
    is_multi_options=True,
).dropdown_components

components_agrouped = [dbc.CardGroup([
    dbc.Col(
        dbc.Row(
            [
                acessories_type_dropdown,
            ]
        )
    ),
    dbc.Col(
        dbc.Row(
            [
                acessories_stats_dropdown
            ]
        )
    ),
]),
dbc.Col(
    acessories_eng1_dropdown,
    )]

build_dropdown = dropdownMenu(
    lang=en_US,
    label="BUILD",
    options=all_builds,
    id_prefix="build"
).dropdown_components

class_dropdown = dropdownMenu(
    lang=en_US,
    label="CLASS",
    options=all_classes,
    id_prefix="class"
).dropdown_components

build_components = dbc.Row([
    dbc.CardGroup([
        dbc.Col(
            dbc.Row(class_dropdown),
        ),
    ]),
    dbc.Col(
        dbc.Row(build_dropdown),
    )
])