#!/bin/bash

while [ $# -gt 0 ] ; do
  case $1 in
    -j | --json) export json=${2};;
  esac
  shift
done

if [ -z "${json+xxx}" ]
then
    echo "Error! Undefined JSON."
    exit
fi


#cd ${HOME}/Projects/download_era5


# Run python
env/bin/python ./main.py --json ${json}
