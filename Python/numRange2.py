# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 16:11:46 2022

@author: mingt
"""

# Given an array of non negative integers A, and a range (B, C), 
# find the number of continuous subsequences in the array which have sum S in the range [B, C] or B <= S <= C
# Continuous subsequence is defined as all the numbers A[i], A[i + 1], .... A[j]
# where 0 <= i <= j < size(A)
# Example :
# as [5, 1], [5, 1, 0], [5, 1, 0, 2] are the only 3 continuous subsequence with their sum in the range [6, 8]
# NOTE : The answer is guranteed to fit in a 32 bit signed integer.class Solution:
	# @param A : list of integers
	# @param B : integer
	# @param C : integer
	# @return an integer
# 	def numRange(self, A, B, C):
    def numRange(A, B, C):
        result = 0
        n_A = len(A)
        for i in range(n_A):
            # print('this is ', i)
            # print(result)
            temp = A[i]
            if (temp >= B) and (temp <= C):
                result += 1
            for j in range(i+1, n_A):
                # print('here is', j, 'which is ', A[j], temp)
                temp += A[j]
                # print(temp)
                if (temp >= B) and (temp <= C):
                    # print('add one as temp is ', temp)
                    result += 1
                elif (temp <= C):
                    continue
                else:
                    break
            # print(result)
        return result

# Testing: 
# A = [10, 5, 1, 0, 2]
# (B, C) = (6, 8)
# numRange(A, B, C)

# A = [10, 5, 1, 0, 2, 3]
# (B, C) = (6, 8)
# numRange(A, B, C)

# A = [10, 5, 1, 0, 2, 3, 9, 1, 3, 4]
# (B, C) = (6, 8)
# numRange(A, B, C)

# A = [ 76, 22, 81, 77, 95, 23, 27, 35, 24, 38, 15, 90, 19, 46, 53, 
#      6, 77, 96, 100, 85, 43, 16, 73, 18, 7, 66 ]
# B = 98
# C = 290
# A[25]
# numRange(A, B, C)
