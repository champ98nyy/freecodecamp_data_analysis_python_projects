
# Sea Level Predictor

For this project, I was tasked with predicting sea level change through the year 2050. Using Pandas, Matplotlib and SciPy I analyzed and visualized data on the Global Average Absolute Sea Level Change from 1880 - 2014.



## Tasks
The data was used to complete the following tasks:

- Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the `date` column.
- Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
- Create a `draw_line_plot` function that uses Matplotlib to draw a line chart. The title should be `Daily freeCodeCamp Forum Page Views 5/2016-12/2019`. The label on the x axis should be `Date` and the label on the y axis should be `Page Views`.
- Create a `draw_bar_plot` function that draws a bar chart. It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of `Months`. On the chart, the label on the x axis should be `Years` and the label on the y axis should be `Average Page Views`.
- Create a `draw_box_plot` function that uses Seaborn to draw two adjacent box plots. These box plots should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be `Year-wise Box Plot (Trend)` and the title of the second chart should be `Month-wise Box Plot (Seasonality)`. Make sure the month labels on bottom start at `Jan` and the x and y axis are labeled correctly. The boilerplate includes commands to prepare the data.

## Data Source
Data Source
[Global Average Absolute Sea Level Change, 1880-2014](https://datahub.io/core/sea-level-rise) from the US Environmental Protection Agency using data from CSIRO, 2015; NOAA, 2015.

Full instructions for this project from freecodecamp.org can be found [here](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/sea-level-predictor)
