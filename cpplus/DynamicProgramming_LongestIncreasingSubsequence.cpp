//============================================================================
// Name        : DynamicProgramming_LongestIncreasingSubsequence.cpp
// Author      : dmtwong
// Version     :
// Copyright   : Simple array dp Q1
// Description : Hello World in C++, Ansi-style
//============================================================================

//Find the longest increasing subsequence of a given array of integers, A.
//In other words, find a subsequence of array in which the subsequence’s elements are in strictly increasing order, and in which the subsequence is as long as possible.
//This subsequence is not necessarily contiguous, or unique.
//In this case, we only care about the length of the longest increasing subsequence.
//Input Format:
//The first and the only argument is an integer array A.
//Output Format:
//Return an integer representing the length of the longest increasing subsequence.

#include <iostream>
#include <vector>
using namespace std;

//int Solution::lis(const vector<int> &A) {
int lis(const vector<int> &A) {
	int n_A = A.size();
	vector<int> result_list(n_A, 1);
	int max_result = 0;
	for (int i = 1; i < n_A; i++){
		for (int j = 0; j < i; j++){
			if ((A[i] > A[j]) and result_list[i] < result_list[j] + 1){
				result_list[i] = result_list[j] + 1;
			}
		}
	}

	for (int i = 0; i < n_A; i++){
		max_result = max(max_result, result_list[i]);
	}
	return max_result;
}

int main() {
	const vector<int> input_1 = {1, 2, 1, 5};
	const vector<int> input_2 = {0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15};
	int output_1 = lis(input_1);
	int output_2 = lis(input_2);
	cout << output_1 << endl; // prints
	cout << output_2 << endl; // prints
	return 0;
}
//
//Scala
//class Solution {
//    def lis(A: Array[Int]): Int  = {
//      val buff = Array.fill[Int](A.length)(1)
//      for {
//        i <- 1 until A.length
//        j <- 0 until i
//        if A(i) > A(j)
//      } buff(i) = math.max(buff(i), buff(j) + 1)
//      buff.max
//    }
//}

//GO:
//
//Editorial
//
//
// * @input A : Integer array
// *
// * @Output Integer
//
//func lis(A []int )  (int) {
//    output := 0
//    dp := make([]int, len(A))
//
//    for i, elem := range A {
//        for j := 0; j < i; j++ {
//            if (elem > A[j]) && (dp[i] < dp[j] + 1) {
//                dp[i] = dp[j] + 1
//            }
//            if dp[i] > output {
//                output = dp[i]
//            }
//        }
//    }
//
//    return output + 1
//}
