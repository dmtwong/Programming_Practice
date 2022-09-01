# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 14:36:22 2022

@author: mingt
"""
# Problem Description
# Given a string A. The string contains some words separated by spaces.
# Return the number of words in the given string.
# Problem Constraints
# 1 <= |A| <= 105
# Ai = { lowercase English letters or spaces}
# Input Format
# The first and only argument is a string A.
# Output Format
# Return an integer.
# Example Input
# Example Output
# Output 1:
# 1
# Output 2:
# 3
# Example Explanation
# Explanation 1:
# The string has only one word "bonjour".
# Explanation 2:
# The string have three words "hasta", "la", "vista".
import string
class Solution:
    # @param A : string
    # @return an integer
    # def solve(self, A):
    def solve(A):
        A = A.split()
        return len(A)

# Input 1:
A = "bonjour"
solve(A)
# Input 2:
A = "hasta la vista"

# C++
# int Solution::solve(string A) {
#     int n = A.size();
#     assert(1 <= n && n <= 1e5);
#     for(char &x: A) assert(x == ' ' || ('a' <= x && x <= 'z'));
#     int ans = 0;
#     for(int i = 0; i < n; ++i){
#         if(A[i] == ' ') continue;
#         while(i < n && A[i] != ' ') ++i;
#         ++ans;
#     }
#     return ans;
# }

# Scala
# class Solution {
#     def solve(A: String): Int  = {
#         A.split(' ').filter(_ != "").length
#     }
    
# }

# Go
# /**
#  * @input A : String
#  * 
#  * @Output Integer
#  */
# func solve(A string )  (int) {
#     num := 0
#     found := false
#     for i:=0;i<len(A);i++ {
#         if A[i] == ' ' {
#             if found {
#             num++
#             }
#             found = false
#         } else {
#             found = true
#         }
#     }
#     if found {
#         num++
#     }
#     return num
# }
