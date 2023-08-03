# ===================================================================================
# boundary_calc.py
# A. Ukhin - July 25, 2023
# -----------------------------------------------------------------------------------
# Brief Description of Program:
# This script takes a netCDF file (.nc) as input and iterates over each value in the
# DataArray subtracts the sst_control variable from the sst_patch_ variables to get 
# the perturbation in SST.
# After this, is saves the results for the specifc perturbation in a seperate file
# sst_patch_(n) where n in sst_patch is a value denoting what specific sst_patch is being reffered to.
# SST == "Sea Surface Temperature", patch meaning the specific square of the sea with data on that square.
# ===================================================================================
import xarray as xr
import numpy as np
import os
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy
import matplotlib.colors as colors

# Input and output file names
in_file = "gfmip_boundary_conditions.nc"
# Grid to use
file_target_grid="/home/jcl001/CanAM5_grid.txt"
# Open input file to work with data inside of it
data = xr.open_dataset(in_file)
# Variables: (time, lat, lon)

# ===================================================================================
# This loop is used to iterate over each variable in the dataset "data" and subtract
# to create a perturbation.
# ===================================================================================
# Size for coord arrays
start_name = "gfmip_bc_"

for sst_patch_name in data.data_vars:
    if sst_patch_name.startswith("sst_patch_"):
        # File name for result
        new_patch_name = sst_patch_name.replace(".", "d")
        new_patch_name = new_patch_name.replace("-", "m")
        out_file = start_name + new_patch_name + ".nc"
        var_data = data.variables[sst_patch_name]
        # Subtracts patch from control values
        data_out = data[sst_patch_name]- data['sst_control']
        data_out = data_out.rename("gt_atm") 
        # Write results to file (temp)
        data_out.to_netcdf(out_file, 'w')

        # Write results to file (temp)
        new_name = out_file.replace("sst_", "sst_t63_")
        out_cmd = f"cdo remapcon,{file_target_grid} {out_file} {new_name}"
        os.system(out_cmd)

        #Min and Max values for graph
        std_min = -2
        std_max = 2
        # Opens the 2 newly created datasets (interpolated and original) for reading
        patch_data = xr.open_dataset(out_file)
        t63_patch_data = xr.open_dataset(new_name)

        origin_dataset = patch_data['gt_atm'].isel(time = 0)
        t63_dataset = t63_patch_data['gt_atm'].isel(time = 0)

        #ccrs.PlateCarree()
        robinson_proj = ccrs.Robinson()

        # Create a figure with two subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), subplot_kw={'projection': robinson_proj})
        ax1.set_xlabel('Longitude'), ax1.set_ylabel('Latitude')
        ax2.set_xlabel('Longitude'), ax2.set_ylabel('Latitude')

        # Remove .nc from filenames
        out_file = out_file.replace(".nc", "")
        new_name = new_name.replace(".nc", "")

        # Plot gt_atm from gfmip_bc_sst_patch_
        origin_dataset.plot(transform=ccrs.PlateCarree(), ax=ax1, extend='both', cmap='bwr', center=0, vmin=std_min, vmax=std_max)
        ax1.set_title(out_file)
        ax1.coastlines()

        # Plot gt_atm from gfmip_bc_sst_t63_patch
        t63_dataset.plot(transform=ccrs.PlateCarree(), ax=ax2, extend='both', cmap='bwr', vmin=std_min, vmax=std_max)
        ax2.set_title(new_name)
        ax2.coastlines()

        # Chart name includes variables that define location of patch
        chart_name = out_file + "_time_0"
        # Save the plots
        plt.savefig(chart_name)