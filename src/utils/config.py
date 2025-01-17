import os
import sys
from dataclasses import dataclass


@dataclass
class Config:
    ROOT_DIR = os.path.abspath(os.curdir)

    # check which platform to define path structure.
    if sys.platform == "darwin" or sys.platform == "linux":
        data_path = os.path.join(ROOT_DIR, "data")
    else:
        data_path = ROOT_DIR + "data"  # used to be: \\src\\utils\\data

    timestamp: str = "2021-10-20T00:00:00.309Z"
    context: str = "src/utils/context.jsonld"

    filepath = {
        "dmg": os.path.join(ROOT_DIR, "data", "dmg_obj.json"),
        "hva": os.path.join(ROOT_DIR, "data", "hva_obj.json"),
        "stam": os.path.join(ROOT_DIR, "data", "stam_obj.json"),
        "industriemuseum": os.path.join(ROOT_DIR, "data", "im_obj.json"),
        "archiefgent": os.path.join(ROOT_DIR, "data", "arch_obj.json"),
        "thesaurus": os.path.join(ROOT_DIR, "data", "thes.json"),
        "agents": os.path.join(ROOT_DIR, "data", "agents.json")
    }

    # define columns to for dataframes
    columns_obj = ["URI", "timestamp", "@type", "owner", "objectnumber", "title", "object_name", "object_name_id",
                   "creator", "creator_role", "creation_date", "creation_place", "provenance_date", "provenance_type",
                   "material", "material_source", "description", "collection", "association", "location"]

    columns_thes = ["URI", "timestamp", "term", "ext_URI"]

    columns_agents = ["URI", "timestamp", "full_name", "family_name", "sirname", "name (organisations)",
                      "date_of_birth",
                      "date_of_death", "place_of_birth", "place_of_death", "nationality", "gender", "ulan", "wikidata",
                      "rkd", "same_as"]

    endpoints = {
        # CLI commands to fetch LDES from actor-init-ldes-client
        "dmg": "https://apidg.gent.be/opendata/adlib2eventstream/v1/dmg/objecten",
        "hva": "https://apidg.gent.be/opendata/adlib2eventstream/v1/hva/objecten",
        "stam": "https://apidg.gent.be/opendata/adlib2eventstream/v1/stam/objecten",
        "industriemuseum": "https://apidg.gent.be/opendata/adlib2eventstream/v1/industriemuseum/objecten",
        "archiefgent": "https://apidg.gent.be/opendata/adlib2eventstream/v1/archiefgent/objecten",
        "thesaurus": " https://apidg.gent.be/opendata/adlib2eventstream/v1/adlib/thesaurus",
        "agents": "https://apidg.gent.be/opendata/adlib2eventstream/v1/adlib/personen"
    }