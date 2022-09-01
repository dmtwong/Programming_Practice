# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 14:04:25 2022

@author: mingt
"""

# You are given a string S, and you have to find all the amazing substrings of S.
# Amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).
# Input
# Only argument given is string S.
# Output
# Return a single integer X mod 10003, here X is number of Amazing Substrings in given string.
# Constraints
# 1 <= length(S) <= 1e6
# S can have special characters
# Example
# Input
#     ABEC
# Output
#     6
# Explanation
# 	Amazing substrings of given string are :
# 	1. A
# 	2. AB
# 	3. ABE
# 	4. ABEC
# 	5. E
# 	6. EC
# 	here number of substrings are 6 and 6 % 10003 = 6.

class Solution:
    # @param A : string
    # @return an integer
    # import string
    # import pylab
    # def solve(self, A):
    def solve(A):
        # A = A.split() 
        # tmp = [0, 2]
        # len_str_A = 4
        # string.punctuation
        def find_vowel(str_A):
            vowel_ix = []
            len_str_A = len(str_A)
            for ix in range(len_str_A):
                if str_A[ix] in 'AEIOUaeiou':
                    vowel_ix.append(ix)
            return (vowel_ix, len_str_A)        
        def count_ass(str_A):
            vowel_ix, len_str_A = find_vowel(str_A)
            # print(vowel_ix)
            # print(len_str_A)
            # print(len_str_A - pylab.array(vowel_ix))
            result = 0
            for i in range(len(vowel_ix)):
                result += (len_str_A - vowel_ix[i])
            return result

        return count_ass(A) % 10003
    
    
test_1 = "ABEC"

A_1 = "pGpEusuCSWEaPOJmamlFAnIBgAJGtcJaMPFTLfUfkQKXeymydQsdWCTyEFjFgbSmknAmKYFHopWceEyCSumTyAFwhrLqQXbWnXSn"
B_1 = "a"
C_1 = "E"
d_1 = "t"

solve(test_1)
solve(A_1)
solve(B_1)
solve(C_1)
solve(d_1)
