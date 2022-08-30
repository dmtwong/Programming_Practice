//============================================================================
// Name        : TwoPointers_MergeTwoSortedLists.cpp
// Author      : dmtwong
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


//void Solution::merge(vector<int> &A, vector<int> &B) {
void merge(vector<int> &A, vector<int> &B) {
	// Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
	int n_A = A.size();
	int n_B = B.size();
	int n_Comb = n_A + n_B;
//	vector<int> input_2 = {0, 4, 7, 9};
	A.insert(end(A), begin(B), end(B));
	sort(A.begin(), A.begin()+n_Comb);
//	return A;
}



int main() {
	vector<int> input_1a = {1, 5, 8};
	vector<int> input_1b = {6, 9};
	merge(input_1a, input_1b);
//	cout << input_1a << endl; // prints Two Pointers Q1
	for (int i: input_1a)
	    std::cout << i << ' ';
	return 0;
}


// allocate space to temp store and then resize A to transfer
/* Editorial C++
void Solution::merge(vector<int> &A, vector<int> &B) {
    int m = A.size();
    int n = B.size();
    int temp[m+n+2];
    int indexA = 0, indexB = 0;
    for (int i = 0; i < m+n; i++){
        if (indexB == n || (indexA < m && A[indexA] < B[indexB])) {
            temp[i] = A[indexA];
            indexA++;
        } else {
            temp[i] = B[indexB];
            indexB++;
        }
    }
    A.resize(m + n);
    for (int i = 0; i < m+n; i++) {
        A[i] = temp[i];
    }
    return;
}
 *
 *
 */

/* Python
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        i=0
        j=0
        l=[]
        while(i<len(A) and j<len(B)):
            if(A[i]>B[j]):
                A.insert(i,B[j])
                j+=1
            else:
                i+=1
        while(j<len(B)):
            A.append(B[j])
            j+=1

 *
 */

/* Java
public class Solution {
	public void merge(ArrayList<Integer> A, ArrayList<Integer> B) {
	    int m, n;
	    ArrayList<Integer> res = new ArrayList<>();

	    if (A == null && B == null)
	        return;

	    if (A == null) {
	        A = B;
	        return;
	    }

	    if (B == null)
	        return;

	    m = A.size();
	    n = B.size();

	    int i, j;
	    int k = 0;

	    for (i = 0, j = 0; k < m + n; k++) {
	        if (i >= m)
	            res.add(B.get(j++));
	        else if (j >= n)
	            res.add(A.get(i++));
	        else if (A.get(i) <= B.get(j)) {
	            res.add(A.get(i));
	            i++;
	        } else {
	            res.add(B.get(j));
	            j++;
	        }
	    }

	    A.clear();

	    for (int num : res)
	        A.add(num);

	    return;

	}
}
 *
 */
