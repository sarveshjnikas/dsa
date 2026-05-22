#include <iostream>
#include <vector>
using namespace std;

int main()
{
    string s;
    cin >> s;
    int string_length = s.size();
    char look = s[0];
    int ct = 1;
    for (int i = 1; i < string_length; i++)
    {
        if (s[i] == look)
        {
            ct += 1;
        }
        else
        {
            cout << look << ct;
            look = s[i];
            ct = 1;
        }
    }
    cout << look << ct;
}