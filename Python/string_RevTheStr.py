# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 14:32:43 2022

@author: mingt
"""

# Given a string A.
# Return the string A after reversing the string word by word.
# NOTE:
# A sequence of non-space characters constitutes a word.
# Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
# If there are multiple spaces between words, reduce them to a single space in the reversed string.
#  Input Format
# The only argument given is string A.
# Output Format
# Return the string A after reversing the string word by word.
# For Example
class Solution:
    # @param A : string
    # @return a strings
    def solve(A):
        sep_A = A.split()
        result = ''
        for i in sep_A:
            if len(i) == 0:
                continue
            result = ' ' + i + result
        # print(result)
        # return result
        return result[1:]

# Testing
# # Input 1:
# A = "the sky is blue"
# solve(A)
# # Output 1:
#     # "blue is sky the"

# # Input 2:
# A = "this is ib"
# solve(A)
# # Output 2:
#     # "ib is this"

# # Input 3:
# A = " hello world "
# solve(A)
# # Output 3:
#  # "world hello"
# Editorial:
#     class Solution:
#     # @param A : string
#     # @return a strings
#     def solve(self, A):
#         return ' '.join(A.strip().split()[::-1])
# Scala:
#     class Solution {
#     def solve(str: String): String  = {
#         str.split(" ").reverse.mkString(" ").trim
#     }
# }
# C++
# string Solution::solve(string A) {
#     int n = A.size();
#     int i = 0;
#     int j;
#     string w, res;
#     while (i < n) {
#       while (i < n && A[i] == ' ') i++;
#       j = i + 1;
#       while (j < n && A[j] != ' ') j++;
#       w = A.substr(i, j - i);
#       if (res.size() == 0) res = w;
#       else res = w + " " + res;
#       i = j + 1;
#     }
#     return res; 
# }

# GO:
#     type stackString struct {
#     s []string
# }

# func NewStackString() *stackString {
#     return &stackString {make([]string,0), }
# }

# func (s *stackString) Push(v string) {
#     s.s = append(s.s, v)
# }

# func (s *stackString) Pop() (string) {
#     l := len(s.s)
#     if l == 0 {
#         panic("empty stackString access")
#     }

#     res := s.s[l-1]
#     s.s = s.s[:l-1]
#     return res
# }

# func (s *stackString) First() string {
#     l := len(s.s)
#     return s.s[l-1]
# }

# func (s *stackString) IsEmpty() bool {
#     return len(s.s) == 0
# }

# func (s *stackString) Size() int {
#     return len(s.s)
# }

# func solve(str string )  (string) {
#     stack := NewStackString()
#     s := ""
    
#     for i := 0; i < len(str); i++ {
#         if str[i] == ' ' {
#             stack.Push(s)
#             s = ""
#         } else {
#             s = s + string(str[i])
#         }
#     }
#     stack.Push(s)
#     result := ""
#     for !stack.IsEmpty() {
#         next := stack.Pop()
#         result = result + next
#         if stack.Size() > 0 {
#             result = result + " "
#         }
#     }
#     return result
# }
