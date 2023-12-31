""" yf_example3.py

Downloads stock price data for Qantas for a given year and save the information in a
CSV file
"""

import os

import toolkit_config
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year):
    """  Download Qantas stock prices for a given year into a CSV file.

        Parameters
        ----------
        year : int
            An integer with a four-digit year
        """
    pth = os.path.join(toolkit_config.DATADIR, f'qan_prc_{year}.csv')
    start = f"{year}-01-01"
    end = f"{year}-12-31"
    yf_example2.yf_prc_to_csv("QAN.AX", pth, start, end)

if __name__ == "__main__":
    year = 2020
    qan_prc_to_csv(year)