import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=['date'])

# Clean data
# Filter out days with top/bottom 2.5% of pageviews
df = df[
    (df['value'] <= df['value'].quantile(0.975)) &
    (df['value'] >= df['value'].quantile(0.025))
]


def draw_line_plot():
    # Draw line plot
    plt.style.use('fivethirtyeight')

    fig, ax = plt.subplots(figsize=(32, 8), dpi=72)
    ax.plot(df.index, df.values, linewidth=1.0)
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    # Add columns for month and year to dataframe
    df_bar = df.copy()
    # df_bar.reset_index(inplace=True)
  
    df_bar['month'] = df_bar.index.month
    df_bar['year'] = df_bar.index.year

    # Group data to display avg daily page views by month, grouped into years on the chart, then unstack index labels
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # List of months to be used for legend
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  
    # Draw bar plot
    fig = df_bar.plot.bar(figsize=(20, 20), legend=True, xlabel='Years', ylabel='Average Page Views').figure

    # Revise Legend titles and style
    plt.legend(months, fancybox=True, shadow=True, edgecolor='black', borderpad=0.75, borderaxespad=2.5, labelspacing=0.6)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(40, 16))

    sns.boxplot(data=df_box, x=df_box['year'], y=df_box['value'], linewidth=0.75, ax=axes[0])
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[0].set_title('Year-wise Box Plot (Trend)')

    # List of months for corectly-ordered data labels
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    sns.boxplot(data=df_box, x=df_box['month'], y=df_box['value'], linewidth=0.75, ax=axes[1], order=months)
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
  
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig