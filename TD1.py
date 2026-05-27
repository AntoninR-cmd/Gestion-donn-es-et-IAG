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

#Question 7
print(countries.isnull().sum())
print(countries.isnull().sum()/len(countries)*100)
print(countries.isnull().any(axis = 1))

#Question 8
print(countries.isnull().any(axis = 1).sum())
countries["continent"] = countries["continent"].apply(
    lambda x: "Inconnu" if pd.isna(x) else x
)
countries["currency_code"] = countries["currency_code"].apply(
    lambda x: "N/A" if pd.isna(x) else x
)
countries["currency_name"] = countries["currency_name"].apply(
    lambda x: "N/A" if pd.isna(x) else x
)
print(countries.isnull().any(axis = 1).sum())
print(countries.isnull().sum())

#Question 9
print(f'Il y a {cities["name"].isnull().sum()} ville(s) sans nom')
print(f'Il y a {cities["country"].isnull().sum()} ville(s) sans pays')
print('Villes sans nom ou pays \n')
print(cities.loc[cities["name"].isnull() | cities["country"].isnull()])
cities.dropna(subset=['name'], inplace = True)
print(f'Il y a {cities["name"].isnull().sum()} ville(s) sans nom')

#Question10
countries["density"] = countries["population"]/countries["area"]
print(countries.sort_values("density", ascending = False).iloc[0:9])

#Question11
def categorie_pop(x):
    if x < 10000 :
        return 'petite ville'
    elif 10000<x<100000 : 
        return 'ville moyenne'
    elif 100000<x<1000000 : 
        return 'grande ville'
    elif x> 1000000 : 
        return 'métropole' 
cities['pop_category'] = cities['population'].apply(categorie_pop)
print(cities['pop_category'].value_counts())

#Question 12
cities['hemisphere'] = np.where(
    cities['latitude']>=0,
    'Nord',
    'Sud'
    )
print('Répartition des villes selon hémisphère')
print(cities['hemisphere'].value_counts())

#Question 13
countries['taille'] = pd.cut(
    countries['area'], 
    bins=[0, 10000, 500000, 3000000, 20000000], 
    labels = ['Micro-état', 'petit pays', 'Pays moyen', 'Grand pays']
    )
print('Répartition des pays selon taille')
print(countries['taille'].value_counts())
