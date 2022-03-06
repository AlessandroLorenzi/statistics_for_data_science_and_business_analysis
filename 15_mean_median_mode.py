#!/usr/bin/env python

import pandas as pd

annual_income = pd.Series(
    [
        62000.00,
        64000.00,
        49000.00,
        324000.00,
        1264000.00,
        54330.00,
        64000.00,
        51000.00,
        55000.00,
        48000.00,
        53000.00,
    ]
)

print(annual_income)
print("Mean  : %f" % annual_income.mean())
print("Median: %f" % annual_income.median())
print("Mode  : %f" % annual_income.mode())
