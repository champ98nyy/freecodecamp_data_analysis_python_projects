# Page View Time Series Visualizer

For this project, Pandas, Matplotlib and Seaborn were used to analyze and visualize a dataset containing the number of page views/day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03.
By visualizing the time series data using a line chart, bar chart and box plots, I was able to identify patterns in visits and identify yearly and monthly growth.

## Tasks
The data was used to complete the following tasks:

- Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the `date` column.
- Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
- Create a `draw_line_plot` function that uses Matplotlib to draw a line chart. The title should be `Daily freeCodeCamp Forum Page Views 5/2016-12/2019`. The label on the x axis should be `Date` and the label on the y axis should be `Page Views`.
- Create a `draw_bar_plot` function that draws a bar chart. It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of `Months`. On the chart, the label on the x axis should be `Years` and the label on the y axis should be `Average Page Views`.
- Create a `draw_box_plot` function that uses Seaborn to draw two adjacent box plots. These box plots should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be `Year-wise Box Plot (Trend)` and the title of the second chart should be `Month-wise Box Plot (Seasonality)`. Make sure the month labels on bottom start at `Jan` and the x and y axis are labeled correctly. The boilerplate includes commands to prepare the data.

Full instructions for this project from freecodecamp.org can be found [here](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/page-view-time-series-visualizer)

![TEMP](https://github.com/champ98nyy/freecodecamp_data_analysis_python_projects/blob/master/Page%20View%20Time%20Series%20Visualizer/bar_plot.png?raw=true)
