#include <iostream>
#include <vector>
using namespace std;

void armstrong(int x){
    int d = x;
    int num_digits = to_string(x).size();
    long long sum = 0;
    while(x){
        sum = sum + pow(x % 10, num_digits);
        x = x /10;
    }
    if(sum == d){
        cout << "y" << " ";
    } else {
        cout << sum << " ";
    }

    
}

int main(){
    int n;
    cin >> n;
    vector<int> a(n);
    for(int i= 0; i <n; i++){
        cin >> a[i];
    }

    for(int j= 0; j <n; j++){
        armstrong(a[j]);
    }
}