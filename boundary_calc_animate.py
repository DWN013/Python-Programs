# ===================================================================================
# boundary_calc_animate.py
# A. Ukhin - August 8, 2023
# -----------------------------------------------------------------------------------
# Brief Description of Program:
# Generates plots and animations to display water vapour movement over an arbitrary 
# timespan from a .nc file and applies it over a Robinson projection of Earth with a 
# gist_yarg colour map 
# ===================================================================================
# Libraries necessesary for program
import xarray as xr
import re
import numpy as np
import os
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from matplotlib.animation import FuncAnimation
import glob
# ===================================================================================
# Gets README file for use of program
def get_README():
    try:
        with open("README.txt", 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File 'README.txt' not found.")
# ===================================================================================
# Generates pngs from a folder or file depending on user input
# Folder/File can be hardcoded or user input in a specific directory
def generate_pngs():
    # Asks if user needs to generate plot(s) from singular file or folder with multiple .nc files
    generation_from = str.lower(input("Are you generating from a folder? (No if only from one file)\n(Y)es\n(N)o\nAny other key to exit\n"))
    if(generation_from != 'y' and generation_from != 'n'): (exit())
    use_default = input("Use default directory?\n(Y)es\n(N)o\nAny other key to exit\n")
    # Gets input for if using default or custom parameters
    custom = str.lower(input("Set custom plot parameters?\n(Y)es\n(N)o or any other key (Uses system defaults)\n"))
    # Decision for if folder and if custome PATH or default
    if(use_default == 'y'):
        # Following lines use hardcoded path
        if(generation_from == 'y'):
            create_plots_from_folder(file_folder_path, custom)
        elif(generation_from == 'n'):
            create_plots_from_file(file_path, custom)
    elif(use_default == 'n'):
        # Following lines get input path
        if(generation_from == 'y'):
            create_plots_from_folder(input("Input folder path where files are located (/path/example/here)\n"), custom)
        elif(generation_from == 'n'):
            create_plots_from_file(input("Input file path (/path/example/here/file.nc)\n"), custom)
    else:
         exit()
    print("Saved plots")
# ===================================================================================
# Gets a sorted list of files and returns it
def get_sorted_png_files():
    # Glob module searchs for files that match a specific file pattern or name
    png_files = glob.glob("*.png")
    # Sorts by name, as such leading zeroes are required to ensure a correct sort
    png_files.sort()
    return png_files
# ===================================================================================
# Animation function definition
def animate(frame):
    plt.clf()  # Clears the previous frame, WILL NOT WORK WITHOUT!
    # Put together frames
    plt.imshow(plt.imread(png_files[frame]))
    # Remove axis from animated plot
    plt.axis('off')
# ===================================================================================
# Creates plots from a singular .nc file, assumes 365 days in a year but will work with a (theoretically) infinite amount ot timesteps without issue.
def create_plots_from_file(input_file_path, iscustom):
    # Head (folder path) is unused, tail is actual filename
    head, tail = os.path.split(input_file_path)
    # Open dataset for work
    dataset = xr.open_dataset(input_file_path)
    size_of_time = dataset['prw'].time.size
    # Default definitions for start/end time to go through all timesteps by default
    start_size_of_time = 0
    end_size_of_time = size_of_time
    # Default colourmap
    cust_cmap = "gist_yarg"
    # If is_custom is 'y' sets custom parameters
    if(iscustom == 'y'):
        # Ask user here about how many months/years they want to generate
        print(f"\nTotal timesteps: {size_of_time}\n")
        start_size_of_time = int(input("What timestep to start run at?\nTimestep num: "))
        end_size_of_time = int(input("What timestep to end run at?\nTimestep num: "))
        #  Custom cmap may be set here, default is gist_yarg
        cust_cmap = input(f"Set custom colourmap (Press enter to use default)\n(Default is currently {cust_cmap}):\n")
        # Assigns default value if no input is used
        if(0 == len(cust_cmap)): cust_cmap = "gist_yarg"
        print(f"\nPlotting with cmap {cust_cmap}\n")
    # Loops from 0 - 364
    for time_step in range(start_size_of_time, end_size_of_time):
                    # Subset of the original data to generate a plot
                    # Squeezes down data to useable format for .plot()
                    subset_origin = dataset['prw'].isel(time = time_step).squeeze()
                    image_out_name = tail.replace(".nc", "")
                    # Params for naming end of file number
                    num_name = time_step
                    total_timesteps = size_of_time
                    # Calculates amount of leading zeroes to add to plot filenames
                    # Starts at 1 instead of 0 since 10**0 == 1, creates pointless calculation
                    leading_zero_amnt = 1
                    # Performs floor division by factors of 10 while result is more than zero
                    while((total_timesteps // 10**leading_zero_amnt) > 0):
                        leading_zero_amnt += 1
                    # Prevents an extra zero from being added
                    leading_zero_amnt -= 1
                    num_result = num_name
                    # Creates final number string for proper sorting
                    for i in range(leading_zero_amnt):
                        if(num_name < (10**leading_zero_amnt)):
                            num_result = "0" + str(num_result)
                            leading_zero_amnt -= 1
                    # Creates final file name
                    # Finds location of last "_" character
                    index = image_out_name.rfind("_")
                    if index != -1:
                        image_out_name = image_out_name[index + 1:]
                    else:
                        print("\nNo underscore found in the string!\nUsing default file name!\n")
                    image_out_name = image_out_name + f"_{num_result}.png"
                    # Visual parameters for plot
                    robinson_proj = ccrs.Robinson()
                    # Selection of which projection to use, uncomment xyz_proj and replace variable name in plt.subplots(subplot_kw={xyz}) line
                    #merc_proj = ccrs.Mercator()
                    fig, ax = plt.subplots(subplot_kw={'projection': robinson_proj})
                    # Function to create the plot based on the data from the .nc file
                    # ax is the axes variable, transform creates a transformation of the data relevant to the projection used and is reccomended as 
                    # a standard inclusion regardless of projection, vmin and vmax provide min and max values for the colorbar, cmap provides the colour map to be used for the plot
                    # extend adds arrows to both ends of the colorbar to show out of bounds values
                    subset_origin.plot(ax=ax, transform=ccrs.PlateCarree(), vmin=std_min, vmax=std_max, cmap=cust_cmap, extend='both')
                    ax.coastlines()
                    ax.gridlines()
                    fig.savefig(image_out_name)
# ===================================================================================
# Function to create mutltiple plots from all files in a folder
# Uses function create_plots_from_file() as a sub-function
def create_plots_from_folder(path, iscustom):
    for filename in os.listdir(path):
        if filename.endswith('.nc'):
            file_path = os.path.join(path, filename)
            # Checks if file path exists and calls file path with create_plots_from_file() function
            if os.path.isfile(file_path):
                create_plots_from_file(file_path, iscustom)
# ===================================================================================
# Hardcoded paths to folder/file, replace as needed
file_folder_path = "/space/hall5/sitestore/eccc/crd/ccrn/users/jcl001/jcl-retro-pi1850-1d0/data/nc_output/CMIP6/CCCma/CCCma/CanESM5-jcl-retro-pi1850-1d0/piControl/r1i1p1f1/Eday/prw/gn/v20190429"
file_path = "/space/hall5/sitestore/eccc/crd/ccrn/users/jcl001/jcl-retro-pi1850-1d0/data/nc_output/CMIP6/CCCma/CCCma/CanESM5-jcl-retro-pi1850-1d0/piControl/r1i1p1f1/Eday/prw/gn/v20190429/prw_Eday_CanESM5-jcl-retro-pi1850-1d0_piControl_r1i1p1f1_gn_32500101-32501231.nc"
# ===================================================================================
# Bounds for graph colourbars, can be changed depending on the data used
std_min = 5
std_max = 85
# ===================================================================================
print("===================================================================================")
action = input("Select an action:\n1. Generate files and animation\n2. Generate files\n3. Generate animation\n4. View instructions in README file\nStop program (any other key)\n")
print("===================================================================================")
# If action with animation animation name is prompted and confirmed
if(action == '1' or action == '3'): 
    gif_name = input("Name the GIF file: (Leave blank for default \'test.gif\' name)\n")
    if(0 == len(gif_name)): gif_name = "test"
    print(f"\nAnimation will be named {gif_name}.gif\n")
# Defined actions to be taken
if((action) == '1'):
    # Generates plot(s) in png(s) from .nc file(s)
    generate_pngs()
    # Gets sorted files for use in animation
    png_files = get_sorted_png_files()
    # Function that returns a tuple containing a figure and axes objects
    # figX is a figure that controls the properties of the animation (size, title, etc.)
    # ax2 is unused as of current.
    figX, ax2 = plt.subplots()
    # Use FuncAnimation library to stich together png's
    animation = FuncAnimation(figX, animate, frames=len(png_files), interval=100)
    animation.save(f"{gif_name}.gif", writer='pillow')
    print("Created animated results")
elif((action) == '2'):
    # Generates plot(s) in png(s) from .nc file(s)
    generate_pngs()
elif((action) == '3'):
    # Gets sorted list of files for use in animation
    png_files = get_sorted_png_files()
    # Function that returns a tuple containing a figure and axes objects
    # figX is a figure that controls the properties of the animation (size, title, etc.) as well as to save the image
    # ax2 is unused as of current.
    figX, ax2 = plt.subplots()
    animation = FuncAnimation(figX, animate, frames=len(png_files), interval=100)
    animation.save(f"{gif_name}.gif", writer='pillow')
    print("Created animated results")
elif((action) == '4'):
    get_README()
# Debug action to view order of files, not necessary to run program
#elif((action) == '5'):
#     sorted_files = get_sorted_png_files()
#     for i in range(len(sorted_files)):
#         print(sorted_files[i])
# Kills program
else:
    exit()
# ===================================================================================