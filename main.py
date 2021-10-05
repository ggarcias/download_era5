# main.py

# Information in README.md

import argparse
import datetime
import json

from src.utils import download_era5_pl, download_era5_sl


parser = argparse.ArgumentParser()
parser.add_argument("--json", help="insert parameters oilspill json format")
args = parser.parse_args()

with open(args.json) as f:
    jdata = json.load(f)


t0 = datetime.datetime.strptime(jdata["t0"], "%Y-%m-%d") 
tf = datetime.datetime.strptime(jdata["tf"], "%Y-%m-%d") 

while t0 <= tf:
#    download_era5_pl(jdata["bbox"], t0)
    download_era5_sl(jdata["bbox"], t0)
    t0 += datetime.timedelta(days=1)

