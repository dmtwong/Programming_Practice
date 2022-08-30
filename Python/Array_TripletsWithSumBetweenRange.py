# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 11:01:39 2022

@author: mingt
"""

# class Solution:
	# @param A : list of strings
	# @return an integer
# def solve(self, A):
# Given an array of real numbers greater than zero in form of strings.

# Find if there exists a triplet (a,b,c) such that 1 < a+b+c < 2 . 

#  Return 1 for true or 0 for false
# Example:

# Given [0.6, 0.7, 0.8, 1.2, 0.4] ,

# You should return 1

# O(n) solution is expected.

# Note: You can assume the numbers in strings don’t overflow the primitive data type and there are no leading zeroes in numbers. Extra memory usage is allowed.

##### self note: this approach is not O(n)####
def solve(A):
    s_1 = set()
    # s_2 = set()
    # s_3 = set()
    for i in range(len(A)):
        A[i] = float(A[i])
        if A[i] < 2:
            s_1.add(A[i])
    n_s_1 = len(s_1)
    # s_dup = s_1.copy()
    # print(s_1)
    if n_s_1 == 0:
        return 0    
    for i in range(n_s_1-2):
        temp = s_1.pop()
        curr_i = temp        
        s_dup_1 = s_1.copy()
        len_s_2 = len(s_dup_1)
        # print(curr_i, temp, len_s_2, s_dup_1)
        for j in range(len_s_2):            
            curr_i += s_dup_1.pop()
            temp_2 = curr_i
            s_dup_2 = s_dup_1.copy()
            # print('there', curr_i, temp_2, s_dup_2)
            if (curr_i >= 2):
                pass           
            len_s_3 = len(s_dup_2)
            for z in range(len_s_3):
                curr_i += s_dup_2.pop()
                # print('here', curr_i, s_dup_2)
                if (curr_i >= 1 and curr_i <= 2):
                    return 1
                curr_i = temp_2
            curr_i = temp                
    return 0
A = [ "0.6", "0.1", "0.2", "1.5" ]
solve(A)
A = [ "0.503094", "0.648924", "0.999298" ]
solve(A)    
A = [ "2.673662", "2.419159", "0.573816", "2.454376", "0.403605", "2.503658", "0.806191" ]
solve(A)     
            
B =[0.6, 0.7, 0.8, 1.2, 0.4] 
solve(B)


# temp_1 = set()
# temp_1.add(5)
# temp_1.add(2)
# temp_1
# temp_2 = temp_1
# for i in temp_1:
#     print(i)
# temp_2.pop()
# temp_1.add(2)
# temp_2 = temp_1.copy()


# Editorial: 
# class Solution:
#     # @param A : list of strings
#     # @return an integer
#     def solve(self, A):
#         n = len(A)
#         B = [float(i) for i in A]
#         buckets = [[], [], []]
#         for i in B:
#             if i < 2.0/3:
#                 buckets[0].append(i)
#             elif i < 1:
#                 buckets[1].append(i)
#             else:
#                 buckets[2].append(i)
        
#         def get(index):
#             amx1, amx2, amx3 = -10, -10, -10
#             ami1, ami2, ami3 = 3, 3, 3
#             for i in buckets[index]:
#                 if i > amx1:
#                     amx1, amx2, amx3 = i, amx1, amx2
#                 elif i > amx2:
#                     amx2, amx3 = i, amx2
#                 elif i > amx3:
#                     amx3 = i
            
#                 if i < ami1:
#                     ami1, ami2, ami3 = i, ami1, ami2
#                 elif i < ami2:
#                     ami2, ami3 = i, ami2
#                 elif i < ami3:
#                     ami3 = i
#             return [amx1, amx2, amx3, ami1, ami2, ami3]
        
        
#         a = get(0)
#         b = get(1)
#         c = get(2)
#         ls = []
#         fc = a[0] + a[1] + a[2]
#         ls.append(fc)
#         fc = a[3] + a[4] + c[3]
#         ls.append(fc)
#         fc = a[3] + b[3] + b[4]
#         ls.append(fc)
#         fc = a[3] + b[3] + c[3]
#         ls.append(fc)
#         fc = b[0] + a[3] + a[4]
#         ls.append(fc)
#         if a[0] != a[3]:
#             fc = b[0] + a[0] + a[3]
#             ls.append(fc)
#             fc = b[3] + a[0] + a[3]
#             ls.append(fc)
#         fc = b[3] + a[0] + a[1]
#         ls.append(fc)
#         for fc in ls:
#             if fc > 1 and fc < 2:
#                 return 1
#         return 0

# C++
# double min_element(vector<double> A)  //return minimum element
# { double min=A[0];
# 	for(int i=0;i<A.size();i++)
# {
# 	if(A[i]<min)
# 	{
# 		min=A[i];
# 	}
# 	
# 	}
# 	return min;
# }
# int Solution::solve(vector<string> &a) {
# vector<double> A,B,C;

# for(int i=0;i<a.size();i++)
# { char b[20];
# for(int j=0;j<a[i].length();j++)
#   {
#   	b[j]=a[i][j];
#   }
# if(0.0<atof(b)&&atof(b)<((double)2.0/(double)3.0)) // atof converts string to double
# {
# 	A.push_back(atof(b));
# 	
# }
# else if((double)2.0/(double)3.0<=atof(b)&&atof(b)<=1.0)
# {
# 	B.push_back(atof(b));
# 	
# }
# else if(1.0<atof(b)&&atof(b)<2.0)
# {
# 	C.push_back(atof(b));
# 	
# }
# 	
# }


# //1
# int res=0;

# if(A.size()>=3)
# {
# priority_queue<double> q(A.begin(),A.end());  //priority queue used to get max 3 elements in O(logn) time
# double m=0;
# for(int i=0;i<=2;i++)
# {
# 	m+=q.top();
# 	q.pop();
# }

# if(m>1.0)
# {
# 	res=1;
# 	return res;
# }

# }
# //2
# if(A.size()>=2&&B.size()>=1)
# {
# priority_queue<double> q1(A.begin(),A.end());  //priority queue used to get max 2 elements in O(logn) time

# double m1=0;
# for(int i=0;i<=1;i++)
# {
# 	m1+=q1.top();
# 	q1.pop();
# }

# for(int i=0;i<B.size();i++)
# {
# 	if(1-m1<B[i]&&B[i]<2-m1)
# 	{
# 		res=1;
# 		return res;
# 	}

# }

# }

# //3
# if(A.size()>=2&&C.size()>=1)
# {
# priority_queue<double,std::vector<double>, std::greater<double> > q2(A.begin(),A.end());  //priority queue used to get min 2 elements in O(logn) time
# double m2=0;
# for(int i=0;i<=1;i++)
# {
#    m2+=q2.top();
#    q2.pop();	
# }

# double min=min_element(C);
# 	

# if(m2+min<2.0)
# {
# 	res=1;
# 	return res;
# }

# }

# //4
# if(B.size()>=2&&A.size()>=1)
# {
# priority_queue<double,std::vector<double>, std::greater<double> > q3(B.begin(),B.end()); //priority queue used to get min 2 elements in O(logn) time

# double m3=0;
# for(int i=0;i<=1;i++)
# {
# 	m3+=q3.top();
# 	q3.pop();
# }

# for(int i=0;i<A.size();i++)
# {
# 	if(A[i]<2-m3)
# 	{
# 		res=1;
# 		return res;
# 	}
# 	
# }

# }

# //5
# if(A.size()>=1&&B.size()>=1&&C.size()>=1)
# {
# int res3=0;
# double min1=min_element(A);
# double min2=min_element(B);
# double min3=min_element(C);
# if(min1+min2+min3<2&&min1+min2+min3>1)
# {
# 	res=1;
# 	return res;
# }

# }

# return res;
# // Time complexity =O(logn)+O(n)
# //hence,Time complexity=O(n)

# }

# Scala
# class Solution {
#     def solve(A: Array[String]): Int  = {
#         val arr = A.map(_.toFloat).sorted
        
#         def rec(left: Int, right: Int): Int = {
#             if (left >= right - 1) 0
#             else {
#                 val al0 = arr(left)
#                 val al1 = arr(left + 1)
#                 val rl0 = arr(right)
#                 val ss = al0 + al1 + rl0
#                 if (ss >= 2) rec(left, right - 1)
#                 else if (ss <= 1) rec(left + 1, right)
#                 else 1
#             }
#         }
        
#         rec(0, arr.length - 1)
#     }
# }
