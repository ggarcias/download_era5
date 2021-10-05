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

WORK_DIR=${HOME}/Projects/download_era5



echo "Change qsub method and WORKDIR"
exit
#qsub -q impressive -e ${WORK_DIR}/process.err -o ${WORK_DIR}/process.o ${WORK_DIR}/download_era5.sh --json ${json}

