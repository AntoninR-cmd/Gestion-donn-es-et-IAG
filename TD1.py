# -*- coding: utf-8 -*-
"""
Created on Wed May 27 08:55:47 2026

@author: Antonin
"""

import pandas as pd
import numpy as np
import random as rd

countries = pd.read_csv("countries.csv", sep = ";")
cities = pd.read_csv("cities.csv", sep = ";")

print( countries)
print(cities)

print(cities.iloc[0:3])

indices = rd.sample(range(len(cities)), 10)
print(cities.iloc[indices])

print(cities.columns.values)

print(cities.dtypes)

cities.describe()

print(cities.iloc[0:10][["name", "latitude", "longitude"]])

print(cities.iloc[10])
nom11 = cities.iloc[10]["name"]

liste_nom = cities["name"]
print(liste_nom.dtypes)