import pandas as pd

df = pd.read_csv("engraving.csv")

engravings_dataframe = df

all_mandatory_engravings = []
for x in engravings_dataframe["Mandatory"].values:
    all_mandatory_engravings.extend(x.split(", "))

all_secondary_engravings = []
for x in engravings_dataframe["Secondary"].dropna().values:
    all_secondary_engravings.extend(x.split(", "))

all_mandatory_engravings_dataframe = pd.DataFrame(all_mandatory_engravings).drop_duplicates()
all_secondary_engravings_dataframe = pd.DataFrame(all_secondary_engravings).drop_duplicates()

all_engravings_list = list(pd.concat([all_mandatory_engravings_dataframe, all_secondary_engravings_dataframe])[0].drop_duplicates().values)

all_acessories_type = list(engravings_dataframe.columns[-4:])
all_acessories_stats_items = ["Spec", "Swift", "Crit",]

all_builds = list(engravings_dataframe["Build"].drop_duplicates().values)
all_classes = list(engravings_dataframe["Class"].drop_duplicates().values)