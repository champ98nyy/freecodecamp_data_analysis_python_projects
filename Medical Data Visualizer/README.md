# Medical Data Visualizer

For this project,Pandas, Matplotlib and Seaborn were used to analyze and visualize patient data collected during medical examinations. I explored the relationship between cardiac disease, body measurements, blood markers and lifestyle choices.

## Tasks
- Create a chart where we show the counts of good and bad outcomes for the `cholesterol`, `gluc`, `alco`, `active`, and `smoke` variables for patients with cardio=1 and cardio=0 in different panels.

Use the data to complete the following tasks in `medical_data_visualizer.py`:

- Add an `overweight` column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
- Normalize the data by making 0 always good and 1 always bad. If the value of `cholesterol` or `gluc` is 1, make the value 0. If the value is more than 1, make the value 1.
- Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's `catplot()`. The dataset should be split by 'Cardio' so there is one chart for each `cardio` value. 

- Clean the data. Filter out the following patient segments that represent incorrect data:
   - diastolic pressure is higher than systolic
   - height is less than the 2.5th percentile
   - height is more than the 97.5th percentile
   - weight is less than the 2.5th percentile
   - weight is more than the 97.5th percentile
- Create a correlation matrix using the dataset. Plot the correlation matrix using seaborn's `heatmap()`. Mask the upper triangle.

Full instructions for this project from freecodecamp.org can be found [here](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer)
