#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> a;

    while (n > 0){
        a.push_back(n % 2);
        n = n / 2;
    }

    int best_run = 1;
    int curr_run = 1;
    
    for(int i=1; i< a.size(); i++){
        if (a[i-1] != a[i]){
            curr_run += 1;
        } else {
            best_run = max(best_run, curr_run);
            curr_run = 1;
        }
    }
    cout << best_run;
}