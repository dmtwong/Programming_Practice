//============================================================================
// Name        : TwoPointers_PairWithGivenDiff.cpp
// Author      : dmtwong
// Version     :
// Copyright   : Two pointers, Takes too long to run for large input
// Description : Hello World in C++, Ansi-style
//============================================================================

//Problem Description
//Given an one-dimensional unsorted array A containing N integers.
//You are also given an integer B, find if there exists a pair of elements in the array whose difference is B.
//Return 1 if any such pair exists else return 0.
//Problem Constraints
//1 <= N <= 105
//-103 <= A[i] <= 103
//-105 <= B <= 105


/// Note to self after reading editoral code:
// 1.) put a into dict (python) to remove duplicated value


#include <iostream>
//#include <assert.h>
#include <vector>
#include <algorithm>

using namespace std;

//int Solution::solve(vector<int> &A, int B) {
int solve(vector<int> &A, int B) {
//	assert(B >= 1 && B <= 1e9);
    int len_A = A.size();
    int ix_last = len_A;
//    sort(A.begin(), A.end());

    for (int i = 0; i <= len_A; i++){
//    	cout << "New" << endl;
//		cout << i << endl;
        for (int j = len_A; j >= i+1; j--){
//        	cout << j << endl;
//        	cout << "here" << endl;
//        	cout << A[j] << endl;
//        	cout << A[i] << endl;
//        	cout << B << endl;
//        	cout << abs(B) << endl;
            if ((abs(A[j] - A[i])) == abs(B)){
//            	cout << "found!" << endl;
            	return 1;

            }
            if (abs(A[j] - A[i]) < abs(B)){
				ix_last = j;
            }
        }
//
//        cout << len_A << endl;
//        cout << "End" << endl;
    }
    return 0;
}
// Test
//int main() {
//	vector<int> input_1_a = {5, 10, 3, 2, 50, 80};
//	vector<int> input_2_a= {-10, 20};
//	int input_1b = 78, input_2b = 30;
//	int output_1 = solve(input_1_a, input_1b), output_2 = solve(input_2_a, input_2b);
//	vector<int> input_3a = {-509, -5};
//	int input_3b = -95173;
//	int output_3 = solve(input_3a, input_3b);
//	vector<int> input_4a = {-533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297, 811, 322 };
//	int input_4b = 369;
//	int output_4 = solve(input_4a, input_4b);
//	vector<int> input_5a = {20, 500, 1000, 200};
//	int input_5b = 0;
//	int output_5 = solve(input_5a, input_5b);
//
//
//	cout << output_1 << endl; // prints
//	cout << output_2 << endl; // prints
//	cout << output_3 << endl; // prints
//	cout << output_4 << endl; // prints
//	cout << output_5 << endl; // prints
//
//	return 0;
//}

//Editorial: Python
//class Solution:
//    # @param A : list of integers
//    # @param B : integer
//    # @return an integer
//    def solve(self, A, B):
//        temp=dict()
//        for a in A:
//            try:
//                temp[a]=temp[a]+1
//            except KeyError:
//                temp[a]=1
//
//        for a in A:
//            if((B+a)==a and temp[a]>1):
//                return 1
//            elif(B+a==a):
//                continue
//            elif(temp.get(B+a,0)!=0):
//                return 1
//        return 0


// C++
//bool findPair(vector<int>&arr, int size, int n)
//{
//    // Initialize positions of two elements
//    int i = 0;
//    int j = 1;
//   sort(arr.begin(),arr.end());
//    // Search for a pair
//    while (i < size && j < size)
//    {
//        if (i != j && arr[j] - arr[i] == n)
//        {
//            return true;
//        }
//        else if (arr[j]-arr[i] < n)
//            j++;
//        else
//            i++;
//    }
//    return false;
//}
//int Solution::solve(vector<int> &A, int B) {
//    return findPair(A,A.size(),B);
//}
//
//Scala
//class Solution {
//    def solve(A: Array[Int], B: Int): Int  = {
//
//        import scala.collection.mutable
//        import scala.collection.mutable.HashMap
//        val arr = A.sorted
//        val diff = B
//        val map = new mutable.HashMap[Int, Boolean]()
//        var status = false
//
//        for(num <- arr) {
//
//          if(map.contains(num)) {
//            status = true
//          } else {
//            map.put(diff + num, true)
//            map.put(num - diff, true)
//          }
//        }
//        if(status) 1 else 0
//    }
//}

//
// * @input A : Integer array
// * @input n1 : Integer array's ( A ) length
// * @input B : Integer
// *
// * @Output Integer
//

//C
//int solve(int* A, int n1, int B) {
//    int arr[2001] = {0}, *map, i;
//
//    // make a map from -1000 to +1000
//    map= &arr[1000];
//
//    // map all the array numbers
//    for(i=0; i<n1; i++) map[A[i]]++;
//
//    for(i=0; i<n1; i++){
//        // printf("A[i]-%d , A[i]+B-%d, map a,b %d",A[i], A[i]+B,  map[A[i]+B] );
//
//        if((A[i]+B>= -1000 && A[i]+B <=1000 )) //check if number falls under range (-1000, 1000)
//        if((B==0 && map[-1*(A[i]+B)] >0 )||(B !=0 && map[A[i]+B] > 0)) return 1;
//        // if B == 0 check for index of (-1 * number)
//        // if B != 0 check for index A[i]+B.
//    }
//    return 0;
//}

