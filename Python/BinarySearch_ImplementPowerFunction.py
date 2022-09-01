# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 10:54:43 2022

@author: mingt
"""

# def pow(self, x, n, d):
# Implement pow(x, n) % d.
# In other words, given x, n and d,

# find (xn % d)

# Note that remainders on division cannot be negative. In other words, make sure the answer you return is non negative.
def pow(x, n, d):
        result = 1
        base = x % d
        while (n > 0):
            if n % 2 == 1:
                result = (result * base) % d
            n = n // 2;
            base = (base * base) % d
        result = result % d 
        if (result < 0):
            result += d
        return result

# # # test
# A = 71045970
# B = 41535484
# C = 64735492
# a = 2
# b = 3
# c = 3

# pow(A, B, C)
# pow(a, b, c)

# # Editorial C
# long long powmode(long long b,long long n,long long d)
# {
#   if(n==0) return 1;
#   else{
#    long long ans=powmode(b,n/2,d)%d;
#       if(n%2) return ((ans*ans)%d*b)%d;
#       else return (ans*ans)%d;

#   }
# }
# int powmod(int x,int n,int d)
# {
#    if(x==0) return 0;
#    long long ans=powmode(x,n,d);
#     if(ans<0) return (ans+d)%d;
#     else ans;
#  }
# Editorial C++
# int Solution::pow(int x, int n, int p) {
#     assert(x >= -1e9 && x <= 1e9);
#     assert(n >= 0 && n <= 1e9);
#     assert(p >= 1 && p <= 1e9);
#     if (n == 0) return 1 % p;

# 			long long ans = 1, base = x;
# 			while (n > 0) {
# 				// We need (base ** n) % p. 
# 				// Now there are 2 cases. 
# 				// 1) n is even. Then we can make base = base^2 and n = n / 2.
# 				// 2) n is odd. So we need base * base^(n-1) 
# 				if (n % 2 == 1) {
# 					ans = (ans * base) % p;
# 					n--;
# 				} else {
# 					base = (base * base) % p;
# 					n /= 2;
# 				}
# 			}
# 			if (ans < 0) ans = (ans + p) % p;
# 			return ans;
# }
