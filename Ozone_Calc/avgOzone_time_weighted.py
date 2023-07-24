# A. Ukhin - July 12, 2023
# Average Ozone Calculation for Aquaplanet config
# This script creates an average between all time OZ values and then averages opposite ends of lat. values for OZ(one) values 
import xarray as xr
import numpy as np
import os
import matplotlib.pyplot as plt

# Input and output file names
in_file = "cmip6_radozone_picontrol_1850_monthly_128_64.999.nc"
out_file = "avgOzoneCalc_TIME_WEIGHTED_Results.nc"
# Open input file to work with data inside of it
data = xr.open_dataset(in_file)
# Create a copy for data
data_copy = data.copy()

# OZ(Ozone) is a float (with a negative exponential)
OZ_data = data['OZ']
# Create a copy of OZ_data so as to not modify the original
# This is a seperate copy from data_copy as it is meant to work with
OZ_data_copy = OZ_data.copy()

#(tim)e first first, Pressure Level (plev) second, (lat)itude third, (lon)gtitude last in array
month_day_weights = [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31]
weights_month = xr.DataArray(month_day_weights, dims='time', coords={'time': OZ_data_copy.time})
#OZ_weighted = weights_month.dot(OZ_data_copy)/427.0
OZ_weighted = OZ_data_copy.dot(weights_month)/427.0
# Update weighted time values
OZ_data_copy[:, :, :, :] = OZ_weighted

# This loop goes through all pressure index values
for plev_index in range(data_copy.dims['plev']):
    # Subset of 1 defined index (OZ[:, defined_plev_index, :, :])
    # ":" Represents for all possible values
    # Purpose of creating a subset is to be able to work within a specific index without needing to
    # explicitly define the index of, for example, plev (Pressure Level) each subsequent time it is used
    subset_pressure = OZ_data_copy.isel(plev=plev_index)
    # Loop through lat. values to equator
    for lat_index_bot in range(32):
        lat_index_top = 63 - lat_index_bot
        # This uses the 2 indexes to extract the value of Ozone (subset_time['OZ'].isel(lat = X)) at value X
        OZ_lat_avg_calc = (subset_pressure.isel(lat = lat_index_bot) + subset_pressure.isel(lat = lat_index_top))/2
        # This section adds the avg. value calculated above into the specific index of the Ozone data
        OZ_data_copy[:, plev_index, lat_index_bot, :] = OZ_lat_avg_calc
        OZ_data_copy[:, plev_index, lat_index_top, :] = OZ_lat_avg_calc


# Write results to file
OZ_data_copy.to_netcdf(out_file, 'w')
dataOut = xr.open_dataset(out_file)
print("\nFile named " + out_file + " succesfully written to directory:\n" + os.path.abspath(out_file) + "\n")

std_max = 1.185E-08
std_min = 1.0E-05

# Subset of the original data to generate a plot
subset_origin = OZ_data.isel(time = 0, lon = 21)
subset_origin_values = subset_origin.values
image_out_name = "OZ_CONTROL_HARDCODE_WEIGHT.png"
# Parameters for control graph
'''
vmin=subset_origin.min()  # These are values to be used for the explicit max and min of a graph
vmax=subset_origin.max()  #  They are replacements for the hardcoded values used for standardization
'''
plt.figure(figsize=(8, 6))
plt.imshow(subset_origin_values, cmap='jet', vmin=std_min, vmax=std_max)
plt.colorbar(label='OZ values')
plt.title(f'Ozone Data: Time = 0, Pressure Level = 20, Lat = 0, Lon = 0')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig(image_out_name)
print(image_out_name + " generated")

# Subset of the modified data to generate a plot
subset_copy = OZ_data_copy.isel(time = 0, lon = 0)
subset_copy_values = subset_copy.values
mod_image_out_name = "OZ_CALCULATED_HARDCODE_WEIGHT.png"
# Parameters for modified graph
'''
vmin=subset_copy_values.min()
vmax=subset_copy_values.max()
'''
plt.figure(figsize=(8, 6))
plt.imshow(subset_copy_values, cmap='jet', vmin=std_min, vmax=std_max)
plt.colorbar(label='Modified OZ values')
plt.title(f'Ozone Data: Time = 0, Pressure Level = 20, Lat = 0, Lon = 0')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig(mod_image_out_name)
print(mod_image_out_name + " generated\n")
