import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 10))
    df.plot(x="Year", y="CSIRO Adjusted Sea Level", kind="scatter", ax=ax)

    # Create first line of best fit
    x1 = pd.Series(range(df["Year"].iloc[0], 2051))
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    y1 = intercept + slope * x1
    plt.plot(x1, y1, 'r', label='Fitted Line 1')

    # Create second line of best fit
    recent_data = df[df["Year"] >= 2000]
    x2 = pd.Series(range(2000, 2051))
    slope, intercept, r_value, p_value, std_err = linregress(recent_data["Year"], recent_data["CSIRO Adjusted Sea Level"])
    y2 = intercept + slope * x2
    plt.plot(x2, y2, 'g', label='Fitted Line 2')

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()