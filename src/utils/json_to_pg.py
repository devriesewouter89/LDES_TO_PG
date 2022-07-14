import pandas as pd
from sqlalchemy import create_engine
import argparse

from src.parser.parser_im import generate_dataframe_im
from src.parser.parser_dmg import generate_dataframe_DMG
from src.parser.parser_hva import generate_dataframe_hva
from src.parser.parser_stam import generate_dataframe_stam
from src.parser.parser_thes import generate_dataframe_thesaurus
from src.parser.parser_agents import generate_dataframe_AGENTS
from src.parser.parser_archief import generate_dataframe_ARCH
from src.parser.parser_generic import generate_dataframe_generic
from src.utils.config import config


# from src.parser.parser_archief import

# df_im = generate_dataframe_im()
# df_stam = generate_dataframe_stam()
# df_dmg = generate_dataframe_DMG()
# df_hva = generate_dataframe_hva()
# df_archief = generate_dataframe_ARCH()
# df_thes = generate_dataframe_thesaurus()
# df_agents = generate_dataframe_AGENTS()
#
# post_gres_credentials = "postgresql://postgres:co2etzee1648@localhost:5432/postgres"
# engine = create_engine(post_gres_credentials)

# df_dmg.to_sql('ldes_dmg', engine, if_exists="append")
# df_stam.to_sql("ldes_stam", engine, if_exists="append")
# df_im.to_sql("ldes_im", engine, if_exists="append")
# df_hva.to_sql("ldes_hva", engine, if_exists="append")
# df_archief.to_sql("ldes_archief", engine, if_exists="append")
# df_agents.to_sql("ldes_agents", engine, if_exists="append")
# df_thes.to_sql("ldes_thes", engine, if_exists="append")


def object_counter(config):
    try:
        count_stam = len(config.df_stam["URI"])
        count_dmg = len(config.df_dmg["URI"])
        count_hva = len(config.df_hva["URI"])
        count_im = len(config.df_im["URI"])
        count_archief = len(config.df_archief["URI"])
        total = count_im + count_dmg + count_hva + count_stam + count_archief
        return total
    except Exception:
        pass


def general_tracker(config):
    try:
        count_stam = len(config.df_stam["URI"])
        count_dmg = len(config.df_dmg["URI"])
        count_hva = len(config.df_hva["URI"])
        count_im = len(config.df_im["URI"])
        count_archief = len(config.df_archief["URI"])

        data = {
            "INST": ["STAM", "Design Museum Gent", "Huis van Alijn", "Industriemuseum", "Archief"],
            "object_count": [count_stam, count_dmg, count_hva, count_im, count_archief]
        }

        df_count = pd.DataFrame(data, columns=["INST", "object_count"])
        return df_count

    except Exception:
        pass


def convert_to_pg(location_list, postgres_engine):
    # todo: optimize for concurrent conversion
    for c in location_list:
        if c in ["DMG", "IM", "STAM", "HVA", "ARCH", "THES"]:
            df = generate_dataframe_generic(c)
        else:
            df = generate_dataframe_AGENTS()
        df.to_sql(c, postgres_engine)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='convert json to postgres for chosen DCAT')
    parser.add_argument("--convert", metavar="convert", action="append", help="choose collections to convert",
                        choices=["DMG", "IM", "STAM", "HVA", "ARCH", "THES", "AGENTS"])
    args = parser.parse_args()

    postgres_credentials = "postgresql://postgres:postgres@localhost:5432/coghent_DMG"
    engine = create_engine(postgres_credentials)

    convert_to_pg(args.convert, engine)
    _config = config()
    # df_im = generate_dataframe_im()
    # df_stam = generate_dataframe_stam()
    # df_dmg = generate_dataframe_DMG()
    # df_hva = generate_dataframe_hva()
    # df_archief = generate_dataframe_ARCH()
    # df_thes = generate_dataframe_thesaurus()
    # df_agents = generate_dataframe_AGENTS()
    """

    general_tracker(config=_config)

    df_dmg_final_len = len(df_dmg.URI.unique())
    df_hva_final_len = len(df_hva.URI.unique())
    df_im_final_len = len(df_im.URI.unique())
    df_stam_final_len = len(df_stam.URI.unique())
    df_archief_final_len = len(df_archief.URI.unique())

    # df_dmg_final = df_dmg.groupby(["URI"], sort=False)["timestamp"].max()
    df_dmg_final = df_dmg.groupby(["URI"], sort=False, as_index=False)["timestamp"].max()
    # df_d_final = pd.merge(df_dmg, df_dmg_final_2, how='left', left_on=["URI", "timestamp"], right_on=["URI", "timestamp"])
"""
