#include<iostream>
#include<vector>
using namespace std;

int main(){
    vector<int> nums = {1,3,6,7,9,4,10,5,6};
    int n = nums.size();
    vector<int> a(n);
    a[0] = 1;
    int max_los = a[0];
    
    for (int i = 1; i < n; i++) {
        int best_guess = 1;
        for (int j = 0; j < i; j++){
            if(nums[j] < nums[i]){
                best_guess = max(best_guess, a[j]+1);
            }
        }
        a[i] = best_guess;
        max_los= max(max_los, best_guess);
    }
    cout << max_los << " " << endl;

    return max_los;
}