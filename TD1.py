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
print('\n'+ "="*60)
print('Question 7')
print("="*60)
print(countries.isnull().sum())
print(countries.isnull().sum()/len(countries)*100)
print(countries.isnull().any(axis = 1))

#Question 8
print('\n'+ "="*60)
print('Question 8')
print("="*60)
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
print('\n'+ "="*60)
print('Question 9')
print("="*60)
print(f'Il y a {cities["name"].isnull().sum()} ville(s) sans nom')
print(f'Il y a {cities["country"].isnull().sum()} ville(s) sans pays')
print('Villes sans nom ou pays \n')
print(cities.loc[cities["name"].isnull() | cities["country"].isnull()])
cities.dropna(subset=['name'], inplace = True)
print(f'Il y a {cities["name"].isnull().sum()} ville(s) sans nom')

#Question10
print('\n'+ "="*60)
print('Question 10')
print("="*60)
countries["density"] = countries["population"]/countries["area"]
print(countries.nlargest(10, 'density')[["name", "population", "area", "density"]])

#Question11
print('\n'+ "="*60)
print('Question 11')
print("="*60)
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
print('\n'+ "="*60)
print('Question 12')
print("="*60)
cities['hemisphere'] = np.where(
    cities['latitude']>=0,
    'Nord',
    'Sud'
    )
print('Répartition des villes selon hémisphère')
print(cities['hemisphere'].value_counts())

#Question 13
print('\n'+ "="*60)
print('Question 13')
print("="*60)
countries['taille'] = pd.cut(
    countries['area'], 
    bins=[0, 10000, 500000, 3000000, 20000000], 
    labels = ['Micro-état', 'petit pays', 'Pays moyen', 'Grand pays']
    )
print('Répartition des pays selon taille')
print(countries['taille'].value_counts())

#Question 14
print('\n'+ "="*60)
print('Question 14')
print("="*60)
print(countries.loc[countries["currency_name"]=="Euro"])

#Question 15
print('\n'+ "="*60)
print('Question 15')
print("="*60)
L = []
for i in range(len(countries)):
    if "Dollar" in countries.iloc[i]["currency_name"]:
        if countries.iloc[i]["currency_code"] not in L : 
            L.append(countries.iloc[i]["currency_code"])
print(L)

#Question 16
print('\n'+ "="*60)
print('Question 16')
print("="*60)
print(countries.nlargest(2, 'area'))
print(countries.nsmallest(3, 'population'))
print(cities.nlargest(10, 'population'))

#Question 17
print('\n'+ "="*60)
print('Question 17')
print("="*60)
print(countries.sort_values(['continent', 'name'], ascending = [True, False]).iloc[:15][['name', 'continent']])

#Question 18
print('\n'+ "="*60)
print('Question 18')
print("="*60)
print(countries.sort_values(['continent', 'name'], ascending = [True, False]).iloc[:15][['name', 'continent', 'population']])
countries = countries.rename(columns={
    'name' : 'pays_nom',
    'area' : 'superficie',
    'population' : 'nb_habitants'
    })
print(countries.columns)

#Question 19
print('\n'+ "="*60)
print('Question 19')
print("="*60)
cities = cities.rename(columns = {'name' : 'capital_name'})
df = pd.merge(countries, cities, left_on='capital', right_on='id', how="left")
print(df)

#Question 20
print('\n'+ "="*60)
print('Question 20')
print("="*60)
print(df['capital_name'].isnull().sum())
print(df.nlargest(5, 'superficie')[['pays_nom', 'superficie', 'capital_name']])
print('-'*60)
print(df.nlargest(1, 'latitude')['capital_name'])
print('-'*60+'plus au Sud')
print(df.nsmallest(1, 'latitude')['capital_name'])