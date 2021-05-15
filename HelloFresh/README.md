#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 15 16:31:12 2021

@author: mariacarolina
"""

This script was developed in Spyder-IDE, using Python 3.9

The only packages imported were the numpy and pandas.

To run the script, open any Python IDE in the same directory as 
the recipes.json database file

First, the JSON file is loaded into the Pandas DataFrame, then all rows (recipes)
containing "Chilies" as an ingredient are added to a new DataFrame called chilie_recipes.

For every row in the chilie_recipes DataFrame, the value on the cookTime column
is inspected and, in case there is a 'H' it is replaced for '60' (so that it can be accounted as an hour).

Only the integers present in the string values of columns cookTime and preptime are extracted as ctime 
and ptime, respectively. Those are summed in a new variable total_time.

Then, a list of conditions for this total-time was created as well as 
list of the values (difficulty levels) we want to assign for each condition ('Hard', 'Medium', 'Easy')
        
Finally, using np.select with both lists as arguments, a new column    
 'Difficulty' was created and added on the chilie_recipes DataFrame
        
Lastly, the updated DataFrame was exported into a .csv file.      
