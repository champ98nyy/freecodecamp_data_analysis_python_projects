import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', index_col='Year')

    # Assign relevant data series to variable for simplicity in plotting syntax
    year = df.index  
    sea_level = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 10))

    plt.scatter(year, sea_level)

    # Create first line of best fit
  
    # Use linregress function to determine slope, intercept
    res = linregress(year, sea_level)
    slope = res.slope
    intercept = res.intercept

    # Create numpy array that includes all years from 1880 - 2051
    all_years = np.arange(1880, 2051)

    """
    Use Slope-Intercept Form linear equation to graph the line
    y = mx + c 
    m --> slope 
    c --> y-intercept   
    """

    line_1 = slope*all_years + intercept

    # Plot the first line of best fit and make it green
    plt.plot(all_years, line_1, 'g')


    # Create second line of best fit
  
    # Subset data to only include records from the year 2000 or greater
    year_2000_up = df.loc[df.index >= 2000]

    # Assign relevant data series to variable for simplicity in plotting syntax
    year_2 = year_2000_up.index
    sea_level_2 = year_2000_up['CSIRO Adjusted Sea Level']

    # Use linregress function to determine slope, intercept
    res_2 = linregress(year_2, sea_level_2)
    slope_2 = res_2.slope
    intercept_2 = res_2.intercept

    # Create numpy array that includes all years from 2000 - 2051
    all_years_2 = np.arange(2000, 2051)

    # Use Slope-Intercept Form linear equation to graph the 2nd line
    line_2 = slope_2*all_years_2 + intercept_2
    plt.plot(all_years_2, line_2, 'r')

    # Add labels and title to graph
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()