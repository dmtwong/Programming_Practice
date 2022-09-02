# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 14:07:44 2022

@author: mingt
"""

# Problem Description
# Given a string A, consisting of comma-separated positive integers.
# Extract the given integers from the string and return an integer array consisting of the integers present in the string.
# Note: All given integers will fit in a 32-bit signed integer.
# Problem Constraints
# 1 <= |A| <= 105
# Input Format
# The first and only argument is a string A.
# Output Format
# Return an integer array.
# The array should contain all the integers in the same order as they appear in the string.
# Example Input
# Input 1:
# Input 2:
# Example Output
# Output 1:
# [1, 2, 3]
# Output 2:
# [1, 99, 3]

# Example Explanation
# Explanation 1:
# The array is given in Example output.
# Explanation 2:
# The array is given in Example output.
import string
class Solution:
    # @param A : string
    # @return a list of integers
    # def solve(self, A):
    def solve(A):
        A = A.split(',')
        result = [int(ele) for ele in A]
        return result

# # Testing 
# A = "1,2,3"
# solve(A)
# A = "1,99,3"
# solve(A)


# Scala:
#     class Solution {
#     def solve(A: String): Array[Int]  = {
#          return A.split(',').map(_.toInt)
        
#     }
# }

# C++:
#     vector<int> Solution::solve(string A) {
#     int n = A.size();
#     assert(1 <= n && n <= 1e5);
#     for(char &x: A) assert(x == ',' || isdigit(x));
#     vector<int> ans;
#     int num = 0;
#     for(char &x: A){
#         if(x == ','){
#             ans.push_back(num);
#             num = 0;
#         }
#         else{
#             num = num*10 + x-'0';
#         }
#     }
#     ans.push_back(num);
#     return ans;
# }
    
# GO:
#     /**
#  * @input A : String
#  * 
#  * @Output Integer array.
#  */
# func solve(A string)  ([]int) {
#     result := []int{}
#     current := 0
#     for _,r := range A {
#         switch(r){
#             case '0','1','2','3','4','5','6','7','8','9':
#                 current = current*10 + int(r - '0')
#             case ',':
#                 result = append(result, current)
#                 current = 0
#         }
#     }
#     result = append(result, current)
#     return result
# }

    
# C:
#     /**
#  * @input A : String termination by '\0'
#  * 
#  * @Output Integer array. You need to malloc memory, and fill the length in len1
#  */
# int* solve(char* A, int *len1) {
#     int j, cnt = 0;
#     int* res;
#     int number = 0;
#     char* ptr;

#     for (ptr = A; *ptr; ++ptr) {
#         if (*ptr == ',') {
#             cnt += 1;
#         }
#     }

#     res = malloc(sizeof(int) * (cnt + 1));
#     *len1 = cnt + 1;
#     j = 0;

#     for (ptr = A; *ptr; ++ptr) {
#         if (*ptr == ',') {
#             res[j] = number;
#             number = 0;
#             j += 1;
#         }

#         else {
#             number = number * 10 + *ptr - '0';
#         }
#     }
#     res[j] = number;

#     return res;
# }
