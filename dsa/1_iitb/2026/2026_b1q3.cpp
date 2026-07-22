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

    int count = 0;
    vector<vector<int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    for (int r = 0; r < m; r++)
    {
        for (int c = 0; c < n; c++)
        {
            int nr, nc;
            bool val = true;
            for (int k = 0; k < directions.size(); k++)
            {
                nr = r + directions[k][0];
                nc = c + directions[k][1];
                if (0 <= nr && nr < m && 0 <= nc && nc < n)
                {
                    if (a[nr][nc] < a[r][c])
                    {
                        val = false;
                    }
                }
            }

            if (val == true)
            {
                cout << r << " " << c << endl;
                count += 1;
            }
        }
    }
    cout << count;
}