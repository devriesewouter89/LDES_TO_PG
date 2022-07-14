from dataclasses import dataclass
import os, sys


@dataclass
class config:
    ROOT_DIR = os.path.abspath(os.curdir)

    # check which platform to define path structure.
    if sys.platform == "darwin" or sys.platform == "linux":
        datapath = os.path.join(ROOT_DIR, "data")
    else:
        datapath = ROOT_DIR + "data"  # used to be: \\src\\utils\\data

    timestamp: str = "2021-10-20T00:00:00.309Z"
    context: str = "src/utils/context.jsonld"

    filepath = {
        "DMG": os.path.join(ROOT_DIR, "data", "dmg_obj.json"),
        "HVA": os.path.join(ROOT_DIR, "data", "hva_obj.json"),
        "STAM": os.path.join(ROOT_DIR, "data", "stam_obj.json"),
        "IM": os.path.join(ROOT_DIR, "data", "im_obj.json"),
        "ARCH": os.path.join(ROOT_DIR, "data", "arch_obj.json"),
        "THES": os.path.join(ROOT_DIR, "data", "thes.json"),
        "AGENT": os.path.join(ROOT_DIR, "data", "agents.json")
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
        "DMG": "https://apidg.gent.be/opendata/adlib2eventstream/v1/dmg/objecten",
        "HVA": "https://apidg.gent.be/opendata/adlib2eventstream/v1/hva/objecten",
        "STAM": "https://apidg.gent.be/opendata/adlib2eventstream/v1/stam/objecten",
        "IM": "https://apidg.gent.be/opendata/adlib2eventstream/v1/industriemuseum/objecten",
        "ARCH": "https://apidg.gent.be/opendata/adlib2eventstream/v1/archiefgent/objecten",
        "THES": " https://apidg.gent.be/opendata/adlib2eventstream/v1/adlib/thesaurus",
        "AGENT": "https://apidg.gent.be/opendata/adlib2eventstream/v1/adlib/personen"
    }