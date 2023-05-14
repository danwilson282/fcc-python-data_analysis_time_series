import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] =  pd.to_datetime(df['date'])
df=df.set_index('date')

# Clean data
df = df.loc[(df['value']>=df['value'].quantile(0.025)) & (df['value']<=df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, axes = plt.subplots(figsize=(12,6))
    axes.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    axes.set_xlabel('Date')
    axes.set_ylabel('Page Views')
    sns.lineplot(data=df, x='date', y='value', color='red')
    



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar["Years"] = df_bar.index.year
    df_bar["Months"] = df_bar.index.month_name()
    df_bar = df_bar.groupby([df_bar['Years'], df_bar['Months']], sort=False)['value'].mean().reset_index()
    df_bar = df_bar.rename(columns={"value": "Average Page Views"})

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12,6))
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    sns.barplot(data=df_bar, x="Years", y="Average Page Views", hue="Months", hue_order=month_order)
    plt.legend(loc = 'upper left', title = 'Months')
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
    fig, axes = plt.subplots(1, 2, figsize=(12,6))
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(data=df_box, x="year", y="value", ax=axes[0])
    sns.boxplot(data=df_box, x="month", y="value", ax=axes[1], order=month_order)
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
