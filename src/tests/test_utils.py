import datetime
import os

from src.utils import download_cmems_data, standardize_sea_water_velocity

def test_cmems():
    data = {
            "id": "deep_horizon",
            "service_id": "GLOBAL_REANALYSIS_PHY_001_030-TDS",
            "product_id": "global-reanalysis-phy-001-030-daily",
            "t0": "2010-04-20",
            "days": 15,
            "lon_o": -98,
            "lon_f": -81,
            "lat_o": 16,
            "lat_f": 31,
            "var_1": "uo",
            "var_2": "vo"
    }

    tf = datetime.datetime.now() - datetime.timedelta(days=3)

    download_cmems_data(data)

    while t0 < tf:
        date_o = t0.strftime("%Y-%m-%d")
        assert os.path.exists("src/tmp_data/"+data["product_id"] + "_" + date_o + ".nc")
        t0 += datetime.timedelta(hours=24)

def test_standard():
    data = {
            "id": "deep_horizon",
            "service_id": "GLOBAL_REANALYSIS_PHY_001_030-TDS",
            "product_id": "global-reanalysis-phy-001-030-daily",
            "t0": "2010-04-20",
            "days": 15,
            "lon_o": -98,
            "lon_f": -81,
            "lat_o": 16,
            "lat_f": 31,
            "var_1": "uo",
            "var_2": "vo"
    }

    standardize_sea_water_velocity(data)
