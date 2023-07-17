from lang import en_US
from menus import MenuCollapse
from dropdown_menu import (
    components_agrouped,
    build_components,
)

acessories_collapse = MenuCollapse(
    lang=en_US,
    label="MODIFY_ACESSORIES",
    component=components_agrouped,
    id_prefix="acessories"
).components

class_collapse = MenuCollapse(
    lang=en_US,
    label="MODIFY_BUILD",
    component=build_components,
    id_prefix="class"
).components

