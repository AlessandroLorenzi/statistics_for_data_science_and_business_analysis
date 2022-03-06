#!/usr/bin/env python

import pandas as pd

sat = pd.DataFrame()

sat = sat.assign(
    writing=[
        344,
        383,
        611,
        713,
        536,
    ]
)

sat = sat.assign(
    reading=[
        378,
        349,
        503,
        719,
        503,
    ]
)

print(sat)

print("Correlation: %f" % sat["reading"].corr(sat["writing"]))
