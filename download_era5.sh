#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -q high



pwd=/BGFS/DISASTER/garcgui/download_era5
cd $pwd

# Run python
env/bin/python ./main.py --json data/data_schism.json
