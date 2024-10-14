import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Setting up the figure
    fig, ax = plt.subplots(figsize=(10,6))

    x_lim=[1880, 2060]
    y_lim=[-2, 16]

    # Create scatter plot
    df.plot(x="Year", y="CSIRO Adjusted Sea Level",
            kind="scatter", marker="x", ax=ax, xlim=x_lim, ylim=y_lim)

    # Create first line of best fit
    linreg = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(range(1880, 2051, 1), linreg.slope*range(1880, 2051, 1) + linreg.intercept, color="black", label="All-time rate")

    # Create second line of best fit
    df_second = df[df["Year"] >= 2000]
    linreg_second = linregress(df_second["Year"], df_second["CSIRO Adjusted Sea Level"])
    plt.plot(range(2000, 2051, 1), linreg_second.slope*range(2000, 2051, 1) + linreg_second.intercept, color="green", linestyle="--", label="2000s rate")
    
    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Grid and legend
    x_major_ticks = pd.RangeIndex(1850.0, 2076.0, 25.0)
    x_minor_ticks = pd.RangeIndex(1850.0, 2076.0, 10.0)
    y_major_ticks = pd.RangeIndex(-2, 17, 2)
    y_minor_ticks = pd.RangeIndex(-2, 17, 1)

    ax.set_xticks(x_major_ticks)
    ax.set_xticks(x_minor_ticks, minor=True)
    ax.set_yticks(y_major_ticks)
    ax.set_yticks(y_minor_ticks, minor=True)

    ax.grid(which='both')
    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)

    ax.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
