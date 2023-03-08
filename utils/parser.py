import argparse
from pathlib import Path
from utils.config import *

def run_parser():
    parser = argparse.ArgumentParser(
        prog = "WCAT Nearest Neighbor Assignments",
        description = "Tool to allocate work items into the nearest open workload. The WCAT file should include work items to be assigned and needs the easting and northing. The datbase file contains all active work items, their workloads, and the easting and northing of the work items."
    )
    parser.add_argument("wcat", help="Copy and paste the name of the WCAT file. This must be in the data folder.")
    parser.add_argument("database", help="Copy and paste the name of the Database file. This must be in the data folder.")
    args = parser.parse_args()
    wcatPath = Path("./data/"+args.wcat)
    databasePath = Path("./data/"+args.database)

    if not wcatPath.exists():
        raise ValueError("Check the WCAT file name.")

    if not databasePath.exists():
        raise ValueError("Check the database file name.")

    return (wcatPath, databasePath)
