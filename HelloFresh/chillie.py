#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 15 16:15:05 2021

@author: mariacarolinabarata
"""
import numpy as np
import pandas as pd


#Load the JSON file into the Pandas DataFrame
recipes_list = pd.read_json('/Users/mariacarolina/Documents/HelloFresh/recipes.json', lines=True)
    
#Select all rows containing "Chilies" to a new DataFrame chilie_recipes
chilie_recipes = recipes_list[recipes_list['ingredients'].str.contains('Chilies', regex=False)]
                 
#For every row (recipe) in the DataFrame chilie_recipes       
for label, recipe in chilie_recipes.iterrows():
    
        #replace the 'H' for '60'
        map (lambda x: 60 if x=="H" else x, recipe['cookTime'])
    

        #extract only the integers in the string 
        ctime = int(''.join(filter(lambda i: i.isdigit(), recipe['cookTime'])))
        ptime = int(''.join(filter(lambda i: i.isdigit(), recipe['prepTime'])))
        
        total_time = ctime + ptime
        
        print(total_time)
        
        # create a list of conditions
        conditions = [
            (total_time >= 60),
            (total_time < 60 & total_time > 30),
            (total_time <= 30)
            ]
        
        # create a list of the values we want to assign for each condition
        values = ['Hard', 'Medium', 'Easy']
        
        # create a new column and use np.select to assign values to it using our lists as arguments
        chilie_recipes['Difficulty'] = np.select(conditions, values)
        
        # display updated DataFrame
        chilie_recipes()
        
 #export updated DataFrame into a .csv file       
chilie_recipes.to_csv(r'/Users/mariacarolina/Documents/HelloFresh/ChilieRecipes.csv', index = False)
        