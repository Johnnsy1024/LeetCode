#include <cstdio>
#include <exception>
#include <iostream>
#include <vector>
using namespace std;

class Solution
{
  public:
    int subSectionSum(std::vector<int> arr, int start, int end)
    {
        int arrLen = arr.size();
        std::vector<int> dp(arrLen);
        dp[0] = arr[0];
        for (int i = 1; i < arrLen; i++)
        {
            dp[i] = dp[i - 1] + arr[i];
        }
        if (start == 0)
        {
            return dp[end];
        }
        else
        {
            return dp[end] - dp[start - 1];
        }
    }
};

int main()
{
    Solution s;
    std::vector<int> arr = {1, 2, 3, 4, 5};
    int start = 0;
    int end = 1;
    int res = s.subSectionSum(arr, start, end);
    printf("%d\n", res);
}