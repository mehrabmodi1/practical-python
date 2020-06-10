# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 10:39:30 2020

@author: Mehrab
"""

tot_cost = 0

with open('Data\portfolio.csv') as file:
    line_n = 1;
    for line in file:
        #skipping header row
        if line_n == 1:
            line_n = line_n + 1
            continue
        
        data = line.split(',')
        n_shares = float(data[1])
        price = float(data[2])
        curr_cost = n_shares*price
        tot_cost = tot_cost + curr_cost
        
        line_n = line_n + 1
        
    print('total cost:', tot_cost)
    