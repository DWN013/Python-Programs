=======================================================================================================
README generated on Aug. 18, 2023
Plot animation program written by Alexander Ukhin on August 8, 2023

General program information:
This program generates plots and animations to display water vapour movement over some arbitrary length 
timespan from a .nc file and applies it over a Robinson projection of Earth with a gist_yarg colour map.


Specific details for functions
-------------------------------------------------------------------------------------------------------
For functions 1, 3
When generating a new animation ensure the previous png plots have been removed via rm *.png.
If not removed animations may generate in an incorrect order and create a buggy appearing animation.

For functions 1, 2
When generating new files, ensure that the filename of the model is different if multiple models are 
being used as the plots rely on the end numerical values to categorize data for the animation.

If setting a custom amount of steps specify 2 ranges: The start (ex. 0) and end (ex. 2920)
Plots will theoretically scale to an infinite number of steps and can be animated disjointly
so long as it is from the same .nc file (eg. timesteps 0-1000 and 2000-3000 can be combined in 1 gif)

Colour map can be changed after selecting "y" for using custom parameters
NOTE: Program does not check if colour map input is valid and will crash if invalid input is provided!

=======================================================================================================
