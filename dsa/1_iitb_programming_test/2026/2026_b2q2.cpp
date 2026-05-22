#include <iostream>
using namespace std;

int main(){
    string A;
    string B;

    cin >> A;
    cin >> B;

    int a = A.size();
    int b = B.size();

    for(int i =0; i< a; i++){
        if(A[i] == B[0]){
            if(A.substr(i, b) == B){
                cout << i << " ";
            }
        }
    }
}