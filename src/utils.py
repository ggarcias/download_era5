import argparse as argparse

import cdsapi
import datetime


def download_era5_pl(jdata, t0):
    """
    Download era5 data pressure levels (3D)
    """

    # convert string to datetime
    date0 = t0.strftime("%Y-%m-%d") 

    # Download ERA5 data
    c = cdsapi.Client()
    c.retrieve(
        "reanalysis-era5-pressure-levels",
        {
            "variable": [
                "geopotential",
                "relative_humidity",
                "specific_humidity",
                "temperature",
                "u_component_of_wind",
                "v_component_of_wind",
            ],
            "pressure_level": [
                "5",
                "10",
                "20",
                "30",
                "50",
                "70",
                "100",
                "125",
                "150",
                "175",
                "200",
                "225",
                "250",
                "300",
                "350",
                "400",
                "450",
                "500",
                "550",
                "600",
                "650",
                "700",
                "750",
                "775",
                "800",
                "825",
                "850",
                "875",
                "900",
                "925",
                "950",
                "975",
                "1000",
            ],
            "product_type": "reanalysis",
            "year": t0.year,
            "month": t0.month,
            "day": t0.day,
            #'area'          : [32, 20, 45, 30], # North, West, South, East. Default: global
            "area": jdata["bbox"],  # North, West, South, East. Default: global
            "grid": [
                1.0,
                1.0,
            ],  # Latitude/longitude grid: east-west (longitude) and north-south resolution (latitude). Default: 0.25 x 0.25
            "time": [
                "00:00",
                "01:00",
                "02:00",
                "03:00",
                "04:00",
                "05:00",
                "06:00",
                "07:00",
                "08:00",
                "09:00",
                "10:00",
                "11:00",
                "12:00",
                "13:00",
                "14:00",
                "15:00",
                "16:00",
                "17:00",
                "18:00",
                "19:00",
                "20:00",
                "21:00",
                "22:00",
                "23:00",
            ],
            "format": jdata["format"],  # Supported format: grib and netcdf. Default: grib
        },
        "data/era5_"+date0+"_1h_pl.grib",
    )


def download_era5_sl(jdata, t0):
    """
    Download era5 data single levels (surface)
    """

    date0 = t0.strftime("%Y-%m-%d") 

    # Download ERA5 data
    c = cdsapi.Client()
    c.retrieve(
        "reanalysis-era5-single-levels",
        {
            "product_type": "reanalysis",
            "variable": [
                "10m_u_component_of_wind",
                "10m_v_component_of_wind",
                "mean_sea_level_pressure",
                "sea_ice_cover",
            ],
            "year": t0.year,
            "month": t0.month,
            "day": t0.day,
            #'area'          : [32, 20, 45, 30], # North, West, South, East. Default: global
            "area": jdata["bbox"],  # North, West, South, East. Default: global
            "grid": [
                1.0,
                1.0,
            ],  # Latitude/longitude grid: east-west (longitude) and north-south resolution (latitude). Default: 0.25 x 0.25
            "time": [
                "00:00",
                "01:00",
                "02:00",
                "03:00",
                "04:00",
                "05:00",
                "06:00",
                "07:00",
                "08:00",
                "09:00",
                "10:00",
                "11:00",
                "12:00",
                "13:00",
                "14:00",
                "15:00",
                "16:00",
                "17:00",
                "18:00",
                "19:00",
                "20:00",
                "21:00",
                "22:00",
                "23:00",
            ],
            "format": jdata["format"],  # Supported format: grib and netcdf. Default: grib
        },
        "data/era5_"+date0+"_1h_sl.grib",
    )
