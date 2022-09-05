//============================================================================
// Name        : TwoPointers_MaxOnesAfterMod.cpp
// Author      : dmtwong
// Version     :
// Copyright   : Tricks Q1
// Description : Hello World in C++, Ansi-style
//============================================================================

//Problem Description
//Given a binary array A and a number B, we need to find length of the longest subsegment of ‘1’s possible by changing at most B ‘0’s.
//Problem Constraints
// 1 <= N, B <= 105
// A[i]=0 or A[i]=1
//Input Format
//First argument is an binary array A.
//Second argument is an integer B.
//Output Format
//Return a single integer denoting the length of the longest subsegment of ‘1’s possible by changing at most B ‘0’s.

#include <iostream>
#include <vector>
using namespace std;

//int Solution::solve(vector<int> &A, int B) {
int solve(vector<int> &A, int B) {
	int count = 0;
	int left_ix = 0;
	int result = 0;
	int n_A = A.size();

	for (int i = 0; i < n_A; i++){
		if (A[i] == 0){
			count += 1;
		}
		while (count > B){
			if (A[left_ix] == 0){
				count -= 1;
			}
			left_ix += 1;
		}
		result = max(result, i - left_ix + 1);
	}
	return result;
}


int main() {
	vector <int> A1 = {1, 0, 0, 1, 1, 0, 1};
	int B1 = 1;
	int out1 = solve(A1,B1);
	vector <int> A2 = {1, 0, 0, 1, 0, 1, 0, 1, 0, 1};
	int B2 = 2;
	int out2 = solve(A2,B2);
	cout << out1 << endl;
	cout << out2 << endl;
  	return 0;
}


//Editorial C:
// * @input A : Integer array
// * @input n1 : Integer array's ( A ) length
// * @input B : Integer
// *
// * @Output Integer
//
//int solve(int* A, int n1, int B) {
//    int n=n1;
//    int l=0, i=0, count=0;
//    int ans=INT_MIN;
//    for(i=0;i<n;i++){
//        if(A[i]==0){
//            count++;
//        }
//        while(count>B){
//            if(A[l]==0)count--;
//            l++;
//        }
//        ans=ans>i-l+1?ans:i-l+1;
//    }
//    return ans;
//}

//Scala:
//
//class Solution {
//    def solve(A: Array[Int], B: Int): Int  = {
//
//        val arr = A
//        val maxUpdates = B
//
//        var currUpdates = 0
//        var start = 0
//        var end = 0
//
//        while(currUpdates < maxUpdates && end < arr.size) {
//          if(arr(end) == 0) currUpdates = currUpdates + 1
//          end = end + 1
//        }
//
//        while(end < arr.size && arr(end) == 1) end = end + 1
//
//        if(end == arr.size) return arr.size
//
//        var currSize = (end - 1) - start + 1
//        var maxSize = currSize
//
//        while(end < arr.size) {
//
//          arr(start) match {
//            case 0 => {
//              start = start + 1
//            }
//            case 1 => {
//              while(start < arr.size && arr(start) == 1) start = start + 1
//              start = start + 1
//            }
//          }
//
//          var counter = 0
//          while(end < arr.size && (counter < 1 || arr(end) == 1)) {
//            if(arr(end) == 0) counter = counter + 1
//            end = end + 1
//          }
//
//          if(end == arr.size) return Math.max(maxSize, (end - 1) - start + 1)
//
//          currSize = (end-1) - start + 1
//          maxSize = Math.max(currSize, maxSize)
//        }
//
//        maxSize
//    }
//}
//

//GO:
// * @input A : Integer array
// * @input B : Integer
// *
// * @Output Integer
//func solve(A []int , B int )  (int) {
//    maxLen,l,count:=0,0,0
//    for i:=0;i<len(A);i++{
//        if A[i]==0{
//            count++
//        }
//        for count > B{
//            if A[l]==0{
//                count--
//            }
//            l+=1
//        }
//        currLen := i-l+1
//        if currLen > maxLen{
//            maxLen = currLen
//        }
//    }
//    return maxLen
//}
