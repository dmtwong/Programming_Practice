//============================================================================
// Name        : TwoPointers_RemoveDuplicatesfromSortedArray.cpp
// Author      : dmtwong
// Version     :
// Copyright   : Simple array dp Q1
// Description : Hello World in C++, Ansi-style
//============================================================================
//Problem Description
//Given a sorted array A consisting of duplicate elements.
//Your task is to remove all the duplicates and return the length of sorted array
//		of distinct elements consisting of all distinct elements present in A.
//Input Format
//First and only argurment containing the integer array A.
//Output Format
//Return a single integer, as per the problem given.
//Example Input
//Input 1:
//A = [1, 1, 2]
//Input 2:
//A = [1, 2, 2, 3, 3]
//Example Output
//Output 1:
//2
//Output 2:
//3
//Example Explanation
//Explanation 1:
//Updated Array: [1, 2, X] after rearranging. Note that there could be any number in place of x since we dont need it.
//We return 2 here.
//Explanation 2:
//Updated Array: [1, 2, 3, X, X] after rearranging duplicates of 2 and 3.
//We return 3 from here.

#include <iostream>
#include <vector>
using namespace std;

//int Solution::removeDuplicates(vector<int> &A) {
int removeDuplicates(vector<int> &A) {

    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
	int n_A = A.size();
//	int low_A = A[0];
//	int max_A = A[n_A - 1];
	int longest_A = n_A;
	int result_A = longest_A;
	vector <int> unique_A;
	unique_A.push_back(A[0]);
	for (int i = 1; i < n_A; i++){
		if (A[i] == A[i-1]){
			result_A -= 1;
			continue;
		}
		unique_A.push_back(A[i]);
	}
	A = unique_A;
	return result_A;

}

//Testing
//int main() {
//	vector <int> input_1 = {1, 2, 2, 3, 3};
//	vector <int> input_2 = {1, 1, 2};
//
//	int output_1 = removeDuplicates(input_1);
//	int output_2 = removeDuplicates(input_2);
//
//	cout << output_1 << endl; // prints
//	cout << output_2 << endl; // prints
//
//	return 0;
//}
//Editorial;
//int Solution::removeDuplicates(vector<int> &A) {
//  			int count = 0, n = A.size();
//			for (int i = 0; i < n; i++) {
//				if (i < n - 1 && A[i] == A[i+1]) continue;
//				else {
//					A[count] = A[i];
//					count++;
//				}
//			}
//			return count;
//
//
//}


