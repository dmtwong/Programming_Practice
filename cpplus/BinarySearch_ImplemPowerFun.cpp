//============================================================================
// Name        : BinarySearch_ImplemPowerFun.cpp
// Author      : dmtwong
// Version     :
// Copyright   : Binary Search
// Description : Hello World in C++, Ansi-style
//============================================================================

//Problem Description
//Implement pow(x, n) % d.
//In other words, given x, n and d,
//find (xn % d)
//Note that remainders on division cannot be negative. In other words, make sure the answer you return is non negative.
//

#include <iostream>
using namespace std;

//int Solution::pow(int x, int n, int d) {
int pow(int x, int n, int d) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
	int result = 1;
	long long base = x % d;
	while (n > 0){
		if (n % 2 == 1){
			result = (result * base) % d;
		}
//		n = n / 2;
		n = n >> 1;

//		bool overflow = true;
//		int count = 0;
//		while (overflow == true){
//			int temp = (base * base);
//			if (base != 0 && temp / base != base) {
//				cout << "overflowed!" << endl; // prints
//				base /= 2;
//				count += 1;
//			} else{
//				break;
//			}
		long long temp = (base * base);
		base = temp % d;
	}
	result = result % d;
	if (result < 0){
		result += d;
	}
//	cout << result << endl; // prints
	return result;
}

//
//int main() {
////	int input_test_4_a = -1, input_test_4_b = 1, input_test_4_c = 20;
//	int input_test_5_a = 71045970, input_test_5_b = 41535484, input_test_5_c = 64735492;
//
////	int input_output_4 = pow(input_test_4_a, input_test_4_b, input_test_4_c);
//	int input_output_5 = pow(input_test_5_a, input_test_5_b, input_test_5_c);
//	//	cout << "" << endl; // prints
//	return 0;
//}
