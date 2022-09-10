# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 14:44:36 2022

@author: mingt
"""

# Compare two version numbers version1 and version2.

# If version1 > version2 return 1,
# If version1 < version2 return -1,
# otherwise return 0.
# You may assume that the version strings are non-empty and contain only 
# digits and the . character.

# The . character does not represent a decimal point and is used to 
# separate number sequences.

# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

# Here is an example of version numbers ordering:
# 0.1 < 1.1 < 1.2 < 1.13 < 1.13.4

# class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
 	# def compareVersion(self, A, B):
def compareVersion(A, B):
    listed_A = A.split(".")
    listed_B = B.split(".")
    n_A, n_B = len(listed_A), len(listed_B)
    
    for i in range(n_A):
        listed_A[i] = int(listed_A[i])
    for j in range(n_B):
        listed_B[j] = int(listed_B[j])        
    # print(listed_A)
    # print(listed_B)
    
    if i > j:
        listed_B.extend([0] * (i - j))
    elif i < j:
        listed_A.extend([0] * (j - i))
        
    for ix in range(len(listed_A)):
        # print(ix, listed_A[ix], listed_B[ix])
        if listed_A[ix] > listed_B[ix]:
            return 1
        elif listed_A[ix] < listed_B[ix]:
            return -1
        else:
            pass
    return 0

# Test case
# v1 = "0.1"
# v2 = "1.1"
# v3 = "1.2"
# v4 = "1.13"
# v5 = "1.13.4"
# v6 = "1.1"
# compareVersion(v1, v2)
# compareVersion(v2, v3)
# compareVersion(v3, v4)
# compareVersion(v5, v4)
# compareVersion(v5, v6)
# compareVersion(v6, v2)

# Editorial:
#     class Solution:
#     # @param A : string
#     # @param B : string
#     # @return an integer
#     def compareVersion(self, A, B):
#         a=list(map(int,A.split('.')))
#         x=len(a)
#         b=list(map(int,B.split('.')))
#         y=len(b)
#         while(x>y):
#             b.append(0)
#             y+=1
#         while(y>x):
#             a.append(0)
#             x+=1
#         if a>b:
#             return 1
#         if a<b:
#             return -1
#         return 0
    
#     class Solution {
#     def compareVersion(A: String, B: String): Int  = {
#       val aa = A.split('.')
#       val bb = B.split('.')
#       val zip = aa.zipAll(bb, "", "")
#       for (t2 <- zip) {
#         val s1 = t2._1.dropWhile(ch => ch == '0')
#         val s2 = t2._2.dropWhile(ch => ch == '0')
#         if (!(s1.isEmpty && s2.isEmpty)) {
#           if (s1.length > s2.length) return 1
#           else if (s1.length < s2.length) return -1
#           else {
#             val v1 = s1.toLong
#             val v2 = s2.toLong
#             if (v1 > v2) return 1
#             else if (v1 < v2) return -1
#           }
#         }
#       }
#       0
#     }
# }
# int Solution::compareVersion(string A, string B) {
#     // Do not write main() function.
#     // Do not read input, instead use the arguments to the function.
#     // Do not print the output, instead return values as specified
#     // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
#     int j, i;
#     for( i=0, j=0 ; i<A.size() || j<B.size() ; i++, j++){
#         unsigned long long num1 = 0, num2 = 0;
#         while(i < A.size() && A[i] != '.'){
#             num1 *= 10;
#             num1 += A[i] - '0';
#             i++;
#         }
#         while(j < B.size() && B[j] != '.'){
#             num2 *= 10;
#             num2 += B[j] - '0';
#             j++;
#         }
#         if(num1 > num2) return 1;
#         if(num1 < num2) return -1;
#     }
#     return 0;
# }