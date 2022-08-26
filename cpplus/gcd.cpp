//============================================================================
// Name        : gcd.cpp
// Author      : dmtwong
// Version     :
// Copyright   : 
// Description : gcd, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

//int Solution::gcd(int A, int B) {
int gcd(int A, int B) {
	int min_AB;
	min_AB = (A>B)?B:A;

	if(min_AB == 0){
		return (A>B)?A:B;
	} else if (min_AB == 1){
		return 1;
	}
    for (int i = min_AB; i > 0; i--){
    	if ((A%i == 0) and (B%i == 0)){
    		return i;
    	}
    }
    return 1;
}

/* Editorial: recursive
 * 6, 9 => 9, 6, gcd(3, 6) => 6, 3 => gcd(0,3) => 3,0, return 3 checked
 *  int Solution::gcd(int m, int n) {

        if(m < n)
               swap(m, n);

        if(n == 0)
               return m;


        return gcd(m % n, n);
  }
 */
