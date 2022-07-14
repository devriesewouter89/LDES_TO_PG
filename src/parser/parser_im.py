#PARSE DATA FROM JSON TO DATAFRAME

from src.utils.utils import *
import json
import pandas as pd

def generate_dataframe_im(config):
    df_im = pd.DataFrame(generate_dataframe("IM", config))

    for i in range(0, len(config.columns_obj)):
        df_im.insert(i, config.columns_obj[i], "")

    for i in range(0, len(df_im)):
        x = df_im.loc[i]
        j = json.loads(x[0])

        # URI
        uri, type = j["http://purl.org/dc/terms/isVersionOf"]["@id"], j["@type"]
        df_im.at[i, "URI"] = uri
        df_im.at[i, "@type"] = type

        fetch_title(df_im, i, j)
        fetch_owner(df_im, i, j)
        fetch_objectname(df_im, i, j)
        fetch_objectnaam_id(df_im, i, j)
        fetch_provenance(df_im, i, j)
        fetch_creator(df_im, i, j)
        fetch_creator_role(df_im,i ,j)
        fetch_creator_place(df_im, i, j)
        fetch_creation_date(df_im, i, j)
        #fetch_provenance_date(df_dmg, i, j)
        fetch_material(df_im, i , j)
        fetch_location(df_im, i , j)
        fetch_collection(df_im, i, j)
        fetch_description(df_im, i, j)
        fetch_timestamp(df_im, i, j)

    return df_im

