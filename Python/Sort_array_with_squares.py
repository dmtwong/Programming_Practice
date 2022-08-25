# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 15:39:01 2022

@author: mingt
"""

def solve(A):
    len_A = len(A)
    result = []
    i = 0
    j = len_A - 1
    if len_A == 1:
        return [A[0]**2]
    while i<=j:
        bool_tails = abs(A[i]) > abs(A[j])
        # print(bool_tails, A[i], A[j], result)
        if bool_tails == True:
            result.append(A[i]**2)
            i += 1
        else:
            result.append(A[j]**2)
            j -= 1
        # print(result)
    result.reverse()
    return result