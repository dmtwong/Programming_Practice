//============================================================================
// Name        : setMatrixZero2.cpp
// Author      : dmtwong
// Version     :
// Copyright   : Not efficient enough, run time too long
// Description : Hello World in C++, Ansi-style
//============================================================================



#include <iostream>
#include <vector>
using namespace std;

//void Solution::setZeroes(vector<vector<int> > &A) {
void setZeroes(vector<vector<int> > &A) {
	// Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
	int n_col = A[0].size();
	int n_row = A.size();
	int flag_col_null = 0;
	int flag_row_null = 0;
	for (int i = 0; i < n_col; i++){
		for(int j = 0; j < n_row; j++){
			if(A[i][j] ==0){
				if(i == 0){
					flag_row_null = 1;
				}
				if(j == 0){
					flag_col_null = 1;
				}
				A[i][0] = 0;
				A[0][j] = 0;
			}
		}

	}
	for (int i = 1; i < n_col; i++){
		for(int j = 0; j < n_row; j++){
			if( (A[i][0] == 0) || (A[0][j] == 0)){
				A[i][j] = 0;
			}
		}
	}
	if (flag_row_null){
		for (int j = 0; j < n_row; j++){
			A[0][j] = 0;
		}
	}
	if (flag_col_null){
		for (int i = 0; i < n_col; i++){
			A[i][0] = 0;
		}
	}
	//return A;
}

// Editorial
/*

void Solution::setZeroes(vector<vector<int> > &matrix) {
    int rownum = matrix.size();
    if (rownum == 0)  return;
    int colnum = matrix[0].size();
    if (colnum == 0)  return;

    bool hasZeroFirstRow = false, hasZeroFirstColumn = false;

    // Does first row have zero?
    for (int j = 0; j < colnum; ++j) {
        if (matrix[0][j] == 0) {
            hasZeroFirstRow = true;
            break;
        }
    }

    // Does first column have zero?
    for (int i = 0; i < rownum; ++i) {
        if (matrix[i][0] == 0) {
            hasZeroFirstColumn = true;
            break;
        }
    }

    // find zeroes and store the info in first row and column
    for (int i = 1; i < rownum; ++i) {
        for (int j = 1; j < colnum; ++j) {
            if (matrix[i][j] == 0) {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }

    // set zeroes except the first row and column
    for (int i = 1; i < rownum; ++i) {
        for (int j = 1; j < colnum; ++j) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0)  matrix[i][j] = 0;
        }
    }

    // set zeroes for first row and column if needed
    if (hasZeroFirstRow) {
        for (int j = 0; j < colnum; ++j) {
            matrix[0][j] = 0;
        }
    }
    if (hasZeroFirstColumn) {
        for (int i = 0; i < rownum; ++i) {
            matrix[i][0] = 0;
        }
    }
}

 */
