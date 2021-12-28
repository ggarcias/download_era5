#!/bin/bash

cdo=/TEST/mentalo/usr/cdo-1.8.2/bin/cdo

data="$ERADIR/src/tmp_dir"

$cdo -b F64 mergetime $data/*.nc $data/era5_data_merged.nc
