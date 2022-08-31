//============================================================================
// Name        : NextSimilarNum.cpp
// Author      : dmtwong
// Version     :
// Copyright   : Math
// Description : Hello World in C++, Ansi-style
//============================================================================

//Problem Description
//
//Given a number A in a form of string.
//
//You have to find the smallest number that has same set of digits as A and is greater than A.
//
//If A is the greatest possible number with its set of digits, then return -1.
//Input Format
//First and only argument is an numeric string denoting the number A.
//Output Format
//Return a string denoting the smallest number greater than A with same set of digits , if A is the largest possible then return -1.
//Example Input
//Input 1:
// A = "218765"
//Input 2:
// A = "4321"
//Example Output
//Output 1:
// "251678"
//Output 2:
// "-1"


#include <iostream>
#include <string>
#include <algorithm>"
using namespace std;

//string Solution::solve(string A) {
string solve(string A) {
	int len_A = A.size();
	int curr_ix = len_A - 2;
	string notfound = to_string(-1);
	if (curr_ix == -1){
		return notfound;
	} else {
		while (curr_ix >= 0){
			if (A[curr_ix] < A[curr_ix +1]){
				break;
			}
			curr_ix -=1;
		}
	}
//	char temp = A[curr_ix];
//	A[curr_ix] = A[curr_ix + 1];
//	A[curr_ix + 1] = temp;
	int ix;
	for (ix = len_A - 1; curr_ix < ix; ix--){
		if (A[ix] > A[curr_ix]){
			char temp = A[curr_ix];
			A[curr_ix] = A[ix];
			A[ix] = temp;
			break;
		}
	}
	if (curr_ix == -1){
		return notfound;
	}
//	cout << ix << endl; // prints
//	cout << curr_ix << endl; // prints
//	cout << A[ix] << endl; // prints
//	cout << A[curr_ix] << endl; // prints

    reverse(A.begin()+ curr_ix + 1, A.end());

//	for (int i = 0; i < len_A; i++){
//		cout << A[i] << endl; // prints
//	}
//	cout << A << endl; // prints
	return A;
}

/*
Testing case
int main() {
//	string input_1 = "218765";
	string input_2 = "4321";
	string input_3 = "1234";
	string input_4 = "12";
	string input_5 = "1";
//	string output_1 = solve(input_1);
	string output_2 = solve(input_2);
	string output_3 = solve(input_3);
	string output_4 = solve(input_4);
	string output_5 = solve(input_5);
//	cout << output_1 << endl; // prints
	cout << output_2 << endl; // prints
	cout << output_3 << endl; // prints
	cout << output_4 << endl; // prints
	cout << output_5 << endl; // prints
	return 0;
}
*/

/* Editorial
string findNext(string number, int n)
{
   int i, j;

   // I) Start from the right most digit and find the first digit that is
   // smaller than the digit next to it.
   for (i = n-1; i > 0; i--)
       if (number[i] > number[i-1])
          break;

   // If no such digit is found, then all digits are in descending order
   // means there cannot be a greater number with same set of digits
   if (i==0)
   {
     return "-1";
   }

   // II) Find the smallest digit on right side of (i-1)'th digit that is
   // greater than number[i-1]
   char x = number[i-1];
   int smallest = i;
   for (j = i+1; j < n; j++)
       if (number[j] > x && number[j] < number[smallest])
           smallest = j;

   // III) Swap the above found smallest digit with number[i-1]
   swap(number[smallest], number[i-1]);
   string a=number.substr(i);
   string b=number.substr(0,i);
    // IV) Sort the digits after (i-1) in ascending order
   sort(a.begin(),a.end());
   string ans=b+a;
   return ans;
}

string Solution::solve(string A) {
    return findNext(A,A.size());
}*/
