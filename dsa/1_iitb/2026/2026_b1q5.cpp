#include <iostream>
#include <vector>
using namespace std;

int count_binary(int n, int k, int prev){
    if (n==1 && (k == 1 || k ==0)){
        return 1;
    }

    if ( k>= n){
        return 0;
    }

    if (prev == 0){
        return count_binary(n-1, k-1, 1) + count_binary(n-1, k, 0);
    } else {
        return count_binary(n-1, k, 0);
    }

}

int main(){
    int n;
    int k;
    cin >> n >> k;
    cout << count_binary(n, k, 0);
}