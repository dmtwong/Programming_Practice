//============================================================================
// Name        : ReverseInteger.cpp
// Author      : dmtwong
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int numDigits(int aNum){
    int digits = 0;
    while (aNum){
    	aNum /= 10;
        digits++;
    }
    return digits;
}

int reverse(int A) {
//int Solution::reverse(int A) {
	bool isNeg = false;
	int result = 0;
	int prev = 0;
	int curr_digit;

	if (A < 0){
		isNeg = true;
		A = -A;
	}


//	int num_D = numDigits(A);
//	if (num_D == 10){
//		if ((A%10) >= 2){
//			return 0;
//		}
//	}

//	int counter = 0;
	while(A != 0){
		// cout << prev << endl;
		// cout << result << endl;
		curr_digit = A%10;

		//		cout << "hi" << endl;
//		cout << curr_digit << endl;

		result = (result * 10) + curr_digit;

		if (result >= 2147483647 or result <= -2147483648){
//			cout << "type 1 overflow" << endl;
			return 0;
		}

		if (int((result - curr_digit) / 10) != prev){

			//int temp = int((result - curr_digit)/ 10);
//			cout << temp << endl;
//			cout << prev << endl;
//			cout << "type 2 overflow" << endl;
			return 0;
		}
		prev = result;
		A = int(A / 10);
//		cout << "bye" << endl;
//		cout << result << endl;
	}
	if (isNeg == true){
		return -result;
	} else {
		return result;
	}
}
// testing case
int main() {
	int test_1 = reverse(123);
	int test_2 = reverse(-123);
	int test_3 = reverse(1000000045);
	int test_4 = reverse(-1000000045);
	int test_5 = reverse(214748364);
	int test_6 = reverse(2147483647);
	int test_7a = reverse(1463847512);
	int test_7b = reverse(1463847112);
	int test_8a = reverse(-1463847512);
	int test_8b = reverse(-1463847112);

	int test_fail_1 = reverse(-1146467285);
	int test_fail_2 = reverse(-1170064042);

	cout << test_1 << endl;
	cout << test_2 << endl;
	cout << test_3 << endl;
	cout << test_4 << endl;
	cout << test_5 << endl;
	cout << test_6 << endl;
	cout << test_7a << endl;
	cout << test_7b << endl;
	cout << test_8a << endl;
	cout << test_8b << endl;

	cout << test_fail_1 << endl;
	cout << test_fail_2 << endl;
	return 0;
}

/* Editorial
int Solution::reverse(int A) {
    long long int ans = 0;
    while (A != 0) {
        ans = ans*10 + A%10;
        A = A/10;
    }
    if (ans > INT_MAX || ans < INT_MIN) return 0;
    else return ans;
}
 *
 */
