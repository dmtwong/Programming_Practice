//============================================================================
// Name        : bishopmove.cpp
// Author      : dmtwong
// Version     :
// Copyright   : 
// Description : TotMoves4Bishop, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

//int Solution::solve(int A, int B) {
int solve(int A, int B) {
	int row_left, row_right, col_up, col_down;
	row_left = B - 1;
	row_right = 8 - B;
	col_up = 8-A;
	col_down = A - 1;

	int quad_1, quad_2, quad_3, quad_4, tot;
	quad_1 = (row_right > col_up)?col_up:row_right;
	quad_2 = (row_right > col_down)?col_down:row_right;
	quad_3 = (row_left > col_down)?col_down:row_left;
	quad_4 = (row_left > col_up)?col_up:row_left;

	return tot = quad_1+quad_2+quad_3+quad_4;
}


/* Editorial
 * int Solution::solve(int A, int B) {


    return min(B-1,A-1) + min(8-B,A-1) + min(8-B,8-A) + min(B-1,8-A);


}
 *
 *
 */
