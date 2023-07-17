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
