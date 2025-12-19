# FAANG Stock Data Automation
Author: Quyen Phan

This repository contains a command-line–based workflow that automates the retrieval and visualization of recent stock market data for 5 major tech companies FAANG 
- Facebook (META)
- Apple (AAPL)
- Amazon (AMZN)
- Netflix (NFLX)
- Google (GOOG)

The project is designed to run as a single executable script, downloading data and plots in a structured and repeatable way. It can be executed manually from the terminal or automatically on a scheduled basis using GitHub Actions. 

To keep generated outputs organised, data files are store in [data]{https://github.com/quyenphanlyons/ci-assessment/tree/main/data}, plot files are store in [plots]{https://github.com/quyenphanlyons/ci-assessment/tree/main/plots}


## The purpose of this repository:

Data collection: Download recent hourly stock market data for FAANG companies using yfinance Python package and store the data in a structured and timestamped format

Data visualisation: Plot the Close prices of all FAANG stocks on a single chart.

Executable Script: Make the process run with a single command in the terminal.

Automation: Schedule the script to run weekly using GitHub Actions.

Automate execution on a weekly schedule using GitHub Actions

This workflow ensures that stock data and visualizations are always up-to-date without manual intervention.


## Dependencies

The script requires:

Python 3.x

yfinance

pandas

matplotlib
