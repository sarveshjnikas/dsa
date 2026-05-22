#include <iostream>
#include <vector>
using namespace std;

int tower_blocks(int n, int k){
    // base cases
    if (n == 0 && k == 0){
        return 1;
    } 

    if (n < 0 || k <0){
        return 0;
    }

    // recurrence
    // we can start the base by taking 1 or 2 or 3
    return tower_blocks(n-1, k-1) +  tower_blocks(n-2, k) + tower_blocks(n-3, k);
}

int main(){
    int n;
    int k;
    cin >> n >> k;
    cout << tower_blocks(n, k);
}