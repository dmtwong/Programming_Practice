//============================================================================
// Name        : primeSum.cpp
// Author      : dmtwong
// Version     :
// Copyright   : Math 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
using namespace std;

bool isPrime(int x){
	if(x == 2 or x == 3){
		return true;
	}
	int mid = int(x / 2);
//	cout << mid << endl; // prints
	for (int i = 2; i <= mid + 1; i++){
//		cout << i << endl; // prints
		if(x % i == 0){
			return false;
		}
	}
	return true;
}

//vector<int> Solution::primesum(int A) {
vector<int> primesum(int A) {
	int mid = int(A / 2);
	vector<int> result = {0, 0};

	for (int i = 2; i <= mid + 1; i++){
		int temp_1 = i, temp_2 = A-i;
		if ((isPrime(temp_1) == true) and (isPrime(temp_2) == true)){
			result = {temp_1, temp_2};
			for (int num = 0; num < 2; num += 1){
//				cout << "there" << endl; // prints
//				cout << result[num] << endl; // prints
			}
			return result;
		}
	}
//	for (int num = 0; num < 2; num += 1){
//		cout << "here" << endl; // prints
//		cout << result[num] << endl; // prints
//	}
	return result;
}


int main() {
	int input_1 = 4;
	int input_2 = 5;
	int input_3 = 6;
	int input_4 = 7;
	int input_5 = 378;
//	vector<int> input_2 = {0, 4, 7, 9};
	vector<int> output_1 = primesum(input_1);
	vector<int> output_2 = primesum(input_2);
	vector<int> output_3 = primesum(input_3);
	vector<int> output_4 = primesum(input_4);
	vector<int> output_5 = primesum(input_5);
//	cout << output_1 << endl; // prints
//	cout << output_2 << endl; // prints
//	cout << output_3 << endl; // prints
	return 0;
}


//Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.
//
//NOTE A solution will always exist. read Goldbach’s  conjecture
//
//Example:
//
//
//Input : 4
//Output: 2 + 2 = 4
//
//If there are more than one solutions possible, return the lexicographically smaller solution.
//
//If [a, b] is one solution with a <= b,
//and [c,d] is another solution with c <= d, then
//
//[a, b] < [c, d]
//
//If a < c OR a==c AND b < d.


/* Editorial
vector<int> Solution::primesum(int A) {
    int n=A;
    int i,j;

    vector<bool>v(n+1, true);
    v[0] = false;
    v[1] = false;

    vector<int>m(2,0);

    for(i=2;i<=n;i++)
    {
        if (i > n/i) {
            break;
        }
        if(v[i])
        {
            //m.push_back(i);
            for(j=i*i;j<=n;j+=i)
            {
                v[j]=false;
            }
        }
    }

    for (i = 2; i <= A/2; ++i) {
        if (v[i] && v[A-i]) {
            m[0] = i;
            m[1] = A-i;
            return m;
        }
    }

    return m;
}
 *
 */

/* Editorial Python
class Solution:
    def primesum(self, n):
        for i in xrange(2, n):
            if self.is_prime(i) and self.is_prime(n - i):
                return i, n - i

    def is_prime(self, n):
        if n < 2:
            return False

        for i in xrange(2, int(n**0.5) + 1):
            if n % i == 0:
                return False

        return True
 */

/* Scala
class Solution {
    def primesum(A: Int): Array[Int]  = {
      def sieve(n: Int): Array[Boolean] = {
        val arr = Array.fill[Boolean](n + 1)(true)
        arr(0) = false
        arr(1) = false
        var i = 2
        while (i * i <= n) {
          if (arr(i)) {
            for (j <- i * 2 to n by i) arr(j) = false
          }
          i = i + 1
        }
        arr
      }

      val arr = sieve(A)
      for (i <- 0 until A) {
        if (arr(i) && arr(A - i)) return Array(i, A - i)
      }
      Array()
    }
}

 */

/* C
int isprime(int a)
{
    int i;
    for(i=2;i<=sqrt(a);i++)
    {
        if(a%i==0)
            return 0;
    }
    return 1;
}
int* primesum(int A, int *len1) {
    *len1 = 2;
    int i=2;
    int *a = (int *)malloc(2*sizeof(int));
    for(i=2;i<=A/2;i++)
    {
        //printf("\n%d %d %d %d",i,A-i,isprime(i),isprime(A-i));
        if(isprime(i)&&isprime(A-i))
        {
            a[0] = i;
            a[1] = A-i;
            return a;
        }
        if(i!=2)
            i++;

    }

}
 */
