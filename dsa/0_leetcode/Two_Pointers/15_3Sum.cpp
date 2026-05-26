#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        vector<vector<int>> out;
        sort(nums.begin(), nums.end());
        int n = nums.size();
        cout << n;
        for (int i = 0; i < n; i++)
        {
            if (i > 0 && nums[i] == nums[i - 1])
                continue;
            int sum_needed = -nums[i];
            int left = i + 1;
            int right = n - 1;

            while (left < right)
            {
                int sum = nums[left] + nums[right];
                if (sum > sum_needed)
                {
                    right = right - 1;
                }
                else if (sum < sum_needed)
                {
                    left = left + 1;
                }
                else
                {
                    out.push_back({nums[i], nums[left], nums[right]});

                    while (left < right && nums[left + 1] == nums[left])
                    {
                        left += 1;
                    };
                    while (left < right && nums[right - 1] == nums[right])
                    {
                        right -= 1;
                    };

                    left++;
                    right--;
                }
            }
        }

        return out;
    }
};

int main()
{
    Solution sol;

    vector<int> nums = {-1, 0, 1, 2, -1, -4};

    vector<vector<int>> result = sol.threeSum(nums);

    for (auto triplet : result)
    {
        cout << "[ ";
        for (int num : triplet)
        {
            cout << num << " ";
        }
        cout << "]\n";
    }

    return 0;
}