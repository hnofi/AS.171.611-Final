#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  1 12:57:20 2025

@author: hayleynofi
"""

import pandas as pd

# Read the file, skipping the top 3 metadata lines
df = pd.read_csv(
    "history.data",
    delim_whitespace=True,
    skiprows=3
)

# Save to CSV
df.to_csv("history.csv", index=False)