# PARSE DATA FROM JSON TO DATAFRAME
from src.utils.utils import *
from src.parser.parser_im import generate_dataframe_im
from src.parser.parser_dmg import generate_dataframe_DMG
from src.parser.parser_hva import generate_dataframe_hva
from src.parser.parser_stam import generate_dataframe_stam
from src.parser.parser_thes import generate_dataframe_thesaurus
from src.parser.parser_agents import generate_dataframe_AGENTS
from src.parser.parser_archief import generate_dataframe_ARCH

keys = ["dmg", "hva", "stam", "industriemuseum", "thesaurus", "agents", "archiefgent"]


def generate_dataframe_generic(location, config):
    match location:
        case "dmg":
            df = generate_dataframe_DMG(location, config)
        case "hva":
            df = generate_dataframe_hva(location, config)
        case "stam":
            df = generate_dataframe_stam(location, config)
        case "industriemuseum":
            df = generate_dataframe_im(location, config)
        case "thesaurus":
            df = generate_dataframe_thesaurus(location, config)
        case "agents":
            df = generate_dataframe_AGENTS(location, config)
        case "archiefgent":
            df = generate_dataframe_ARCH(location, config)
        case _:
            print("code not found")
            df = None
    return df
