//============================================================================
// Name        : ExcelColNum.cpp
// Author      : dmtwong
// Version     :
// Copyright   : 
// Description : ExcelColNum, Ansi-style
//============================================================================

#include <iostream>
#include <map>
#include <cmath>
#include <string>


using namespace std;


//
//int Solution::titleToNumber(string A) {
int titleToNumber(string A) {
	int len_A = A.length();
//	char full_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

	int result = 0;
	int deg = len_A;
	for (int i = 0; i < len_A; i++){
		result += pow(26, deg-1) * (int(A[i])-64);
		deg -= 1;
	}
	return result;
}

int main() {
	string input_1 = "A";
	string input_2 = "AB";
	int test_1 = titleToNumber(input_1);
	int test_2 = titleToNumber(input_2);
	cout << test_1 << endl; // prints ExcelColNum
	cout << test_2 << endl;
	return 0;
}

/* Editorial
 * int Solution::titleToNumber(string A) {
int res=0;
for (const auto& c:A) {res =res*26+c +1 - 'A';}return res;
}
 */
