# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 13:42:15 2022

@author: mingt
"""

# Given an array of integers,  sort the array into a wave like array and 
# return it, 
# In other words, arrange the elements into a sequence such that 
 # a1 >= a2 <= a3 >= a4 <= a5.....
# Example
# Given [1, 2, 3, 4]
# One possible answer : [2, 1, 4, 3]
# Another possible answer : [4, 1, 3, 2]
# NOTE : If there are multiple answers possible, 
# return the one thats lexicographically smallest. 
# So, in example case, you will return [2, 1, 4, 3]

# class Solution:
	# @param A : list of integers
	# @return a list of integers
	def wave(A):
        len_A = len(A)
        A.sort()
        for i in range(0, len_A, 2):
            # print(i, len_A - 1, A[i], A[i-1], A[i+1])
            if (i > 0 and A[i-1] > A[i]):
                # print("here")
                A[i], A[i-1] = A[i-1], A[i]
            if (i < len_A - 1 and A[i] < A[i+1]):
                # print("there")
                A[i+1], A[i] = A[i], A[i+1]
        return(A)
    
# Test case
# A = [1, 2, 3, 4]
# wave(A)

# C++ 
# vector<int> Solution::wave(vector<int> &A) {
#     sort(A.begin(), A.end());
#     for(int i=0; i<A.size()-1; i+=2) swap(A[i], A[i+1]);
#     return A;
# }
# Scala:
#     class Solution {
#     def wave(A: Array[Int]): Array[Int]  = {
#         val sorted = A.sorted
#         for (i <- 1 until sorted.length by 2) {
#             val tmp = sorted(i - 1)
#             sorted(i - 1) = sorted(i)
#             sorted(i) = tmp
#         }
#         sorted
#     }
# }
