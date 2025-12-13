#!/usr/bin/env python3

# Data frames.
import pandas as pd

# Dates and times.
import datetime as dt

# Plotting
import matplotlib.pyplot as plt

# Listing files in a folder.
import os

# Yahoo Finance data.
import yfinance as yf

tickers = ["META","AAPL","AMZN","NFLX","GOOG"]
# Function get_data
def get_data():

    # Get data.
    df = yf.download(tickers,period="5d",interval="1h",auto_adjust=False)

    # Create data folder if it doesn't already exist
    os.makedirs("data", exist_ok=True)

    # Format date and time.
    now = dt.datetime.now()

    # create file name with format YYYYMMDD-HHmmss
    filename = now.strftime("%Y%m%d-%H%M%S")

    # Save data as csv in folder data
    df.to_csv(f"data/{filename}.csv")
    print(f"The file {filename} is now in folder 'data'.")
    return


# Function plot_data
def plot_data():

    # List the files in the data folder.
    data_files = os.listdir('data')

    # Sort the list of files.
    data_files=sorted(data_files, reverse=True)

    # The latest file.
    latest_file = data_files[0]

    # Read the CSV file.
    df = pd.read_csv(f'data/{latest_file}', header=[0, 1], index_col=0, parse_dates=True)
    df.head()

    # Create 'plots' folder if it doesn't already exist
    os.makedirs("plots", exist_ok=True)

    # Plot the Close price.
    plt.figure(figsize=(15,7))
    
    df['Close'].plot(marker='*')
    plt.title("Close price over the last 5 days - from " + latest_file)
    plt.xlabel('Date')
    plt.ylabel('Close price')
    plt.grid(axis = 'x', color = 'green', linestyle = '--', linewidth = 0.4)
    plt.legend(title="Stocks",fontsize='small',bbox_to_anchor=(1,0.7))
    plt.tight_layout()

    # Name of the plot
    plot_name = latest_file[:-4]
    # put a copy of the image of the plot (.png file) into the `plots` folder in the root of my repository
    plt.savefig(f"plots/{plot_name}.png")

    plt.show()

    print(f"The plot of the Close price of FAANG in {latest_file} is now saved in folder 'plot'.")

    return


def main():
    # Run the function and capture the data frame
    get_data()
    # Run the function and capture the plot
    plot_data()

if __name__ == "__main__":
    main()