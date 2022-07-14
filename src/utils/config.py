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
