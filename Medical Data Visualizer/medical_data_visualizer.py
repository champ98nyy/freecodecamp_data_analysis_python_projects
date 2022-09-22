import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column

# Calculate BMI, including first converting height from cm to m
bmi = df['weight']/((df['height'] / 100) ** 2)

# Add 'overweight column to df with value of 1 where bmi > 25, otherwise 0
df['overweight'] = np.where(bmi > 25, 1, 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)

df['gluc'] = np.where(df['gluc'] == 1, 0, 1)



# Draw Categorical Plot
def draw_cat_plot():

    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.melt(id_vars = ['cardio'], value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['cardio', 'value', 'variable'], as_index=False).count()
    

    # Draw the catplot with 'sns.catplot()'

    # Get the figure for the output
    fig = sns.catplot(x='variable', y='total', data=df_cat, hue='value', kind='bar', col='cardio').fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

  

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[
      (df['ap_lo'] <= df['ap_hi']) & 
      (df['height'] >= df['height'].quantile(0.025)) & 
      (df['height'] <= df['height'].quantile(0.975)) & 
      (df['weight'] >= df['weight'].quantile(0.025)) & 
      (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(16, 16))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, fmt=".1f", cmap='inferno', linewidths=1, mask=mask, center=0, cbar_kws={"label": "Correlation", "shrink": 0.6})


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
