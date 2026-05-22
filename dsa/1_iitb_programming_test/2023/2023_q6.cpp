#include <iostream>
#include <vector>

using namespace std;

int check_sum(int sum, vector<int> numbers)
{
    if (numbers.empty())
    {
        return sum == 0;
    }

    int popped = numbers[numbers.size() - 1];
    numbers.pop_back();
    int a = check_sum(sum - popped, numbers);
    int b = check_sum(sum, numbers);

    return a || b;
}

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int sum;
        int x;
        vector<int> arr;
        cin >> sum;

        while (cin >> x && x != -1)
        {
            arr.push_back(x);
        }

        cout << check_sum(sum, arr) << "\n";
    }
}