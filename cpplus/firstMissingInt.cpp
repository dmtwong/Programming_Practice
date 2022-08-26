//============================================================================
// Name        : firstMissingInt.cpp
// Author      : dmtwong
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
using namespace std;

//int Solution::firstMissingPositive(vector<int> &A) {
int firstMissingPositive(vector<int> &A) {
    //int max_A = *max_element(A.begin(), A.end()); //[1,1,1] max:1
    int max_A = 1;
	int n_A = A.size(); //3
    if(max_A < 1){
        return 1;
    }
    if(n_A == 1){
        if (A[0] == 1){
            return 2;
        } else {
            return 1;
        }
    }
    vector<int> result(max_A, 0); // 0, 0 ,0

    //i = 0: A[0]>0 result result[0]!=1 => become 1
    int i = 0;
    // return i;
    for (i = 0; i <= n_A; i++){
        if(A[i] > 0){ //i = 1, 2, same
//        	cout << A[i] - 1 << endl;
//        	cout << result[A[i] - 1] << endl;
            if(result[A[i] - 1] != 1){
                result[A[i] - 1] = 1;
            }
        }
    }
    //int len_result = result.size();
    //int counter = 0;
//   	cout << result[0] << endl;
//   	cout << result[1] << endl;
//   	cout << result[2] << endl;
    int j;
    for (j = 0; j < max_A; j++){
        if(result[j] == 0){
            //counter += 1;
            return j+1;
//            cout << "Ar" << endl;
            }
        }
    //return counter + 2;
//    cout << j << endl;
    return j + 1;
}

//int main() {
//	//firstMissingPositive(vector<int>);
//	vector<int> A(3, 1);
//	int result2 = firstMissingPositive(A);
//	cout << result2 << endl; // prints rev int
//	return result2;
//}

/* Editorial
class Solution {
    public:
        int firstMissingPositive(vector<int> &A) {
            int n = A.size();
            for (int i = 0; i < n; i++) {
                if (A[i] > 0 && A[i] <= n) {
                    int pos = A[i] - 1;
                    if (A[pos] != A[i]) {
                        swap(A[pos], A[i]);
                        i--;
                    }
                }
            }
            for (int i = 0; i < n; i++) {
                if (A[i] != i + 1) return (i + 1);
            }
            return n + 1;
        }
};
*/

//int firstMissingPositive(vector<int> &A) {
/*
int Solution::firstMissingPositive(vector<int> &A) {
    int max_A = *max_element(A.begin(), A.end()); //[1,1,1] max:1
    int n_A = A.size(); //3
    if(max_A < 1){
        return 1;
    }
    if(n_A == 1){
        if (A[0] == 1){
            return 2;
        } else {
            return 1;
        }
    }
    vector<int> result(max_A, 0); // 0, 0 ,0
    //i = 0: A[0]>0 result result[0]!=1 => become 1
    int i;
    for (i = 0; i < n_A; i++){
        if(A[i] > 0){ //i = 1, 2, same
            if(result[A[i] - 1] != 1){
                result[A[i] - 1] = 1;
            }
        }
    }
    int len_result = result.size();
    int counter = 0;
    for (i = 0; i < len_result; i++){
        if(result[i] == 0){
            counter += 1;
            return i+1;
            }
        }
    return counter + 2;
    //return i + 2;
}
*/
