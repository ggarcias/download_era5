# main.py

# Information in README.md

import argparse
import datetime
import json
import sys

from src.utils import download_era5_pl, download_era5_sl, download_example


parser = argparse.ArgumentParser()
parser.add_argument("--json", help="insert parameters oilspill json format")
args = parser.parse_args()

with open(args.json) as f:
    jdata = json.load(f)

if jdata["format"] != "netcdf" and jdata["format"] != "grib":
    print("format must be netcdf or grib")
    sys.exit()


t0 = datetime.datetime.strptime(jdata["t0"], "%Y-%m-%d") 
tf = datetime.datetime.strptime(jdata["tf"], "%Y-%m-%d") 

#download_example()
#sys.exit()

while t0 <= tf:
#    download_era5_pl(jdata, t0)
    download_era5_sl(jdata, t0)
    t0 += datetime.timedelta(days=1)

