# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], float(row[1]), float(row[2]))  #this creates the tuple 'holding' that has current row's data
            portfolio.append(holding)       #this appends the tuple 'holding' to the list 'portfolio'
    
    print(portfolio)
    return portfolio

            