# A. Ukhin - July 12, 2023
# Average Ozone Calculation for Aquaplanet config
# This script create an average between opposite ends of lat. values for Ozone 

import xarray as xr
import numpy as np
import os
import matplotlib.pyplot as plt

in_file = "cmip6_radozone_picontrol_1850_monthly_128_64.999.nc"
out_file = "avgOzoneCalcResults.nc"
data = xr.open_dataset(in_file)
data_copy = data.copy()

# OZ(Ozone) is a float (with a negative exponential)
OZ_data = data['OZ']
OZ_data_copy = OZ_data.copy()

#(tim)e first first, Pressure Level (plev) second, (lat)itude third, (lon)gtitude last in array
# time, pressure, lat, lon

# This loop goes through all pressure index values
for plev_index in range(data_copy.dims['plev']):
    subset_pressure = data_copy.isel(plev=plev_index, lon=0)

    # This loop goes through all time index values
    for time_index in range(data_copy.dims['time']):

        subset = subset_pressure.isel(time=time_index)

        # Where x is a desired latitude range (x = 0 to 31, y = 63 to 32)
        # This loop goes through latidue values up till it reaches the equator, it calculates the avg. with the latitude value
        # opposite of it (ex. 0 and 63, 1 and 62, ... 31 and 32)
        for lat_index_bot in range(32):
            lat_index_top = 63 - lat_index_bot
            OZ_avg_calc = (subset['OZ'].isel(lat = lat_index_bot) + subset['OZ'].isel(lat = lat_index_top))/2
            OZ_data_copy[time_index, plev_index, lat_index_bot, :] = OZ_avg_calc
            OZ_data_copy[time_index, plev_index, lat_index_top, :] = OZ_avg_calc

OZ_data_copy.to_netcdf(out_file, 'w')
dataOut = xr.open_dataset(out_file)

print("\nFile named " + out_file + " succesfully written to directory:\n" + os.path.abspath(out_file) + "\n")

# Subset of the original data to generate a plot
subset_origin = OZ_data.isel(time = 0, lon = 21)
subset_origin_values = subset_origin.values

plt.figure(figsize=(8, 6))
plt.imshow(subset_origin_values, cmap='jet', vmin=subset_origin_values.min(), vmax=subset_origin_values.max())
plt.colorbar(label='OZ values')
plt.title(f'Ozone Data: Time = 0, Pressure Level = 20, Lat = 0, Lon = 0')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('ozone_plot_origin.png')
print("ozone_plot_origin.png generated")

# Subset of the modified data to generate a plot
subset_copy = OZ_data_copy.isel(time = 0, lon = 0)
subset_copy_values = subset_copy.values

plt.figure(figsize=(8, 6))
plt.imshow(subset_copy_values, cmap='jet', vmin=subset_copy_values.min(), vmax=subset_copy_values.max())
plt.colorbar(label='Modified OZ values')
plt.title(f'Ozone Data: Time = 0, Pressure Level = 20, Lat = 0, Lon = 0')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('ozone_plot_modified.png')
print("ozone_plot_modified.png generated")
