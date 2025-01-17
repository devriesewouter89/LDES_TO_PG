import sys
from src.utils.utils import fetch_json, clean_json_file
import argparse
import os
from datetime import datetime
from src.parser.parser_generic import generate_dataframe_generic
from sqlalchemy import create_engine
import psycopg2
from src.utils.config import *
import threading

# todo: add archive
keys = ["dmg", "hva", "stam", "industriemuseum", "thesaurus", "agents", "archiefgent"]


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


def df_to_sql(df, db_name):
    postgres_credentials = "postgresql://postgres:postgres@localhost/".format(db_name)
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


class DownloadCollection(threading.Thread):
    def __init__(self, threadID, location, config):
        threading.Thread.__init__(self, daemon=True)
        self.threadID = threadID
        self.location = location
        self.config = config

    def run(self) -> None:
        print("downloading collection of {}".format(self.location))
        try:
            p = fetch_json(key=self.location, config=self.config)
            print("{} fetched".format(_location))
            # 2. clean the json file
            clean_json_file(_location, config=_config)
            print("cleaned {}".format(_location))
            # 3. export to dataframe
            # todo: check if all names are correct (_location)
            df = generate_dataframe_generic(_location, config=_config)
            if args.result == "pg":
                df_to_sql(df, db_name=_location)
            if args.result == "csv":
                df_to_csv(df, csv_name=_location, export_path=_config.data_path)
            if args.result == "xlsx":
                df_to_xlsx(df, xlsx_name=_location, export_path=_config.data_path)

        except Exception as e:
            print(e)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='return LDES for chosen DCAT')
    parser.add_argument("--process", metavar="process", nargs='*', help="choose collections to process",
                        choices=["dmg", "industriemuseum", "stam", "hva",
                                 "archiefgent", "thesaurus", "AGENT"], default=["dmg"])
    parser.add_argument("--timestamp", default="2021-07-14T15:48:12.309Z")
    parser.add_argument("--result", choices=["pg", "csv", "xlsx"], default="csv")
    parser.add_argument("--download", "-d", action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    choice = args.process
    # initialize the config file
    _config = Config(timestamp=args.timestamp)
    # IM + HVA; laatste maal 28-08
    # stam; 30-08

    os.makedirs(_config.data_path, exist_ok=True)
    if args.download:
        print("starting the download at {}".format(datetime.now().strftime("%H:%M:%S")))
        threadList = list()
        for idx, _location in enumerate(choice):
            # 1. fetch the stream and place it in json file
            # todo: when does the stream stop???
            tempThread = DownloadCollection(idx, _location, _config)
            threadList.append(tempThread)
            tempThread.start()
        for i in threadList:
            i.join()

    for _location in choice:
        try:
            # 2. clean the json file
            clean_json_file(_location, config=_config)
            print("cleaned {}".format(_location))
            # 3. export to dataframe
            df = generate_dataframe_generic(_location, config=_config)
            if args.result == "pg":
                df_to_sql(df, db_name=_location)
                continue
            if args.result == "csv":
                df_to_csv(df, csv_name=_location, export_path=_config.data_path)
                continue
            if args.result == "xlsx":
                df_to_xlsx(df, xlsx_name=_location, export_path=_config.data_path)
                continue
        except Exception as e:
            print(e)
            pass
