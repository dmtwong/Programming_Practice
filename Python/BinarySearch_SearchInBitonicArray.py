# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 13:08:26 2022

@author: mingt
"""

# Problem Description
# Given a bitonic sequence A of N distinct elements, write a program to find a given element B in the bitonic sequence in O(logN) time.
# NOTE:
# A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.
# Problem Constraints
# 3 <= N <= 105
# 1 <= A[i], B <= 108
# Given array always contain a bitonic point.
# Array A always contain distinct elements.
# Input Format
# First argument is an integer array A denoting the bitonic sequence.
# Second argument is an integer B.

# Output Format
# Return a single integer denoting the position (0 index based) of the element B in the array A if B doesn't exist in A return -1.
# Example Input
# Input 1:
#  A = [3, 9, 10, 20, 17, 5, 1]
#  B = 20
# Input 2:
#  A = [5, 6, 7, 8, 9, 10, 3, 2, 1]
#  B = 30
# Example Output
# Output 1:
#  3
# Output 2:
#  -1
# example Explanation
# Explanation 1:
#  B = 20 present in A at index 3
# Explanation 2:
#  B = 30 is not present in A


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(A, B):
        def upSearch(A, left, right, key):     
            # print('up', A, left, right, key)
            while left <= right:
                mid = left + (right - left) // 2       
                # print(mid, A[mid])
                if A[mid] == key:
                    # print('yeah')
                    return mid                 
                if A[mid] > key:
                    right = mid - 1
                else:
                    left = mid + 1             
            return -1
 
        def downSearch(A, left, right, key):         
            # print('down', A, left, right, key)
            while left <= right:
                mid = left + (right - left) // 2
                # print(mid, A[mid])
                if A[mid] == key:
                    return mid
                if A[mid] < key:
                    right = mid - 1
                else:
                    left = mid + 1                     
            return -1   
        
        def findBP(A, left, right):    
            # print('findBP', A, left, right)
            bp = 0
            mid = (left + right) // 2
            # print(mid, A[mid-1], A[mid], A[mid+1])
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                # print('case1', mid)
                return mid             
            elif A[mid] > A[mid-1] and A[mid] < A[mid+1]:
                bp = findBP(A, mid, right)           
                # print('left side', bp)
            else:
                bp = findBP(A, left, mid)
                # print('right side', bp)
            return bp
         
        def search(A, ix, n, key):    
            # print('search', A, n, key, ix)
            # print(A[ix])
            if key > A[ix]:
                return -1
            elif key == A[ix]:
                return ix
            else:
                temp = upSearch(A, 0, ix-1, key)
                if temp != -1:
                    # print('yeahh')
                    return temp                 
                return downSearch(A, ix+1, n-1, key)
                     

        def main(A, B):
            key = B
            n = len(A)
            left = 0
            right = n - 1            
            ix = findBP(A, left, right)             
            x = search(A, ix, n, key)
            if (x == -1):
                return -1
            else:
                return x
        return main(A,B)
            
#  A = [3, 9, 10, 20, 17, 5, 1]
#  B = 20
# solve(A,B)

#  A = [5, 6, 7, 8, 9, 10, 3, 2, 1]
#  B = 30
# A= [ 1, 20, 50, 40, 10 ]
# B= 5
A = [ 1, 2, 3, 4, 5, 10, 9, 8, 7, 6 ]
B = 5

solve(A,B)

# Editorial: Scala
# class Solution {
#   def solve(A: Array[Int], B: Int): Int  = {
#     var start = 0
#     var end = A.length-1

#     var bitonicPoint = -1
#     while (bitonicPoint == -1) {
#       if (end - start <= 1) {
#         bitonicPoint = if (A(start) > A(start+1)) start else end
#       } else if (A(start) < A(start + 1)) {
#         start = (end + start) / 2
#       } else {
#         end = start
#         start = start / 2
#       }
#     }
#     import scala.collection.Searching._
#     A.search(B, 0, bitonicPoint) match {
#       case Found(foundIndex) => foundIndex
#       case InsertionPoint(insertionPoint) =>
#         A.search(B, bitonicPoint, A.length)(Ordering.Int.reverse) match {
#           case Found(foundIndex) => foundIndex
#           case InsertionPoint(insertionPoint) => -1
#         }
#     }
#   }
# }

# C:
#  * @input A : Integer array
#  * @input n1 : Integer array's ( A ) length
#  * @input B : Integer
#  * 
#  * @Output Integer


# int solve(int* A, int n1, int B) {

#     if(n1 == 0)
#     return -1;
    
#     int i = 0;
    
#     for(i = 0; i<n1; ++i){
#         if(A[i] == B)
#         return i;
#     }
    
#     return -1;
# }

# GO:
#     func isAscendingIndex(A []int, mid int) bool {
#     if mid == 0 || (mid != len(A) - 1 && A[mid] > A[mid - 1] && A[mid] < A[mid + 1]) {
#         return true
#     }
#     return false
# }

# func isBitonicIndex(A []int, mid int) bool {
#     if mid != 0 && mid != len(A) - 1 && A[mid] > A[mid - 1] && A[mid] > A[mid + 1] {
#         return true
#     }
#     return false
# }

# func findIncreasing(A []int, B int, high int) int {
#     low := 0
#     for low <= high {
#         mid := low + ((high - low) / 2)
#         if A[mid] == B {
#             return mid
#         } else if A[mid] < B {
#             low = mid + 1
#         } else {
#             high = mid - 1
#         }
#     }
#     return -1
# }

# func findDecreasing(A []int, B int, low int) int {
#     high := len(A) - 1
#     for low <= high {
#         mid := low + ((high - low) / 2)
#         if A[mid] == B {
#             return mid
#         } else if A[mid] < B {
#             high = mid - 1
#         } else {
#             low = mid + 1
#         }
#     }
#     return -1
# }

# func findBitonicIndex(A []int) int {
#     low := 0
#     high := len(A) - 1
#     mid := low + ((high - low) / 2)
#     for !isBitonicIndex(A, mid) {
#         if isAscendingIndex(A, mid) {
#             low = mid + 1
#         } else {
#             high = mid - 1
#         }
#         mid = low + ((high - low) / 2)
#     }
#     return mid
# }
 
# func solve(A []int , B int )  (int) {
#     bitonicIndex := findBitonicIndex(A)
#     result := findIncreasing(A, B, bitonicIndex)
#     if result == -1 {
#         return findDecreasing(A, B, bitonicIndex + 1)
#     }
#     return result
# }
