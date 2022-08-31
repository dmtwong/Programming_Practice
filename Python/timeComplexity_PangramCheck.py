# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 12:00:21 2022

@author: mingt
"""

# Given a sentence represented as an array A of strings that contains all lowercase alphabets.
# Chech if it is a pangram or not.
# A pangram is a unique sentence in which every letter of the lowercase alphabet is used at least once.
# Problem Constraints
# 1 <= |A| <= 105
# 1 <= Ai <= 5
# Input Format
# Given an array of strings A.
# Output Format
# Return an integer.


class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(A):
        char_seen = [False] * 26
        conden_A = ''.join(A)
        for i in conden_A.lower():
            char_seen[ord(i)-97] = True
        if (sum(char_seen) != 26):
            return 0
        else:
            return 1
        
# Example Input
# Input 1:
A = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
solve(A)
# Input 2:
A = ["interviewbit", "scaler"]
solve(A)
# Example Output
# Output 1:
# 1
# Output 2:
# 0
# Example Explanation
# Explanation 1:
# We can check that all english alphabets are present in given sentence.
# Explanation 2:
# Not all english alphabets are present.

# Editorial
# class Solution:
#     # @param A : list of strings
#     # @return an integer
#     def solve(self, A):
#         if len(set(list("".join(A).lower()))) == 26 : return 1
#         else: return 0
# C++
# int Solution::solve(vector<string> &A) {
#     assert(1<=A.size() && A.size()<=1e5);
#     bool vis[26] = {0};
#     for(string x: A){
#         assert(1<=x.size() && x.size()<=1e5);
#         for(char y: x){
#             assert('a'<=y && y<='z');
#             vis[y-'a'] = 1;
#         }
#     }
#     for(int i = 0; i < 26; ++i){
#         if(!vis[i]){
#             return 0;
#         }
#     }
#     return 1;
# }