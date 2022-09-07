# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 15:50:58 2022

@author: mingt
"""

# Find the kth smallest element in an unsorted array of non-negative integers.
# Definition of kth smallest element
# kth smallest element is the minimum possible n such that there are 
# at least k elements in the array <= n.

# In other words, if the array A was sorted, then A[k - 1] 
# ( k is 1 based, while the arrays are 0 based )

# NOTE

# You are not allowed to modify the array ( The array is read only ). 

# Try to do it using constant extra space.

# Example:


# answer : 2

import sys
class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
# 	def kthsmallest(self, A, B):
	def kthsmallest(A, B):        
        
        def countSmall(A, mid):
            result = 0
            for i in range(n_A):
                if A[i] <= mid:
                    result += 1
            return result

        low = sys.maxsize
        high = -low
        n_A = len(A)
        
        for i in range(n_A):
            low = min(low, A[i])
            high = max(high, A[i])
    
        while low < high:
            mid = low + (high - low) // 2
            # print(low, mid, high)    
            if countSmall(A, mid) < B:
                low = mid + 1
                # print('this')
            else:
                high = mid
                # print('that')
        # print(low, mid, high)
        if (low == high):
            return high
        else:
            return "Opps!"

# Test Case
# A = [2, 1, 4,3, 2]
# k = 3
# kthsmallest(A, k)
# A = [1, 4, 5, 3, 19, 3]
# k = 4

