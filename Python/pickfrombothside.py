# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 14:25:43 2022

@author: mingt
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(A, B):
        curr_left = sum(A[:B])
        curr_right = 0
        curr_max = curr_left
        for i in range(1, B+1):
            curr_left -= A[B-i]
            curr_right += A[-i] 
            # print(curr_max)
            this_sum = curr_left + curr_right
            # print(this_sum)
            if this_sum > curr_max:
                curr_max = this_sum
        return(curr_max)

# Blackbox
A, B = ( [5, -2, 3 , 1, 2], 3 )
solve(A, B)
A, B = ( [1, 2], 1 )
solve(A, B)
A = [ -533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297, 811, 322, -667, 673, -336, 141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741, 529, -222, -684, 35 ]
B = 48
solve(A, B)

# GlassBox
# Enter for loop once
A, B = ([1, 2], 0)
