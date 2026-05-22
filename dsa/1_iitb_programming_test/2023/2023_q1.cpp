#include <iostream>
#include <vector>
using namespace std;

int main (){
    int n;
    cin >> n;
    vector<long long> a(n);

    for (int i =0; i < n; i++){
        cin >> a[i];
    }

    long long sum = 0;

    for (int j = 0; j < n; j++) {
        for (int k = j+1; k < n; k++){
            sum = sum + a[k]*a[j];
        }
    }
    cout << sum;
    return 0;
}
