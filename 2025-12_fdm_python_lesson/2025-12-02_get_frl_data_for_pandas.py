import pandas as pd
import requests as rq
import time

from datetime import datetime
from tqdm import tqdm

datestamp_now = datetime.now().strftime("%Y-%m-%d")


response_frl_find = rq.get(
    "https://frl.publisso.de/find?q="
    "isDescribedBy.created%3A2025*"
    "+AND+NOT+contentType%3Afile"
    "+AND+hasPart.%40id%3A*"
    "+AND+NOT+isDescribedBy.createdBy%3A322"
    "&format=json"
    "&from=0"
    "&until=5000"
).json()

list_of_dataframes_parents = []
list_of_dataframes_children = []


for i in tqdm(range(len(response_frl_find))):

    time.sleep(1)

    frlId_parent = response_frl_find[i]["@id"]

    try:

        response_frl_parent = rq.get(
            f"https://frl.publisso.de/resource/{frlId_parent}.json2"
        ).json()
        df_parent = pd.json_normalize(response_frl_parent, sep="_")
        list_of_dataframes_parents.append(df_parent)

        for item in response_frl_parent["hasPart"]:

            frlId_child = item["@id"]
            response_frl_child = rq.get(
                f"https://frl.publisso.de/resource/{frlId_child}.json2"
            ).json()
            df_child = pd.json_normalize(response_frl_child, sep="_")
            list_of_dataframes_children.append(df_child)

    except Exception as e:
        print(frlId_parent, e)


try:
    df_frl_parents = pd.concat(list_of_dataframes_parents)
    df_frl_parents.to_excel(
        datestamp_now + "_frl_export_researchData_parents.xlsx", index=False
    )
except Exception as e:
    print(f"list_of_dataframes_parents: {e}")


try:
    df_frl_children = pd.concat(list_of_dataframes_children)
    df_frl_children.to_excel(
        datestamp_now + "_frl_export_researchData_children.xlsx", index=False
    )
except Exception as e:
    print(f"list_of_dataframes_children: {e}")
