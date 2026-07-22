#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int m, n, k;
    cin >> m >> n >> k;
    vector<vector<int>> a(m, vector<int>(n));

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> a[i][j];
        }
    }

    vector<vector<int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    vector<vector<int>> b(m, vector<int>(n));
        for (int ite = 0; ite < k; ite++)
        {
            for (int i = 0; i < m; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    long long sum = 0;
                    int count = 0;
                    for (int l = 0; l < 4; l++)
                    {
                        int nr = i + directions[l][0];
                        int nc = j + directions[l][1];
                        if (0 <= nr && nr < m && 0 <= nc && nc < n)
                        {
                            sum = sum + a[nr][nc];
                            count = count + 1;
                        }
                    }
                    b[i][j] = sum / count;
                }
            }
            a = b;
        }

         for (int row = 0; row < m; row++)
            {
                for (int col = 0; col < n; col++)
                {
                    cout << b[row][col] << " ";
                }

               
            }
    }