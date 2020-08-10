#!/usr/bin/python
# Zhe Zhang
# 2020-04-21
# python script to extract gldas variables
# origional perl code from Mike's directory
# migrate from perl to python

import glob
import os

# Configure start and end day
day_start = 1
day_end = 3

# Set directories and file name
data_dir = "/opt/ARW/DATA/GLDAS/raw/netcdf/"
results_dir = "/opt/ARW/DATA/GLDAS/extracted/"
filestem = "GLDAS_NOAH025_3H.A"

# set years
cc = ["20"]
yrs = ["10"]

# create date arrays
nums = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09",
        "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
        "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
        "30", "31"]
hrs = ["00", "03", "06", "09", "12", "15", "18", "21"]
noleap_days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
leap_days = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]

# Set var names
vars_name = ["Rainf_tavg", "Snowf_tavg", "Wind_f_inst", "Tair_f_inst",
             "Qair_f_inst", "Psurf_f_inst", "SWdown_f_tavg", "LWdown_f_tavg"]
vars_short = ["Rainf", "Snowf", "Wind", "Tair", "Qair", "Psurf", "SWdown",
              "LWdown"]

for var in range(len(vars_name)):
    print("working on variable: ", vars_short[var])
    for yy in range(len(yrs)):
        for julday in range(day_start, day_end+1, 1):
            # check for leap years and select days
            modays = noleap_days
            if (yy == "92" or yy == "96" or yy == "00" or yy == "04" or
                yy == "08" or yy == "12" or yy == "16" or yy == "20" or
                yy == "24" or yy == "28" or yy == "32" or yy == "36" or
                    yy == "40" or yy == "44" or yy == "48"):
                modays = leap_days
            # Month loop
            for mo in range(0, 12, 1):
                if (julday > modays[mo] and julday <= modays[mo+1]):
                    day = (julday - modays[mo])
                    # Set month and day strings
                    if (mo < 9):
                        mon = "0"+str(mo+1)
                    else:
                        mon = str(mo+1)
                    if (day < 10):
                        day = "0"+str(day)
                    else:
                        day = str(day)
                    # Get ini files
                    infiles = sorted(glob.glob(
                        data_dir + filestem + cc[0] + yrs[yy] + (mon) + (day)
                        + "*"))
                    if (len(infiles) > 0):
                        intime = cc[0]+yrs[yy]+(mon)+(day)
                        infile_list = infiles
                    if not os.path.exists(results_dir + vars_short[var]):
                        os.system("mkdir " + results_dir + vars_short[var])
                    for hr in range(0, 8):
                        infile = infile_list[hr]
                        outfile = results_dir + vars_short[var] + "/GLDAS_" + \
                            vars_name[var] + "_" + intime + hrs[hr]
                        if not os.path.exists(outfile):
                            print("writing file: ", outfile)
                            os.system("ncks -v " + vars_name[var] + " "
                                      + infile + " " + outfile)
                        else:
                            print("file exist, move to next one")

print("Successfully extracted necessary variables!")
