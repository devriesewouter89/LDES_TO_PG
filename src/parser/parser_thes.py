from src.utils.utils import *
import json


def generate_dataframe_thesaurus(location, config):
    """generate dataframe and populate with data from LDES"""
    df_thes = pd.DataFrame(generate_dataframe(location, config))

    for i in range(0, len(config.columns_thes)):
        df_thes.insert(i, config.columns_thes[i], "")

    for i in range(0, len(df_thes)):
        x = df_thes.loc[i]
        j = json.loads(x[0])
        # print(j["http://purl.org/dc/terms/isVersionOf"])

        uri = j["http://purl.org/dc/terms/isVersionOf"]
        df_thes.at[i, "URI"] = uri

        fetch_timestamp(df_thes, i, j)
        fetch_thesaurus_term(df_thes, i, j)
        fetch_thesaurus_external_uri(df_thes, i, j)

    return df_thes

