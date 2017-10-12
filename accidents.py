#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

# Files hki_accidents.csv and hki_accidents_clean.csv contain all traffic accidents
# in Helsinki area from 2011 to 2016

# File hki_accidents.csv contains all original columns except Oslakpvm and Luovpvm
# The following columns have been removed from  hki_accidents_clean.csv:
# Maakunta, Maakuntsel, Rautatie, Rautatsel, Muuliitsel, Muuliit, Maankäyttö,
# Maankäytse, Tienverkas, Tienverkse

accidents = pd.read_csv('data/hki_accidents_clean.csv')

#print(accidents.columns.values)
#print(len(accidents))




