# LDES_TO_PG

replicate CoGhent Linked Data Event Streams into tabular dataframe (postgresql, csv, excel)

Available collections:

| code            | Description |
|-----------------|-----------|
| dmg             | Design Museum Gent|
| hva             | Huis van Alijn|
| industriemuseum | Industriemuseum|
| archiefgent     | Archief Gent|
| stam            | STAM (stadsmuseum Gent)|
|||
| thesaurus       | thesaurus (conceptlist)|
| agents          | agent list|
| EXHIBITIONS     |list of exhibitions (restricted to Design Museum Gent )|

## installation

### python environment

`pip install -r requirements.txt`

### actor-init-ldes-client

This repo makes use of the actor-init-ldes-client library. see [https://github.com/CoGhent/api-docs-tooling/wiki/TOOLING](https://github.com/CoGhent/api-docs-tooling/wiki/TOOLING) for installation.

### postgresql environment

In order to insert the data into a postgresql database, you must first install postgresql and create a database.
Based on the [connection string](https://hasura.io/learn/database/postgresql/installation/postgresql-connection-string/) you can then insert the captured data into the postgresql database.


## USAGE 

| Parameter      | Description                                                                              | Possible values |
|----------------|------------------------------------------------------------------------------------------|----------|
| --process      | define collections to process from CoGhent LDES                                          |DMG, HVA, STAM, IM, ARCHIEF, THESAURUS, AGENTS|
| --timestamp    | datetime to prune relations that have a lower datetime value                             |for example: 2020-01-01T00:00:00, default = "2021-01-01T15:48:12.309Z"|
| --result       | define the wished for result (pg=postrgres)                                              |pg, csv, xlsx|
| --download, -d | download a collection, boolean to be set to first download and then process a collection ||
for example if you want to download & process data from Design Museum Gent en Huis Van Alijn starting from 15 november 2021 you use the following line of code in CLI:

 `python3 ldes-to-pg.py --process DMG --timestamp 2021-10-10T15:48:12.309Z -d`

## License
This project is released as an open-source project under the MIT License
