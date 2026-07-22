#include<iostream>
#include<vector>
using namespace std;

void disarium(int num){
    int stored= num;
    int total_digits = to_string(num).size();
    long long sum = 0;
    while(num){
        int digit = num % 10;
        sum = sum + pow(digit, total_digits);
        num = num / 10;
        total_digits -= 1;
    }

    if (stored == sum){
        cout << "y" << " ";
    } else {
        cout << sum << " ";
    }
    
}

int main(){
    int n;
    cin >> n;
    vector<int> a(n);
    for(int i =0; i<n; i++){
        cin >> a[i];
    }

    for(int i =0; i<n; i++){
        disarium(a[i]);
    }
}