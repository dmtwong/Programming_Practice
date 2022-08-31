//============================================================================
// Name        : array_MinStepsInInfGrid.cpp
// Author      : dmtwong
// Version     :
// Copyright   : Array
// Description : Hello World in C++, Ansi-style
//============================================================================

//Problem Description
//You are in an infinite 2D grid where you can move in any of the 8 directions
// (x,y) to
//    (x-1, y-1),
//    (x-1, y)  ,
//    (x-1, y+1),
//    (x  , y-1),
//    (x  , y+1),
//    (x+1, y-1),
//    (x+1, y)  ,
//    (x+1, y+1)
//You are given a sequence of points and the order in which you need to cover the points.. Give the minimum number of steps in which you can achieve it. You start from the first point.
//NOTE: This question is intentionally left slightly vague. Clarify the question by trying out a few cases in the “See Expected Output” section.
//Input Format
//Given two integer arrays A and B, where A[i] is x coordinate and B[i] is y coordinate of ith point respectively.
//Output Format
//Return an Integer, i.e minimum number of steps.
//Example Input
//Input 1:
// A = [0, 1, 1]
// B = [0, 1, 2]
//Example Output
//Output 1:
// 2

#include <iostream>
#include <vector>

using namespace std;

//int Solution::coverPoints(vector<int> &A, vector<int> &B) {
int coverPoints(vector<int> &A, vector<int> &B) {
	int steps = 0;
	int n_points = A.size();
	if (n_points <= 1){
//		cout << "one or no points" << endl; // prints
		return steps;
	} else {
		for (int i = 0; n_points > i + 1;i++){
			steps += max(abs(A[i+1]-A[i]), abs(B[i+1] - B[i]));
		}
//		cout << steps << endl; // prints
		return steps;
	}
}


int main() {
	vector<int> input_1a = {0, 1, 1};
	vector<int> input_1b = {0, 1, 2};
	int output_1 = coverPoints(input_1a, input_1b) ;
//	cout << output_1 << endl; // prints
	return 0;
}

/* Editorial
// Input : X and Y co-ordinates of the points in order.
// Each point is represented by (X[i], Y[i])
int Solution::coverPoints(vector<int> &X, vector<int> &Y) {
    int res=0;
    for(int i=0; i<X.size()-1; i++) {
        res+=max(sqrt((X[i]-X[i+1])*(X[i]-X[i+1])), sqrt((Y[i]-Y[i+1])*(Y[i]-Y[i+1])));
    }
    return res;
}*/
/*

Scala:
class Solution {
    def coverPoints(A: Array[Int], B: Array[Int]): Int  = {
        var sum = 0
        for (i <- 1 until A.length) {
            val a = math.abs(A(i) - A(i - 1))
            val b = math.abs(B(i) - B(i - 1))
            sum = sum + math.max(a, b)
        }
        sum
    }
}

*/
