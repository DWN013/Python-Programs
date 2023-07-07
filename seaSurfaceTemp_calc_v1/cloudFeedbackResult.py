# A. Ukhin - July 4, 2023
# Version 1.0 of an implementation of a formula for use in netCDF file work

import xarray as xr
import math
import os

# Paper title:
# The Cloud Feedback Model Intercomparison Project (CFMIP) contribution to CMIP6
# doi:10.5194/gmd-10-359-2017
# Function calculate_T() taken from Appendix B, equation B1

# Tested and confirmed results to correlate to control results on:
# https://www.met.reading.ac.uk/~mike/APE/ape_spec_sst_2.pdf

# Only variable that affects results is latitude?

# REMINDER
# Python uses radians for calculations so conversion from degrees is necessary Ex. (x * math.pi)/180
#(lat)itude first, (lon)gtitude second, (tim)e third in array and is counter in months

def calculate_T1():

    for current_lat_val in range (len(GT_atm_copy['lat'])):
        #x = float(input("Input the latitude:\n"))
        
        #x = current_lat_val
        
        # Convert x to radians 
        x = (current_lat_val * math.pi)/180
        # Function definitions
        xmax = math.pi/3
        y = (math.pi/2) * (x/xmax)
        Tmin = 0  # T(min) == O degrees C
        Tmax = 27 # T(max) == 27 degrees C
        bT = Tmax - Tmin # This is just 27 degrees

        # Calculation of formula
        T_func = 0.5 * (2 - (math.sin(y)**4) - (math.sin(y)**2)) * bT

        # Return result
        # if |φ| < π/3:
        if abs(x) < xmax:
            GT_atm_copy[:, current_lat_val, :] = T_func
        # Otherwise if |φ| > π/3  return 0:
        else:
            GT_atm_copy[:, current_lat_val, :] = 0

# This function is responsible for determining which forumla the user requests and can be added to in future if more formulas are desired
# Additional formulas can be added by defining a function name below the most recent function/formula using def FUNC_NAME():
# Then adding the function call and incrementing the number below
def function_selection(num):    
    if (num == 1): 
        calculate_T1()
    
    # Ex. new function template:
    # elif (num == n+1):
    #   NAME_OF_FUNC()

    else:
        raise ValueError("Invalid input, check the formula you're attempting to select is valid and properly implemented.")
        

in_file = "CONDITIONS_v1.nc.999"
out_file = "cloud_feedback_v1_results.nc"
data = xr.open_dataset(in_file)

GT_atm = data['GT_atm']
SICN_atm = data['SICN_atm']
SIC_atm = data['SIC_atm']  #SIC == Sea Ice Concentration

GT_atm_copy = GT_atm.copy()
SICN_atm_copy = SICN_atm.copy()
SIC_atm_copy = SIC_atm.copy()

SICN_atm_copy[:] = 0.0
SIC_atm_copy[:] = 0.0

# Writes to GT_atm_copy once a function is selected with an SST formula
what_form = int(input("Which SST forumla is needed? (select a number between 1-1):\n"))
function_selection(what_form)

modified_ds = xr.Dataset({'GT_atm': GT_atm_copy, 'SICN_atm': SICN_atm_copy, 'SIC_atm': SIC_atm})

modified_ds.to_netcdf(out_file, 'w')

dataOut = xr.open_dataset(out_file)
print("\nFile named " + out_file + " succesfully written to directory:\n" + os.path.abspath(out_file) + "\n")