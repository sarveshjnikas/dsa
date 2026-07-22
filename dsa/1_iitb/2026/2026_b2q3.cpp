#include<iostream>
#include<vector>
using namespace std;

int main(){
    int m, n;
    cin >> m >> n;
    vector<vector<int>> a(m, vector<int>(n));
    for(int i=0; i<m; i++){
        for(int j =0; j<n; j++){
            cin >> a[i][j];
        }
    }

    for(int i=0; i<m; i++){
        for(int j =0; j<n; j++){
            bool rowMin = true;
            bool colMax = true;
            
            for(int k=0; k<n; k++){
                if(a[i][k] < a[i][j]){
                rowMin = false;
                break;
                }
            }

            for(int l=0; l<m; l++){
                if(a[l][j] >
                 a[i][j]){
                colMax = false;
                break;
                }

            }

            if(rowMin && colMax){
                cout << a[i][j];
            }
    
        }
    }

    int p, q;
    cin >> p >> q;
    
}