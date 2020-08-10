#!/usr/bin/python
# Zhe Zhang
# 2020-04-22
# python script to extract gldas initial conditions
# origional perl code from Mike's directory
# migrate from perl to python

import os

# Manually set the date for initialization
date = "20100101"

# Set directories and file name
data_dir = "/opt/ARW/DATA/GLDAS/raw/netcdf/"
results_dir = "/opt/ARW/DATA/GLDAS/extracted/INIT/"
filestem = "GLDAS_NOAH025_3H.A"

if not os.path.exists(results_dir):
    os.system("mkdir " + results_dir)

filename = data_dir + filestem + date + ".0000.021.nc4"
vars_name = ["SWE_inst", "CanopInt_inst", "AvgSurfT_inst", "SoilMoi",
             "SoilTMP"]

for var in range(len(vars_name)):
    if vars_name[var] == "SoilMoi" or vars_name[var] == "SoilTMP":
        os.system("ncks -v " + vars_name[var] + "0_10cm_inst " + filename +
                  " " + results_dir + "/GLDAS_" + vars_name[var] +
                  "_000-010_" + date + "00")
        os.system("ncks -v " + vars_name[var] + "10_40cm_inst " + filename +
                  " " + results_dir + "/GLDAS_" + vars_name[var] +
                  "_010-040_" + date + "00")
        os.system("ncks -v " + vars_name[var] + "40_100cm_inst " + filename +
                  " " + results_dir + "/GLDAS_" + vars_name[var] +
                  "_040-100_" + date + "00")
        os.system("ncks -v " + vars_name[var] + "100_200cm_inst " + filename +
                  " " + results_dir + "/GLDAS_" + vars_name[var] +
                  "_100-200_" + date + "00")
    else:
        os.system("ncks -v " + vars_name[var] + " " + filename +
                  " " + results_dir + "/GLDAS_" + vars_name[var] +
                  "_" + date + "00")

print("Successfully extracted initial variables")
