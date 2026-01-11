import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # 1. Import the data
    df = pd.read_csv("epa-sea-level.csv")

    # 2. Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # 3. Line of best fit for all data
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred = np.arange(1880, 2051)
    y_pred = res.intercept + res.slope * x_pred
    plt.plot(x_pred, y_pred, 'r')

    # 4. Line of best fit from year 2000 onward
    df_recent = df[df["Year"] >= 2000]
    res_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )
    x_recent = np.arange(2000, 2051)
    y_recent = res_recent.intercept + res_recent.slope * x_recent
    plt.plot(x_recent, y_recent, 'g')

    # 5. Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # 6. Save and return plot
    plt.savefig("sea_level_plot.png")
    return plt.gca()
