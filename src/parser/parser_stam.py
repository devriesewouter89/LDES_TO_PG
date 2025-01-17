# PARSE DATA FROM JSON TO DATAFRAME

from src.utils.utils import *
import json


def generate_dataframe_stam(location, config):
    df_stam = pd.DataFrame(generate_dataframe(location, config))

    for i in range(0, len(config.columns_obj)):
        df_stam.insert(i, config.columns_obj[i], "")

    for i in range(0, len(df_stam)):
        x = df_stam.loc[i]
        j = json.loads(x[0])

        # URI
        uri, type = j["http://purl.org/dc/terms/isVersionOf"]["@id"], j["@type"]
        df_stam.at[i, "URI"] = uri
        df_stam.at[i, "@type"] = type

        fetch_title(df_stam, i, j)
        fetch_owner(df_stam, i, j)
        fetch_objectname(df_stam, i, j)
        fetch_provenance(df_stam, i, j)
        fetch_creators(df_stam, i, j)
        fetch_creator_role(df_stam, i, j)
        fetch_creator_place(df_stam, i, j)
        fetch_creation_date(df_stam, i, j)
        # fetch_provenance_date(df_stam, i, j)
        fetch_objectnumber(df_stam, i, j)
        fetch_material(df_stam, i, j)
        fetch_location(df_stam, i, j)
        fetch_collection(df_stam, i, j)
        fetch_description(df_stam, i, j)
        fetch_timestamp(df_stam, i, j)
    return df_stam
# TODO: add to ES
