/*
 *  This solution is **NOT** mine. I generated it with
 *  ChatGPT because I wanted to understand how to solve
 *  a problem like this. It is left in this repo because
 *  it may be helpful to me or others. 
 */


#include<bits/stdc++.h>
using namespace std;

int main(int argc, char* argv[]) {
    unsigned int n = 0;
    while (true) {
        cin >> n;

        if (n == 0) break;

        unsigned int result = n;
        unsigned int p = 2;

        while (p * p <= n) {
            if (n % p == 0) {
                while (n % p == 0) {
                    n /= p;
                } 
                result -= result / p;
            }
            p++;
        }

        if (n > 1) result -= result / n;

        cout << result << endl;
    }
}
