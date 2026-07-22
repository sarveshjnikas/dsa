#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int m;
    cin >> m;
    vector<vector<int>> a(m, vector<int>(m));

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> a[i][j];
        }
    }

    int n;
    cin >> n;
    vector<vector<int>> b(n, vector<int>(n));
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> b[i][j];
        }
    }

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (a[i][j] == b[0][0])
            {
                bool val = true;
                for (int k = 0; k < n; k++)
                {
                    for (int l = 0; l < n; l++)
                    {
                        if (b[k][l] != a[i + k][j + l])
                        {
                            val = false;
                        }
                    }
                }
                if (val == true)
                {
                    return (i, j);
                }
            }
        }
    }
    return -1;
}
