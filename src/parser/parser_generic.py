#PARSE DATA FROM JSON TO DATAFRAME
from src.utils.utils import *
from src.parser.parser_im import generate_dataframe_im
from src.parser.parser_dmg import generate_dataframe_DMG
from src.parser.parser_hva import generate_dataframe_hva
from src.parser.parser_stam import generate_dataframe_stam
from src.parser.parser_thes import generate_dataframe_thesaurus
from src.parser.parser_agents import generate_dataframe_AGENTS
from src.parser.parser_archief import generate_dataframe_ARCH

keys = ["DMG", "HVA", "STAM", "IM", "THES", "AGENT", "ARCH"]
def generate_dataframe_generic(location, config):
    match location:
        case "DMG":
            df = generate_dataframe_DMG(config)
        case "HVA":
            df = generate_dataframe_hva(config)
        case "STAM":
            df = generate_dataframe_stam(config)
        case "IM":
            df = generate_dataframe_im(config)
        case "THES":
            df = generate_dataframe_thesaurus(config)
        case "AGENT":
            df = generate_dataframe_AGENTS(config)
        case "ARCH":
            df = generate_dataframe_ARCH(config)
        case _:
            print("code not found")
            df = None
    return df

