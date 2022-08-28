# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 11:08:02 2022

@author: mingt
"""

def lengthOfLastWord(A):
    # last_space = A.rfind(' ')
    # len_A = len(A)
    # if last_space == -1:
    #     return len_A
    result = list(A.split(" "))
    # print(result)
    len_result = len(result)
    result = result[::-1]
    for i in range(len(result)):
        len_i = len(result[i])
        # print(i)
        # print(len_i)
        if len_i == 0 and i < len_result:
            # print('jump')
            pass
            # print(i)
        else:
            return len_i
    # print('bottom')
    return 0
A = "Hello World"
B = "Hello World  "
C = 'd'
D = "  xDGBklKecz IAcOJYOH O  WY WPi"
E = "Hello $5"
F = ''
lengthOfLastWord(A)
lengthOfLastWord(B)
lengthOfLastWord(C)
lengthOfLastWord(D)
lengthOfLastWord(E)
lengthOfLastWord(F)

# Editorial (Python)
# class Solution:
#     # @param A : string
#     # @return an integer
#     def lengthOfLastWord(self, A):
#         l=len(A)
#         if (l==0):
#             return 0
        
#         i=l-1
#         while (i>=0 and A[i]==" "):
#             i-=1
        
#         cnt=0
#         while (i>=0 and A[i]!=" "):
#             cnt+=1
#             i-=1
        
#         return cnt

# Editorial (C++)
# int Solution::lengthOfLastWord(const string &A) {
#     int i = A.length() - 1, j = 0;
#     while(A[i] == 32)   i--;
#     while(A[i] != 32 && i>= 0)   i--,j++;
#     return j;
# }

# #Editorial (Scala)
# class Solution {
#     def lengthOfLastWord(A: String): Int  = {
#       var isChar = false
#       var len = 0
#       for {
#         i <- A.indices
#         ch = A.charAt(A.length - i - 1)
#       } {
#         if (ch.isLetter) {
#           isChar = true
#           len += 1
#         } else {
#           if (isChar) return len
#         }
#       }
#       len
#     }
# }
