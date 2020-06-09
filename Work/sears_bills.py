# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:52:41 2020

@author: Mehrab
"""
import math as math

thickness = 0.11*0.001;     # in m
sears_height = 442          # in m

stack_height = thickness;
n_days = 1;
while stack_height < 442:
    stack_height = stack_height*2;
    n_days = n_days + 1;
    
print('number of days', n_days)
print('number of bills', math.ceil(stack_height/thickness))
print('final height', stack_height)