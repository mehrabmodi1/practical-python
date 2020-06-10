# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 10:39:30 2020

@author: Mehrab

"""


def portfolio_cost(filename):
    print('Hello')
    tot_cost = 0
    fpath = 'Data/' + filename
   
    with open(fpath, 'rt') as file:
        line_n = 1;
        for line in file:
            #skipping header row
            if line_n == 1:
                line_n = line_n + 1
                continue
            
            data = line.split(',')
            
            try:
                n_shares = float(data[1])
            except: 
                print('could not read current n shares, skipping row ', line_n)
                continue
            
            try:
                price = float(data[2])
            except: 
                print('could not read current price, skipping row ', line_n)
                continue
                
            curr_cost = n_shares*price
            tot_cost = tot_cost + curr_cost
            
            line_n = line_n + 1
            
    return tot_cost

#tot_cost = portfolio_cost('portfolio.csv')            
#print('total cost:', tot_cost)
    