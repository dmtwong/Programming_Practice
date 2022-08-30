//============================================================================
// Name        : singleNumber.cpp
// Author      : dmtwong
// Version     :
// Copyright   : Bit Manipulation 
// Description : Hello World in C++, Ansi-style
//============================================================================

//Problem Description
//
//
//
//Given an array of integers A, every element appears twice except for one. Find that single one.
//
//
//NOTE: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
//
//
//
//Problem Constraints
//1 <= |A| <= 2000000
//
//0 <= A[i] <= INTMAX
//
//
//
//Input Format
//First and only argument of input contains an integer array A.
//
//
//
//Output Format
//Return a single integer denoting the single element.
//
//
//
//Example Input
//Input 1:
//
// A = [1, 2, 2, 3, 1]
//Input 2:
//
// A = [1, 2, 2]
//
//
//Example Output
//Output 1:
//
// 3
//Output 2:
//
// 1
//
//
//Example Explanation
//Explanation 1:
//
//3 occurs once.
//Explanation 2:
//
//1 occurs once.


#include <iostream>
#include <vector>
using namespace std;

//int Solution::singleNumber(const vector<int> &A) {
int singleNumber(const vector<int> &A) {
	int result = 0;
	int n_A = A.size();

	for (int i = 0; i < n_A; i++){
		result = result ^ A[i];
	}
	return result;
}

int main() {
	vector<int> input_1 = {1, 2, 2, 3, 1};
	vector<int> input_2 = {1, 2, 2};
	int output_1 = singleNumber(input_1);
	int output_2 = singleNumber(input_2);
	cout << output_1 << endl; // prints
	cout << output_2 << endl; // prints
	return 0;
}


/* Scala
class Solution {
    def singleNumber(A: Array[Int]): Int  = {
        var res = 0
        A.foreach(ai => res = res ^ ai)
        res
    }
}

 */

/* GO
 * @input A : Integer array
 *
 * @Output Integer

func singleNumber(numbers []int) (int) {
	number := 0
	for i := 0; i < len(numbers); i++ {
		number ^= numbers[i]
	}

	return number
}
 *
 */

//C
//int singleNumber(const int* A, int n1){
//
//    int index = 0 ;
//    int result = 0 ;
//
//    for (index = 0 ; index < n1 ; index ++) {
//
//        result = result ^ A[index];
//    }
//    return result;
//}
