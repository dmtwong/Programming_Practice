//============================================================================
// Name        : strings_minCharReq2makeStrPalindrom.cpp
// Author      : dmtwong
// Version     :
// Copyright   : Strings Trick Q1
// Description : Output not expected, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>

using namespace std;

vector<int> find_lps(string subA){
//	cout << subA << endl; // prints
	int M = subA.length();
//	cout << M << endl; // prints
	vector<int> longestPreSuf(M, 0);
	int curr_len = 0;
	int counter = 1;
	longestPreSuf[0] = 0;
//		for (int i: longestPreSuf)
//		    std::cout << i << ' ';
	while (counter < M){
		if (subA[counter] == subA[curr_len]){
//			cout << "here" << endl; // prints
			curr_len += 1;
			longestPreSuf[counter] = curr_len;
			counter += 1;
		} else {
            if (curr_len != 0){
//            	cout << "there" << endl; // prints
            	curr_len = longestPreSuf[curr_len - 1];
            } else {
//            	cout << "yay" << endl; // prints
            	longestPreSuf[counter] = 0;
            	counter += 1;
            }
		}

//	for (int i: longestPreSuf)
//	    std::cout << i << ' ';
	}

	return longestPreSuf;
}
//int Solution::solve(string A) {
int solve(string A) {
    int n_A = A.length();
    string rev_A;
    rev_A = A;
    for (int i = 0; i < n_A / 2; i++)
        swap(rev_A[i], rev_A[n_A - i - 1]);
    string temp;
    temp = A + "#" + rev_A;
//	cout << temp << endl; // prints
    vector<int> lps_list;
    lps_list = find_lps(temp);
//	for (int i: lps_list)
//	    std::cout << i << ' ';
    int n_temp = lps_list.size() - 1;
//    cout << n_temp << endl;
    return n_A - lps_list[n_temp];
}

int main() {
	string test_1 = "ABC";
	string test_2 = "AACECAAAA";
	string test_3 = "hqghumeaylnlfdxfi";
	int out_1 = solve(test_1);
	int out_2 = solve(test_2);
	int out_3 = solve(test_3);
	cout << out_1 << endl; // prints
	cout << out_2 << endl;
	cout << out_3 << endl;
	return 0;
}
//def solve(self, A):
//    def findLPS(subA):
//        M = len(subA)
//        longestPreSuf = [None] * M
//        length = 0
//        longestPreSuf[0] = 0
//        i = 1
//        while i < M:
//            if subA[i] == subA[length]:
//                length += 1
//                longestPreSuf[i] = length
//                i += 1
//            else:
//                if length != 0:
//                    length = longestPreSuf[length - 1]
//                else:
//                    longestPreSuf[i] = 0
//                    i += 1
//        return longestPreSuf
//    rev_A = A[::-1]
//
//    temp = A + "%" + rev_A
//    lps = findLPS(temp)
//    return len(A) - lps[-1]
/* Editorial
#define all(x)            (x).begin(),(x).end()
vector<int> z_algorithm(string pattern) {
    int n = pattern.size();
    vector<int> Z(n, 0);
    Z[0] = n;
    int loc = 1;

    for (int i = 1; i < n; i++) {
        if (i < loc + Z[loc])
            Z[i] = min(Z[i - loc], loc + Z[loc] - i);

        while (i + Z[i] < n && pattern[Z[i]] == pattern[i + Z[i]])
            Z[i]++;

        if (i + Z[i] > loc + Z[loc])
            loc = i;
    }

    return Z;
}



int Solution::solve(string str) {
      string s;

      s =str;
      int n = s.size();

      string s3 = s;
      s3+='#';
      reverse(all(s));
      s3+=s;
      vector<int> v = z_algorithm(s3);
      int m = 2*n+1;
      int ans = n;
      for(int i = n + 1 ; i< m; i++){
        if(v[i] == m -i){
          ans = min(ans, n - (m-i));

        }
      }
      return ans;

}


 */
