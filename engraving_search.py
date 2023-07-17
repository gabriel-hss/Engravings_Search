import pandas as pd
from functools import reduce


class EngravingSearch:
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def accessory_search(self, status_list: list[str], accessory: str):
        if accessory == "all":
            status_cond = reduce(
                lambda x, y: x & y,
                [
                            self.dataframe["Necklace"].str.contains(val)
                            | self.dataframe["Earring"].str.contains(val)
                            | self.dataframe["Ring"].str.contains(val)
                    for val in status_list
                ],
            )
        else:
            status_cond = reduce(
                lambda x, y: x & y,
                [
                    self.dataframe[accessory].str.contains(val)
                    for val in status_list
                ],
            )

        return self.dataframe[status_cond]

    def engraving_search(self, engraving_list: list[str]):
        engraving_cond = reduce(
            lambda x, y: x & y,
            [
                self.dataframe["Mandatory"].str.contains(val)
                | self.dataframe["Secondary"].str.contains(val)
                for val in engraving_list
            ],
        )

        return self.dataframe[engraving_cond]

    def class_search(self, class_selected: str):
        return self.dataframe[self.dataframe["Class"] == class_selected]

    def build_search(self, build_selected: str):
        return self.dataframe[self.dataframe["Build"] == build_selected]

    def aggregate_search(
        self,
        status_list: list[str] = None,
        accessory: str = None,
        engraving_list: list[str] = None,
        class_selected: str = None,
        build_selected: str = None,
    ):
        result = self.dataframe.copy()

        if status_list and accessory:
            result = self.accessory_search(status_list, accessory)

        if engraving_list:
            result = self.engraving_search(engraving_list)

        if class_selected:
            result = self.class_search(class_selected)

        if build_selected:
            result = self.build_search(build_selected)

        return result