# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 09:38:19 2022

@author: mingt
"""

# Given a matrix of integers A of size N x M in which each row is sorted.
# Find an return the overall median of the matrix A.
# Note: No extra memory is allowed.
# Note: Rows are numbered from top to bottom and columns are numbered from left to right.

# Input Format
# The first and only argument given is the integer matrix A.
# Output Format
# Return the overall median of the matrix A.
# Constraints
# 1 <= N, M <= 10^5
# 1 <= N*M  <= 10^6
# 1 <= A[i] <= 10^9
# N*M is odd
# For Example
# Input 1:
# Output 1:
#     5
# Explanation 1:
#     A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
#     Median is 5. So, we return 5.
# Input 2:
# Output 2:
#     17 ``` Matrix=
# ```

class Solution:
	# @param A : list of list of integers
	# @return an integer
# 	def findMedian(self, A):
    def findMedian(A):
        r_A = len(A)
        c_A = len(A[0])
        mid_ix = (r_A * c_A + 1) // 2
        min_A = A[0][0]
        max_A = A[0][c_A - 1]
        for i in range(r_A):
            if A[i][0] < min_A:
                min_A = A[i][0]
            if A[i][c_A - 1] > max_A:
                max_A = A[i][c_A - 1]
        
        while (min_A < max_A):
            temp_mid_A = min_A + (max_A - min_A) // 2
            # print('new round', min_A, max_A, temp_mid_A)
            temp_ix = 0
            for i in range(r_A):
                temp_count = 0
                for j in range(c_A):
                    if A[i][j] <= temp_mid_A:
                        temp_count += 1
                temp_ix += temp_count
                # print(temp_ix)
            if temp_ix < mid_ix:
                min_A = temp_mid_A + 1
            else:
                max_A = temp_mid_A
        
        return(min_A)

#         # Test Case
# A = [   [1, 3, 5],
#             [2, 6, 9],
#             [3, 6, 9]   ]
# findMedian(A)
# A = [   [5, 17, 100]    ]
# findMedian(A)

# Editorial:
#     import bisect

# class Solution:
#     # @param A : list of list of integers
#     # @return an integer
#     def findMedian(self, A):
        
#         temp = []
        
#         for i in range(0, len(A)):
#             for j in range(0, len(A[0])):
#                 temp.append(A[i][j])
        
#         temp.sort()
        
#         return temp[len(temp)//2]
# Scala:
#     class Solution {
#     def findMedian(A: Array[Array[Int]]): Int  = {
#       import java.util

#       val r = A.length
#       val c = A(0).length
    
#       var max = Int.MinValue
#       var min = Int.MaxValue
#       for (i <- 0 until r) {
#         min = math.min(min, A(i)(0))
#         max = math.max(max, A(i)(c - 1))
#       }
    
#       val desired = (r * c + 1) / 2
#       while (min < max) {
#         val mid = min + (max - min) /2
#         var place = 0
#         var get = 0
    
#         for (i <- 0 until r) {
#           get = util.Arrays.binarySearch(A(i), mid)
#           if(get < 0) get = Math.abs(get) - 1
#           else {
#             while (get < A(i).length && A(i)(get) == mid) {
#               get += 1
#             }
#           }
          
#           place += get
#         }
        
#         if(place < desired) min = mid + 1
#         else max = mid
#       }
      
#       min
#     }
# }
    
#     C++
#     int Solution::findMedian(vector<vector<int> > &A) {
#     int l = 0, r = INT_MAX;
#     int mid, req = (int)A.size() * (int)A[0].size();
#     assert(A.size()*A[0].size()<=1000000);
#     assert(req % 2);
#     while(r - l > 1){
#         mid = l + (r - l) / 2;
#         int cnt = 0;
#         for(auto &i: A){ 
#             //using upper bound in a sorted array to count number of elements smaller than mid
#             int p = upper_bound(i.begin(), i.end(), mid) - i.begin();
#             cnt += p;
#         }
#         if(cnt >= (req/2 +1)) r = mid;
#         else l = mid;
#     }   
#     return r;
# }

