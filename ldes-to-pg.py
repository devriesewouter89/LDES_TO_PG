import sys
from src.utils.utils import fetch_json, clean_json_file
import argparse
import os
from datetime import datetime
from src.parser.parser_generic import generate_dataframe_generic
from sqlalchemy import create_engine
import psycopg2
from src.utils.config import *

# todo: add archive
keys = ["DMG", "HVA", "STAM", "IM", "THES", "AGENT", "ARCH"]


# TODO: make function so that it only fetches updates made since last day.
# TODO: define function that fetches all lists
# TODO: redefine function to be ASYNC
# TODO: keys (line 8) are not same as choices line 18

def verify_time(timestamp: str):
    # example: "2021-10-20T00:00:00.309Z"
    # FIRST VERIFY IF <fetch_time> in correct format
    # initializing format
    _format = "%Y-%m-%dT%H:%M:%S.%fZ"
    # using try-except to check for truth value
    try:
        bool(datetime.strptime(timestamp, _format))
        return timestamp
    except ValueError:
        print("incorrect fetch time given")


def df_to_sql(df, dbName):
    postgres_credentials = "postgresql://postgres:postgres@localhost/".format(dbName)
    db = create_engine(postgres_credentials)
    conn = db.connect()

    df.to_sql('data', con=conn, if_exists='replace', index=False)

    # check if contents are correct:
    conn = psycopg2.connect(postgres_credentials)
    conn.autocommit = True
    cursor = conn.cursor()

    sql1 = '''select * from data;'''
    cursor.execute(sql1)
    for _i in cursor.fetchall():
        print(_i)

    # conn.commit()
    conn.close()


def df_to_csv(df, csv_name, export_path):
    df.to_csv(os.path.join(export_path, "{}.csv".format(csv_name)), index=False)


def df_to_xlsx(df, xlsx_name, export_path):
    _file = os.path.join(export_path, "{}.xlsx".format(xlsx_name))
    df.to_excel(_file)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='return LDES for chosen DCAT')
    parser.add_argument("--fetch", metavar="fetch", action="append", help="choose collections to fetch",
                        choices=["DMG", "IM", "STAM", "HVA",
                                 "ARCHIEF", "THESAURUS", "AGENTS"])
    parser.add_argument("--timestamp", default="2022-07-14T15:48:12.309Z")
    parser.add_argument("--result", choices=["pg", "csv", "xlsx"])
    args = parser.parse_args()

    choice = args.fetch
    # initialize the config file
    _config = config(timestamp=args.timestamp)
    # IM + HVA; laatste maal 28-08
    # STAM; 30-08

    os.makedirs(_config.datapath, exist_ok=True)

    for _location in choice:
        try:
            # 1. fetch the stream and place it in json file
            # todo: when does the stream stop???
            # todo: right now, we don't know when the subprocess is finished, only then can we continue: ASYNCIO!!
            fetch_json(key=_location, config=_config)
            # print("{} fetched".format(_c))
            # 2. clean the json file
            clean_json_file(_location)
            # print("cleaned {}".format(_c))
            # 3. export to dataframe
            # todo: check if all names are correct (_location)
            df = generate_dataframe_generic(_location)
            if args.result == "pg":
                df_to_sql(df, dbName=_location)
                continue
            if args.result == "csv":
                df_to_csv(df, csv_name=_location, export_path=_config.datapath)
                continue
            if args.result == "xlsx":
                df_to_xlsx(df, xlsx_name=_location, export_path=_config.datapath)
                continue
        except Exception as e:
            print(e)
            pass