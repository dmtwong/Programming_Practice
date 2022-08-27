# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 13:30:25 2022

@author: mingt
"""


def prettyPrint(A):
    len_M = A*2 - 1
    result = list()     
    len_side = len_M//2
    
    for i in range(0, len_side):
        inner_list = [] 
        ix = A 
        for j in range(i):
            inner_list.append(ix)
            ix -= 1                
        for k in range( len_M - 2 * i):
            inner_list.append(A - i)
        ix = A - i + 1
        for l in range(i):
            inner_list.append(ix)
            ix += 1            
        result.append(inner_list) 
            
    for i in range(len_side, -1, -1):
        inner_list = [] 
        ix = A 
        for j in range(i):
            inner_list.append(ix)
            ix -= 1             
        for k in range( len_M - 2 * i):
            inner_list.append(A - i)
            ix = A - i + 1
        for l in range(i):
            inner_list.append(ix)
            ix += 1
        result.append(inner_list)  
    return result

prettyPrint(4)      