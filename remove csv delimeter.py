# -*- coding: utf-8 -*-
"""
Created on Thu May  5 16:05:23 2022

@author: Gurkirat
"""

import csv
import glob 
import os
import sys

#mention folder where you want to store the files
path_output = '/' 
#mention folder where input files are present
path='/'

#detecting all files
csv_files = glob.glob(os.path.join(path, "*.csv"))

for path_input in csv_files:
    print path_input
    
    filel= open(path_input)
    print type(file1)   
    csvreader = csv.reader(file1) 
    header = [] 
    header = next(csvreader)
    print header
    
    rows = []   
    for row in csvreader: 
        rows.append(row) 
    print (rows)    
    output_name = path_input.split("\\")[-1]
    print output_name
    output_file = os.path.join(path_output, output_name) 
    print output_file 
    
    with open(output_file, 'wb') as outcsv:  
        writer csv.writer (outcsv)
        writer.writerow (header)
    
        with open (path_input, "rU") as incsv:
            reader = csv.reader(incsv, delimiter='#')
            reader.next()  
            writer.writerows((row for row in reader))
    
    print("Delimiter successfully changed\n\n")