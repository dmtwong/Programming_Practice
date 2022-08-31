# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 11:33:54 2022

@author: mingt
"""
# Convert the amount in number to words
# Our company wants to create a data entry verification system. 

# Given an amount in words and an amount indicated by data entry person in numbers, you have to detect whether the amounts are same or not.

# Note: There are a lot of corner cases to be considered. Interviewer expects you to take care of them.

# Input:

# String num: Amount written in digits as a string. This string will be an integer number without having any commas in between the digits.
# String words: Amount written in words according to Indian Numbering System.
# Output:

# An integer
# 1: Values match
# 0: Otherwise
# Please note :Every word needs to be separated using "-" rather than a space character
#  https://en.wikipedia.org/wiki/Indian_numbering_system

# Constraints 

# The number will fall in integer range(10^9)

# Example :

# Input :
# String  num = "1234"
# String words  = "one-thousand-two-hundred-and-thirty-four"

# Output:
# 1

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    # def solve(self, A, B):
    def solve(A, B):
        below20 = ["ERROR_0", "one-", "two-", "three-", "four-","five-", "six-", 
                   "seven-", "eight-", "nine-", "ten-", "eleven-", "twelve-",
                "thirteen-", "fourteen-", "fifteen-", "sixteen-", "seventeen-", 
                "eighteen-", "nineteen-"]
        
        multi10 = ["ERROR_0b", "ERROR_1b", "twenty-", "thirty-", "forty-", 
                   "fifty-", "sixty-", "seventy-", "eighty-", "ninety-"]
        
        def numToWords(n, s):     
            # print('now')
            this_str = ""
            # print(n)
            if (n > 19):
                # print(multi10[n // 10], below20[n % 10])
                this_str += multi10[n // 10] + below20[n % 10]
            else:
                this_str += below20[n]
                # print(below20[n])
            # print('this_str')
            if (n):
                this_str += s
            # print('here', this_str)
            return this_str
        
        def convertToWords(n):
            n = int(n)
            out = ""
            # print(out + 'a')
            
            out += numToWords((n // 10000000), "crore-")
    
            out += numToWords(((n // 100000) % 100), "lakh-")
        
            # out += numToWords(((n // 100000000) % 1000000), "hundred-")
            # if n >= 100000000:
            #     n /= 10
            #     n = int(n)
            # out += numToWords((n // 1000000), "million-")
            # n -= n//1000000 * 1000000
            # print(out + 'b')
            # out += numToWords(((n // 100000) % 1000), "hundred-")

            out += numToWords(((n // 1000) % 100), "thousand-")

            out += numToWords(((n // 100) % 10), "hundred-")
        
            if (n > 100 and n % 100):
                out += "and-"
            # print(out + 'c')
            out += numToWords((n % 100), "")
            # print(out + 'd')
            return out
        
        result = convertToWords(A)  
        # return result[:len(result)-1] 
        if (result[:len(result)-1] == B):
            return 1
        else:
            return 0
        
solve("63019100", 'six-million-three-hundred-nineteen-thousand-one-hundre')  
solve("63019100", 'six-crore-thirty-lakh-nineteen-thousand-one-hundred')  
solve("1234", 'one-thousand-two-hundred-and-thirty-four')

# Editorial C++
# // strings at index 0 is not used
# // to make indexing simple
# //Please note we will add space after every word
# string one[] = { "", "one-", "two-", "three-", "four-",
#                  "five-", "six-", "seven-", "eight-",
#                  "nine-", "ten-", "eleven-", "twelve-",
#                  "thirteen-", "fourteen-", "fifteen-",
#                  "sixteen-", "seventeen-", "eighteen-",
#                  "nineteen-"
#                };
 
# // strings at index 0 and 1 are not used
# //to make array indexing simple
# string ten[] = { "", "", "twenty-", "thirty-", "forty-",
#                  "fifty-", "sixty-", "seventy-", "eighty-",
#                  "ninety-"
#                };
 
# // n is 1- or 2-digit number
# string numToWords(int n, string s)
# {
#     string str = "";
#     // if n is more than 19, divide it
#     if (n > 19)
#         str += ten[n / 10] + one[n % 10];
#     else
#         str += one[n];
 
#     // if n is non-zero
#     if (n)
#         str += s;
 
#     return str;
# }
 
# // Function to print a given number in words
# string convertToWords(int n)
# {
#     // stores word representation of given number n
#     string out;
 
#     // handles digits at ten crore and crore places (if any)
#     out += numToWords((n / 10000000), "crore-");
 
#     // handles digits at ten lakh and lakh places (if any)
#     out += numToWords(((n / 100000) % 100), "lakh-");
 
#     // handles digits at thousands and tens thousands
#     // places (if any)
#     out += numToWords(((n / 1000) % 100), "thousand-");
 
#     // handles digit at hundreds places (if any)
#     out += numToWords(((n / 100) % 10), "hundred-");
 
#     // we need to add "and" if the number is more than hundred and contains digit at ten's or one's place
#     if (n > 100 && n % 100)
#         out += "and-";
 
#     // handles digits at ones and tens places (if any)
#     out += numToWords((n % 100), "");
#     out = out.substr(0, out.size()-1); // to remove the last trailing "-"
#     return out;
# }
# int Solution::solve(const string A, const string B) {
#     int n = stoi(A);
#     string y = convertToWords(n);
#     if(y.compare(B)==0)
#         return 1;
#     return 0;
# }