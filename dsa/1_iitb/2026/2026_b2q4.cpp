#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int m, n;
    cin >> m >> n;
    vector<vector<int>> a(m, vector<int>(n));

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> a[i][j];
        }
    }

    int p, q;
    cin >> p >> q;

    for (int row = 0; row <= m - p; row++)
    {
        for (int col = 0; col <= n - q; col++)
        {
            long long sum = 0;
            for (int i = row; i < row+p; i++)
            {
            for (int j = col; j < col+q; j++)
            {
                sum = sum+ a[i][j];
            }
        }
            cout << sum << " " << endl ;
        }


    }
}