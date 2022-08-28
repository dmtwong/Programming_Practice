//============================================================================
// Name        : findMinXor.cpp
// Author      : dmtwong
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>

#include <algorithm>

using namespace std;


//int Solution::findMinXor(vector<int> &A) {
int findMinXor(vector<int> &A) {
	int n_A = A.size();
	sort(A.begin(), A.end());
	int result = 2147483647; // max or else overflowed
	int curr_compare;
	for (int i = 0; i < (n_A - 1); i++){
		curr_compare = A[i] ^ A[i+1];
		result = min(curr_compare, result);
	}
	return result;
}

// Testing
int main() {
//	vector<int> input_1 = {0, 2, 5, 7};
	vector<int> input_2 = {0, 4, 7, 9};
//	int test_1 = findMinXor(input_1);
	int test_2 = findMinXor(input_2);
	cout << test_2 << endl; // prints findMinXor
	return 0;
}

/*
 Editorial
 int Solution::findMinXor(vector<int> &numbers) {
    sort(numbers.begin(), numbers.end());
    int smallestXor = numbers[0] ^ numbers[1];
    for (int i = 2; i < numbers.size(); i ++) {
        smallestXor = min(smallestXor, numbers[i - 1] ^ numbers[i]);
    }
    return smallestXor;
}
 */

/* Python
class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        s = sorted(A)
        minn = s[0]^s[1]
        for i in range(1,len(A)):
            if(s[i]^s[i-1]<minn):
                minn = s[i]^s[i-1]
        return minn

 */

/* Scala
 class Solution {
    def findMinXor(A: Array[Int]): Int  = {
        A.sorted.sliding(2).map(arr => arr(1) ^ arr(0)).min
    }
}
 */

